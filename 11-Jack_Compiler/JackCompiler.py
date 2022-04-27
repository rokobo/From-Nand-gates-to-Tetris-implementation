"""
JackAnalyzer is desined to compile Jack files into VM files.
"""

from sys import argv
from os import path, walk
import re
import time


class JackAnalyzer:
    def __init__(
            self, enable_assert: bool, logs: bool,
            print_symbols: bool) -> None:
        self.asserts = enable_assert
        self.log = logs
        self.print_symbols = print_symbols
        self.operators = {
            '+': 'add', '-': 'sub', '*': 'call Math.multiply 2',
            '/': 'call Math.divide 2', '&': 'and', '|': 'or', '<': 'lt',
            '>': 'gt', '=': 'eq'
        }
        self.constants = {
            'this': 'push pointer 0', 'true': 'push constant 0\nnot',
            'false': 'push constant 0', 'null': 'push constant 0'
        }
        self.while_label = -1
        self.if_label = -1
        self.colors = {
            "empty": "",
            # Cyan background and Black text
            "do": "\033[46m\033[30mDo statement\033[00m",
            # Red text
            "term": "\033[31mTerm\033[00m",
            # Green text
            "let compile array": "\033[32mLet compile array\033[00m",
            "let compile expression": "\033[32mLet compile expression\033[00m",
            # Yellow text
            "parenthesis": "\033[33mParenthesis\033[00m",
            # Red background and White text
            "let": "\033[41mLet statement\033[00m",
            # Green background and Black text
            "if": "\033[42m\033[30mIf statement\033[00m",
            # Yellow background and Black text
            "while": "\033[43m\033[30mWhile statement\033[00m",
            # Blue background and White text
            "return": "\033[44mReturn statement\033[00m",
            # Magenta background and White text
            "call": "\033[45mCall statement\033[00m",
            # Bright Red text
            "advance": "\033[91mtoken\033[00m",
            # Bright Yellow text
            "array call": "\033[93mArray call\033[00m",
            # Bright Cyan text
            "expression": "\033[96mExpression\033[00m",

            "string": "\033[94mString\033[00m",
            # Underlined (all as follows)
            "args list": "\033[04mArgs List\033[0m:",
            "total args": "\033[04mTotal Args\033[0m:",
            "class": "\033[04mClass\033[0m",
            "subroutinedec": "\033[04mSubroutineDec\033[0m",
            "statements": "\033[04mStatements\033[0m",
            "engine": "\033[04mEngine\033[0m"
            }
        return

    def print_log(
        self, initial_word: str, log_target: str, optional_text=""
    ) -> None:
        """Prints prompt logs of the functions of this program."""
        if not self.log:
            return
        output = f"{initial_word} {self.colors[log_target]}"
        if not optional_text:
            output += f" '{self.token0}', {self.token_index[0]}"
        else:
            output += f" {optional_text}"
        print(output)
        return

    def input_handler(self) -> None:
        """Handles the input (file or folder)."""
        input = argv[1]
        script_directory = path.dirname(__file__)
        absolute_path = path.join(script_directory, input)
        if ".jack" in input:  # For handling .jack file as input
            self.jack_file = open(absolute_path, "r")
            location = absolute_path.replace(".jack", ".vm")
            self.vm_file = open(location, "w")
            self.JackTokenizer()
            self.compileClass()
            self.close()
        else:  # For handling directory as input
            for _, _, files in walk(absolute_path):
                for DirFile in files:
                    if DirFile.endswith(".jack"):
                        current_file = DirFile.replace(".jack", ".vm")
                        self.jack_file = open(
                            path.join(absolute_path, DirFile), "r"
                        )
                        self.vm_file = open(
                            path.join(absolute_path, current_file), "w"
                        )
                        self.JackTokenizer()
                        self.compileClass()
                        self.close()
        return

    def JackTokenizer(self) -> None:
        """Produces a list of all tokens in the file."""
        self.tokens = []
        comment = False
        for line in self.jack_file:
            # Delete comments
            raw = line.split("//", 1)[0]

            if "*/" in raw:  # For multi-line comments
                raw = raw.split("*/", 1)[-1]
                comment = False
            if comment:  # For multi-line comments
                continue

            if "/**" in raw:  # For multi-line comments
                raw = raw.split("/**", 1)[0]
                comment = True

            # Separate tokens into:
            # Numbers and negative numbers like -1
            # Strings like "Hello world"
            # And all other tokens
            raw = filter(None, re.split(r'(-\d*)|(\".*\")|(\W)', raw))

            # Delete whitespace elements
            raw = [elem for elem in raw if elem.strip()]
            if not raw:
                continue
            self.tokens += raw

        # Token information
        self.token_index = [0, len(self.tokens)]
        self.token0 = self.tokens[0]
        self.token1 = self.tokens[1]
        self.createSymbolTable()
        return

    def createSymbolTable(self) -> None:
        """Creates the symbol table for the current file."""
        self.symbolTable = {"class": {}}
        class_name = self.tokens[1]
        index = 3

        # For class level symbols
        class_types = {"field": 0, "static": 0}
        while self.tokens[index] in ["field", "static"]:
            kind = self.tokens[index]
            current_type = self.tokens[index + 1]
            self.symbolTable["class"][self.tokens[index + 2]] = {
                "type": current_type,
                "kind": kind,
                "occurrence": class_types[kind]
            }
            class_types[kind] += 1
            index += 3
            # multiple variables in one field/static assignment
            while self.tokens[index] == ",":
                self.symbolTable["class"][self.tokens[index + 1]] = {
                    "type": current_type,
                    "kind": kind,
                    "occurrence": class_types[kind]
                }
                class_types[kind] += 1
                index += 2
            index += 1

        # For constructor, methods and functions level symbols
        positions = [
            i for i, w in enumerate(self.tokens)
            if w in ("constructor", "method", "function")
        ]  # Gives location of all constructor, methods and functions

        for i in positions:
            index = i
            types = {"argument": 0, "local": 0}
            table_name = self.tokens[index + 2]
            self.symbolTable[table_name] = {}

            # For methods, THIS is the first argument
            if self.tokens[index] == "method":
                self.symbolTable[table_name]["this"] = {
                        "type": class_name,
                        "kind": "argument",
                        "occurrence": types["argument"]
                    }
                types["argument"] += 1
            index += 4
            # For argument variables
            if self.tokens[index] != ")":
                self.symbolTable[table_name][self.tokens[index + 1]] = {
                        "type": self.tokens[index],
                        "kind": "argument",
                        "occurrence": types["argument"]
                    }
                types["argument"] += 1
                index += 2

                while self.tokens[index] == ",":
                    self.symbolTable[table_name][self.tokens[index + 2]] = {
                        "type": self.tokens[index + 1],
                        "kind": "argument",
                        "occurrence": types["argument"]
                    }
                    types["argument"] += 1
                    index += 3
            index += 2

            # For local variable assignment
            while self.tokens[index] == "var":
                current_type = self.tokens[index + 1]
                self.symbolTable[table_name][self.tokens[index + 2]] = {
                        "type": current_type,
                        "kind": "local",
                        "occurrence": types["local"]
                    }
                types["local"] += 1
                index += 3
                while self.tokens[index] == ",":
                    self.symbolTable[table_name][self.tokens[index + 1]] = {
                        "type": current_type,
                        "kind": "local",
                        "occurrence": types["local"]
                    }
                    types["local"] += 1
                    index += 2
                index += 1

        if self.print_symbols:
            for name, table in self.symbolTable.items():
                print(f"---------------(Current scope: {name})---------------")
                for key, value in table.items():
                    print(key, ':', value)
                print("\n")
        return

    def accessSymbol(self, symbol) -> str:
        """Access symbols in the symbol table (class or subroutine)."""
        try:
            data = self.symbolTable[self.subroutine_name][symbol]
        except KeyError:
            try:
                data = self.symbolTable["class"][symbol]
            except KeyError:
                raise Exception(f"Variable {symbol} not in symbol table")
        return data

    def advance(self, offset=1) -> None:
        """Advances the tokens by the offset (can be negative)."""
        self.token_index[0] += offset
        # Prevent list index being out of bounds
        try:
            self.token0 = self.tokens[self.token_index[0]]
            try:
                self.token1 = self.tokens[self.token_index[0] + 1]
            except IndexError:
                self.token1 = ""
        except IndexError:
            self.token0 = ""
            self.token1 = ""
        self.print_log("    Advanced", "advance")
        return

    def compileClass(self) -> None:
        """Handles all functions, methods and constructors."""
        self.print_log("Started", "class")
        self.class_name = self.token1
        self.vm_file.write(f"// Class {self.class_name}\n")
        positions = [
            i for i, w in enumerate(self.tokens)
            if w in ("constructor", "method", "function")
        ]
        for index in positions:
            self.token_index[0] = index
            self.advance(0)
            self.compileSubroutineDec()
        self.print_log("Finished", "class")
        return

    def compileSubroutineDec(self) -> None:
        """Handles a single function, method or constructor."""
        self.print_log("Started", "subroutinedec")

        # Function name
        self.function_type = self.token0
        self.advance()
        self.return_var = False if self.token0 == "void" else True
        self.subroutine_name = self.token1
        push_vars = sum(
            x["kind"] == "local" for x in
            self.symbolTable[self.subroutine_name].values()
        )
        self.vm_file.write(
            "function {}.{} {}\n".format(
                self.class_name, self.subroutine_name, push_vars
            )
        )

        # Allocate space for object in case of constructor
        if self.function_type == "constructor":
            fields = sum(
                x["kind"] == "field" for x in
                self.symbolTable["class"].values()
            )
            self.vm_file.write(
                f"push constant {fields}\n"
            )
            self.vm_file.write("call Memory.alloc 1\n")
            self.vm_file.write("pop pointer 0\n")
        elif self.function_type == "method":
            self.vm_file.write("push argument 0\n")
            self.vm_file.write("pop pointer 0\n")

        # advance to subroutine body statements
        while self.token0 not in ["do", "let", "if", "while", "return"]:
            self.advance()
        self.compileStatements()
        self.print_log("Finished", "subroutinedec")
        return

    def compileStatements(self) -> None:
        """Handles all statements."""
        self.print_log("Started", "statements")

        while self.token0 not in ("return", "}"):
            if self.token0 == "let":
                self.compileLet()
            elif self.token0 == "do":
                self.compileDo()
            elif self.token0 == "if":
                self.compileIf()
            elif self.token0 == "while":
                self.compileWhile()

        if self.token0 == "return":
            self.compileReturn()

        self.print_log("Finished", "statements")
        return

    def compileLet(self) -> None:
        """Compiles let statements."""
        self.print_log("Started", "let")
        # Determine the variable being assigned
        data = self.accessSymbol(self.token1)

        # Determine if we have an array being assigned
        self.advance()
        array_access = False
        if self.token1 == ".":
            self.compileCall()
        elif self.token1 == "[":
            array_access = True
            occurrence = data["occurrence"]
            kind = data["kind"]
            self.vm_file.write(f"push {kind} {occurrence}\n")
            self.advance(2)
            self.print_log("    Started", "let compile array")
            self.compileExpression()
            self.print_log("    Finished", "let compile array")
            self.vm_file.write("add\n")
            self.advance()
        else:
            self.advance()
        self.advance()
        self.print_log("    Started", "let compile expression")
        self.compileExpression()
        self.print_log("    Finished", "let compile expression")

        # Finally assign to variable
        kind = data["kind"]
        occurrence = data["occurrence"]
        if array_access:
            self.vm_file.write("pop temp 0\n")
            self.vm_file.write("pop pointer 1\n")
            self.vm_file.write("push temp 0\n")
            kind = "that"
            occurrence = 0
        elif kind == "field":
            kind = "this"
        self.vm_file.write(f"pop {kind} {occurrence}\n")
        if self.token1 == ";":
            self.advance(2)
        else:
            self.advance()
        self.print_log("Finished", "let")
        return

    def compileIf(self) -> None:
        """Compiles if statements."""
        self.if_label += 1
        self.print_log("Started", "if")

        # Compiled expression in if condition
        self.advance(2)
        self.compileExpression()
        self.advance()
        if self.asserts:
            assert self.token0 == "{", f"{self.token0}, {self.token1}"

        # Invert condition for better computation
        self.vm_file.write("not\n")

        # if-goto label in case of false
        label = self.if_label
        self.vm_file.write(f"if-goto IF_FALSE_{label}\n")

        # true case statements
        self.advance()
        self.compileStatements()

        # goto label for true case statement execution
        self.vm_file.write(f"goto IF_TRUE_{label}\n")

        # true case label
        self.vm_file.write(f"label IF_FALSE_{label}\n")

        # false case statements
        if self.asserts:
            assert self.token0 == "}", f"{self.token0}, {self.token1}"
        if self.token1 == "else":
            self.advance(3)
            self.compileStatements()

        while self.token0 != "}":
            self.advance()
        self.advance()

        # end of if condition in case of true case execution
        self.vm_file.write(f"label IF_TRUE_{label}\n")
        self.print_log("Finished", "if")
        return

    def compileWhile(self) -> None:
        """Compiles while statements."""
        self.while_label += 1
        label = self.while_label
        self.print_log("Started", "while")

        # First label
        self.vm_file.write(f"label WHILE_START_{label}\n")

        # Compile expression for condition
        self.advance(2)
        self.compileExpression()

        # Invert expression for easier computation
        self.vm_file.write("not\n")

        # if-goto label
        self.vm_file.write(f"if-goto WHILE_END_{label}\n")

        # Compiled statements for while not completed
        self.advance(2)
        self.compileStatements()
        self.advance()

        # goto label to return to beggining of while computation
        self.vm_file.write(f"goto WHILE_START_{label}\n")

        # Second label for when while expression finishes
        self.vm_file.write(f"label WHILE_END_{label}\n")
        self.print_log("Finished", "while")
        return

    def compileDo(self) -> None:
        """Compiles do statements."""
        self.print_log("Started", "do")
        self.advance()
        self.compileCall()
        self.advance()
        if self.asserts:
            assert self.token0 == ";", f"Expected ; got {self.token0}"
        # Do statement return does not matter
        self.vm_file.write("pop temp 0\n")
        self.advance()
        self.print_log("Finished", "do")
        return

    def compileCall(self) -> None:
        """Compiles call statements."""
        self.print_log("Started", "call")
        function_name = self.token0
        self.advance()
        local_method_call = False
        OS_call = False

        # Call to an external class method
        # Happens when we call a method on an object of another class
        external_obj_call = any(
            function_name in self.symbolTable[d] for d in self.symbolTable
        )

        # Variable definition based on an external class
        # Happens in constructors only
        external_class_def = False
        if self.function_type == "constructor":
            for scope in self.symbolTable:
                for var in self.symbolTable[scope]:
                    if function_name == self.symbolTable[scope][var]["type"]:
                        external_class_def = external_class_def or True

        # Correct function name to call
        if self.token0 == ".":
            if external_obj_call:
                data = self.accessSymbol(function_name)
                function_name = data["type"] + self.token0 + self.token1
            else:
                # We know the call is to an OS function because
                # we are not calling a function defined in the class
                # variables and we are not calling a local function
                OS_call = True
                function_name += self.token0 + self.token1
            self.advance(3)
        else:
            # Method call for a local function of the current class
            local_method_call = True
            function_name = self.class_name + "." + function_name
            self.advance()

        # Determine what arguments to call
        args = []
        parenthesis = 0
        index = self.token_index[0]
        while self.tokens[index] != ")" or parenthesis != 0:
            element = self.tokens[index]
            if element == "(":
                parenthesis += 1
            elif element == ")":
                parenthesis -= 1
            args.append(element)
            index += 1
        self.print_log("        ", "args list", str(args))

        # Determine how many arguments to call
        if not args:
            args = 0
            self.advance()
        elif args.count(",") == 0:
            args = 1
        else:
            args = args.count(",") + 1
        self.print_log("        ", "total args", str(args))

        # Compile each argument
        if external_class_def or OS_call:
            pass
        elif external_obj_call:
            reference = data["occurrence"]
            kind = data["kind"]
            if kind != "local":
                kind = "this"
            self.vm_file.write(f"push {kind} {reference}\n")
        elif self.function_type == "constructor" or local_method_call:
            self.vm_file.write("push pointer 0\n")

        for _ in range(args):
            self.compileExpression()
            self.advance()

        self.advance(-1)

        # Update how many arguments to call since we may need to
        # pass the current object as an argument
        if external_class_def or OS_call:
            pass
        elif external_obj_call:
            args += 1
        elif self.function_type == "constructor" or local_method_call:
            args += 1

        # Finish by calling the function
        self.vm_file.write(f"call {function_name} {args}\n")
        self.print_log("Finished", "call")
        return

    def compileReturn(self) -> None:
        """Compiles return statements."""
        self.print_log("Started", "return")
        # Check if there is something to return
        if self.return_var:
            self.advance()
            self.compileExpression()
            self.vm_file.write("return\n")
        else:
            self.vm_file.write("push constant 0\n")
            self.vm_file.write("return\n")
        self.advance()
        self.print_log("Finished", "return")
        return

    def compileExpression(self):
        """Compiles all expressions present in statements."""
        self.print_log("Started", "expression")
        while self.token0 not in (";", ",", ")", "]"):
            # Simple numbers
            if self.token0.isnumeric():
                self.vm_file.write(f"push constant {self.token0}\n")
                self.advance()
            # Negative numbers
            elif len(self.token0) > 1 and self.token0[0] == "-":
                self.vm_file.write(f"push constant {self.token0[1:]}\n")
                self.vm_file.write("neg\n")
                self.advance()
            # Keyword constants
            elif self.token0 in ("true", "false", "null", "this"):
                self.vm_file.write(f"{self.constants[self.token0]}\n")
                self.advance()
            # Calls like Screen.drawRectangle
            elif self.token1 == ".":
                self.compileCall()
                self.advance()
            # Array access
            elif self.token1 == "[":
                self.print_log("        Started", "array call")
                data = self.accessSymbol(self.token0)
                occurence = data["occurrence"]
                self.vm_file.write(f"push local {occurence}\n")
                self.advance(2)
                self.compileExpression()
                self.vm_file.write("add\n")
                self.vm_file.write("pop pointer 1\n")
                self.vm_file.write("push that 0\n")
                self.advance()
                self.print_log("        Finished", "array call")
            # Symbol table variables
            elif any(
                self.token0 in self.symbolTable[d]
                for d in self.symbolTable
            ):
                self.compileTerm()
            # Parenthesis computations that take priority
            elif self.token0 == "(":
                self.print_log("        Started", "parenthesis")
                self.advance()
                self.compileExpression()
                self.advance()
                self.print_log("        Finished", "parenthesis")
            # Operations
            elif self.token0 in ("/", "*", "+", "-", ">", "<", "|", "&", "="):
                operator = self.token0
                self.advance()
                self.compileExpression()
                self.vm_file.write(f"{self.operators[operator]}\n")
            # Unary operator
            elif self.token0 in ("~"):
                self.advance()
                self.compileExpression()
                self.vm_file.write("not\n")
            # String
            elif '"' in self.token0:
                self.print_log(
                    "    Started",
                    "string",
                    f"with {len(self.token0) - 2} chars"
                )
                self.vm_file.write(f"push constant {len(self.token0) - 2}\n")
                self.vm_file.write("call String.new 1\n")
                for char in self.token0[1:-1]:
                    self.vm_file.write(
                        f"push constant {ord(char)}\n")
                    self.vm_file.write("call String.appendChar 2\n")
                self.advance()
                self.print_log("    Finished", "string")
            else:
                raise Exception(
                    f"Unknown term '{self.token0}' not in symbol table"
                )
        self.print_log("Finished", "expression")
        return

    def compileTerm(self) -> None:
        """Compiles variables present in the symbol table."""
        self.print_log("Started", "term")
        data = self.accessSymbol(self.token0)
        kind = data["kind"]
        if kind == "field":
            kind = "this"
        occurrence = data["occurrence"]
        self.vm_file.write(f"push {kind} {occurrence}\n")
        self.advance()
        self.print_log("Finished", "term")
        return

    def close(self) -> None:
        """Closes Jack and VM files."""
        self.jack_file.close()
        self.vm_file.close()
        return


if __name__ == "__main__":
    start = time.perf_counter()
    analyzer = JackAnalyzer(
        True,  # Enable assert statements
        False,  # Enable program logs
        False,  # Print symbol table at prompt
    )
    analyzer.input_handler()
    end = time.perf_counter() - start
    print(f"\nProgram finished in {round(end * 1000, 3)} miliseconds")
