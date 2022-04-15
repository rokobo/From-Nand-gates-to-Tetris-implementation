"""
JackAnalyzer is desined to translate Jack files into a XML parse tree.
"""

from sys import argv
from os import path, walk
import re
import time


class JackAnalyzer:
    def __init__(self, enable_assert, enable_dataless_tags, enable_logs):
        self.indentation_space = "  "
        self.asserts = enable_assert
        self.all_tags = enable_dataless_tags
        self.log = enable_logs
        return

    def input_handler(self):
        input = argv[1]
        script_directory = path.dirname(__file__)
        absolute_path = path.join(script_directory, input)
        self.indentation = 1 if self.all_tags else 0
        if ".jack" in input:  # For handling .jack file as input
            self.jack_file = open(absolute_path, "r")
            location = absolute_path.replace(".jack", ".xml")
            self.xml_file = open(location, "w")
            self.JackTokenizer()
            self.CompilationEngine()
            self.close()
        else:  # For handling directory as input
            for _, _, files in walk(absolute_path):
                for DirFile in files:
                    if DirFile.endswith(".jack"):
                        current_file = DirFile.replace(".jack", ".xml")
                        self.jack_file = open(
                            path.join(absolute_path, DirFile), "r"
                        )
                        self.xml_file = open(
                            path.join(absolute_path, current_file), "w"
                        )
                        self.JackTokenizer()
                        self.CompilationEngine()
                        self.close()

    def JackTokenizer(self):
        self.xml_file.write("<class>\n")
        self.tokens = []
        texts = []
        for line in self.jack_file:
            # Delete comments
            raw = line.split("//", 1)[0]
            raw = raw.split("/**", 1)[0]
            if '"' in raw:  # Fixes string parsing
                texts.append(raw.split('"')[1].rstrip())
            # Separate tokens
            raw = re.split(r'(\W)', raw)

            # Delete whitespace elements
            raw = [elem for elem in raw if elem.strip()]
            if not raw:
                continue
            self.tokens += raw

        # Join separated string elements
        # ['"', 'hello', 'world', '"'] -> ['"', 'hello world', '"']
        quote_list = [i for i, j in enumerate(self.tokens) if j == '\"']
        offset = 0
        for index in range(0, len(quote_list), 2):
            i = quote_list[index] - offset
            j = quote_list[index + 1] - offset
            offset += quote_list[index + 1] - quote_list[index]
            text = f'"{texts[int(index/2)]}"'
            self.tokens[i:j+1] = [text]

        # Token information
        self.token_index = [0, len(self.tokens)]
        self.token0 = self.tokens[0]
        self.token1 = self.tokens[1]
        self.tokenType()

    def tokenType(self):
        keyword = [
            "class", "method", "function", "constructor", "int",
            "boolean", "char", "void", "var", "static", "field",
            "let", "do", "if", "else", "while", "return", "true",
            "false", "null", "this"
        ]
        symbol = [
            "{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-",
            "*", "/", "&", "|", "<", ">", "=", "~"
        ]

        self.types = []
        for item in self.tokens:
            if item in keyword:
                self.types.append("keyword")
            elif item in symbol:
                self.types.append("symbol")
            elif '\"' in item:
                self.types.append("stringConstant")
            elif item.isdigit():
                self.types.append("integerConstant")
            else:
                self.types.append("identifier")

    def currentType(self):
        return self.types[self.token_index[0]]

    def advance(self):
        self.token_index[0] += 1
        # Prevent list index being out of bounds
        self.token0 = self.token1
        if self.token_index[0] >= self.token_index[1] - 2:
            self.token1 = ""
        else:
            self.token1 = self.tokens[self.token_index[0] + 1]
        if self.log:
            print(f"    Advanced token '{self.token0}'")

    def space(self):
        return self.indentation_space * self.indentation

    def compileClass(self):
        self.xml_file.write(
            self.space() + "<keyword> class </keyword>\n"
        )
        self.advance()
        self.xml_file.write(
            self.space() + f"<identifier> {self.token0} </identifier>\n"
        )
        self.advance()
        assert self.token0 == "{", f"Expected {{ got {self.token0}"
        self.xml_file.write(
            self.space() + "<symbol> { </symbol>\n"
        )
        self.advance()

        self.compileClassVarDec()
        self.compileSubroutineDec()
        self.xml_file.write(
            self.space() + "<symbol> } </symbol>\n"
        )
        return

    def compileClassVarDec(self):
        if self.log:
            print(f"Started ClassVarDec '{self.token0}'")
        if self.token0 not in ("static", "field"):
            return
        while self.token0 in ("static", "field"):
            if self.all_tags:
                self.xml_file.write(
                    self.space() + "<classVarDec>\n"
                )
                self.indentation += 1
            # Add type and as many var names as present
            self.xml_file.write(
                self.space() + f"<keyword> {self.token0} </keyword>\n"
            )
            self.advance()

            if self.token0 in ("int", "boolean", "char"):
                self.xml_file.write(
                    self.space() + f"<keyword> {self.token0} </keyword>\n"
                )
                self.advance()
            else:
                self.xml_file.write(
                        self.space() +
                        f"<identifier> {self.token0} </identifier>\n"
                    )
                self.advance()

            while self.token0 != ";":
                if self.token0 in ("int", "boolean", "char"):
                    self.xml_file.write(
                        self.space() + f"<keyword> {self.token0} </keyword>\n"
                    )
                    self.advance()
                else:
                    self.xml_file.write(
                        self.space() +
                        f"<identifier> {self.token0} </identifier>\n"
                    )
                    self.advance()
                if self.token0 == ",":
                    self.xml_file.write(
                        self.space() + "<symbol> , </symbol>\n"
                    )
                    self.advance()

            self.xml_file.write(
                self.space() + "<symbol> ; </symbol>\n"
            )

            self.advance()
            if self.all_tags:
                self.indentation -= 1
                self.xml_file.write(
                    self.space() + "</classVarDec>\n"
                )
        if self.log:
            print(f"Finished ClassVarDec '{self.token0}'")
        return

    def compileSubroutineDec(self):
        if self.log:
            print(f"Started SubroutineDec '{self.token0}'")
        if self.token0 not in ("constructor", "function", "method"):
            return

        while self.token0 in ("constructor", "function", "method"):
            if self.all_tags:
                self.xml_file.write(
                    self.space() + "<subroutineDec>\n"
                )
                self.indentation += 1
            # Function, construcor of method
            self.xml_file.write(
                self.space() + f"<keyword> {self.token0} </keyword>\n"
            )
            self.advance()

            # function type
            if self.token0 != "void":
                self.xml_file.write(
                    self.space() +
                    f"<identifier> {self.token0} </identifier>\n"
                )
            else:
                self.xml_file.write(
                    self.space() + "<keyword> void </keyword>\n"
                )
            self.advance()

            # function, constructor, method name
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()

            # parameter list and subroutine body
            assert self.token0 == "(", f"Expected ( got {self.token0}"
            self.xml_file.write(
                self.space() + "<symbol> ( </symbol>\n"
            )
            self.advance()

            self.compileParameterList()

            assert self.token0 == ")", f"Expected ) got {self.token0}"
            self.xml_file.write(
                self.space() + "<symbol> ) </symbol>\n"
            )
            self.advance()

            self.compileSubroutineBody()
            if self.all_tags:
                self.indentation -= 1
                self.xml_file.write(
                    self.space() + "</subroutineDec>\n"
                )
        return

    def compileParameterList(self):
        if self.log:
            print(f"Started ParameterList '{self.token0}'")
        if self.token0 == ")":
            if self.all_tags:
                self.xml_file.write(
                    self.space() + "<parameterList>\n"
                )
                self.xml_file.write(
                    self.space() + "</parameterList>\n"
                )
            return

        while self.token0 in ("int", "boolean, char"):
            # parameterList tag for every int, boolean, char
            if self.all_tags:
                self.xml_file.write(
                    self.space() + "<parameterList>\n"
                )
                self.indentation += 1

            # Add type and as many var names as present
            while self.token0 != ")":
                # Type
                types = ("int", "char", "boolean")
                self.xml_file.write(
                    self.space() + f"<keyword> {self.token0} </keyword>\n"
                )
                assert self.token0 in types, f"Expected type got {self.token0}"
                self.advance()

                # variable name
                self.xml_file.write(
                    self.space() +
                    f"<identifier> {self.token0} </identifier>\n"
                )
                self.advance()

                # possibly more variables
                if self.token0 == ",":
                    self.xml_file.write(
                        self.space() + "<symbol> , </symbol>\n"
                    )
                    self.advance()

            # End tag
            if self.all_tags:
                self.indentation -= 1
                self.xml_file.write(
                    self.space() + "</parameterList>\n"
                )
        return

    def compileSubroutineBody(self):
        if self.log:
            print(f"Started SubroutineBody '{self.token0}'")
        # subroutineBody tag
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<subroutineBody>\n"
            )
            self.indentation += 1

        self.xml_file.write(
            self.space() + "<symbol> { </symbol>\n"
        )
        assert self.token0 == "{", f"Expected {{ got {self.token0}"
        self.advance()

        # Statements
        while self.token0 == "var":
            self.compileVarDec()
        self.compileStatements()

        self.xml_file.write(
            self.space() + "<symbol> } </symbol>\n"
        )
        # self.advance()

        # End tag
        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</subroutineBody>\n"
            )
        if self.log:
            print(f"Finished SubroutineBody '{self.token0}'")
        return

    def compileVarDec(self):
        if self.log:
            print(f"Started VarDec '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<varDec>\n"
            )
            self.indentation += 1
        # standard tags for var statement
        self.xml_file.write(
            self.space() + "<keyword> var </keyword>\n"
        )
        self.advance()

        if self.token0 in ("int", "boolean", "char"):
            self.xml_file.write(
                self.space() + f"<keyword> {self.token0} </keyword>\n"
            )
            self.advance()
        else:
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()

        self.xml_file.write(
            self.space() + f"<identifier> {self.token0} </identifier>\n"
        )
        self.advance()

        while self.token0 != ";":
            self.xml_file.write(
                self.space() + "<symbol> , </symbol>\n"
            )
            self.advance()
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()

        # end for standard tags for var statement
        self.xml_file.write(
            self.space() + "<symbol> ; </symbol>\n"
        )
        self.advance()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</varDec>\n"
            )
        if self.log:
            print(f"Finished VarDec '{self.token0}'")
        return

    def compileStatements(self):
        if self.log:
            print(f"Started Statements '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<statements>\n"
            )
            self.indentation += 1

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

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</statements>\n"
            )
        if self.log:
            print(f"Finished Statements '{self.token0}'")
        return

    def compileLet(self):
        if self.log:
            print(f"Started Let '{self.token0}'")
        # standard tags for let statement
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<letStatement>\n"
            )
            self.indentation += 1

        # let statement
        self.xml_file.write(
            self.space() + "<keyword> let </keyword>\n"
        )
        self.advance()

        self.xml_file.write(
            self.space() + f"<identifier> {self.token0} </identifier>\n"
        )
        self.advance()

        if self.token0 in ("["):
            self.xml_file.write(
                self.space() + "<symbol> [ </symbol>\n"
            )
            self.advance()
            self.compileExpression()
            assert self.token0 == "]", f"Expected ] got {self.token0}"
            self.xml_file.write(
                self.space() + "<symbol> ] </symbol>\n"
            )
            self.advance()

        self.xml_file.write(
            self.space() + "<symbol> = </symbol>\n"
        )
        assert self.token0 == "=", f"Expected = got {self.token0}"
        self.advance()

        self.compileExpression()
        # end for standard tags for let statement
        assert self.token0 == ";", f"Expected ; got {self.token0}"
        self.xml_file.write(
            self.space() + "<symbol> ; </symbol>\n"
        )
        self.advance()
        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</letStatement>\n"
            )
        return

    def compileIf(self):
        if self.log:
            print(f"Started If '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<ifStatement>\n"
            )
            self.indentation += 1

        self.xml_file.write(
            self.space() + "<keyword> if </keyword>\n"
        )
        assert self.token0 == "if", f"Expected if got {self.token0}"
        self.advance()

        # Expressions
        self.xml_file.write(
            self.space() + "<symbol> ( </symbol>\n"
        )
        assert self.token0 == "(", f"Expected ( got {self.token0}"
        self.advance()

        self.compileExpression(True)
        self.xml_file.write(
            self.space() + "<symbol> ) </symbol>\n"
        )
        assert self.token0 == ")", f"Expected ) got {self.token0}"
        self.advance()

        # Statements
        self.xml_file.write(
            self.space() + "<symbol> { </symbol>\n"
        )
        assert self.token0 == "{", f"Expected {{ got {self.token0}"
        self.advance()

        self.compileStatements()

        self.xml_file.write(
            self.space() + "<symbol> } </symbol>\n"
        )
        assert self.token0 == "}", f"Expected }} got {self.token0}"
        self.advance()

        # Else + statements
        if self.token0 == "else":
            self.xml_file.write(
                self.space() + "<keyword> else </keyword>\n"
            )
            self.advance()

            self.xml_file.write(
                self.space() + "<symbol> { </symbol>\n"
            )
            assert self.token0 == "{", f"Expected {{ got {self.token0}"
            self.advance()

            self.compileStatements()

            self.xml_file.write(
                self.space() + "<symbol> } </symbol>\n"
            )
            assert self.token0 == "}", f"Expected }} got {self.token0}"
            self.advance()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</ifStatement>\n"
            )
        return

    def compileWhile(self):
        if self.log:
            print(f"Started While '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<whileStatement>\n"
            )
            self.indentation += 1

        self.xml_file.write(
            self.space() + "<keyword> while </keyword>\n"
        )
        self.advance()

        # Expressions
        self.xml_file.write(
            self.space() + "<symbol> ( </symbol>\n"
        )
        assert self.token0 == "(", f"Expected ( got {self.token0}"
        self.advance()

        self.compileExpression(True)

        self.xml_file.write(
            self.space() + "<symbol> ) </symbol>\n"
        )
        assert self.token0 == ")", f"Expected ) got {self.token0}"
        self.advance()

        # Statements
        self.xml_file.write(
            self.space() + "<symbol> { </symbol>\n"
        )
        assert self.token0 == "{", f"Expected {{ got {self.token0}"
        self.advance()

        self.compileStatements()

        self.xml_file.write(
            self.space() + "<symbol> } </symbol>\n"
        )
        assert self.token0 == "}", f"Expected }} got {self.token0}"
        self.advance()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</whileStatement>\n"
            )
        return

    def compileDo(self):
        if self.log:
            print(f"Started Do '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<doStatement>\n"
            )
            self.indentation += 1

        self.xml_file.write(
            self.space() + "<keyword> do </keyword>\n"
        )
        assert self.token0 == "do", "Expected do got {self.token0}"
        self.advance()

        self.xml_file.write(
            self.space() + f"<identifier> {self.token0} </identifier>\n"
        )
        self.advance()

        if self.token0 == ".":  # className or varName
            self.xml_file.write(
                self.space() + "<symbol> . </symbol>\n"
            )
            self.advance()
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()

        self.xml_file.write(
            self.space() + "<symbol> ( </symbol>\n"
        )
        assert self.token0 == "(", f"Expected ( got {self.token0}"
        self.advance()

        self.compileExpressionList()

        self.xml_file.write(
            self.space() + "<symbol> ) </symbol>\n"
        )
        assert self.token0 == ")", f"Expected ) got {self.token0}"
        self.advance()
        self.xml_file.write(
            self.space() + "<symbol> ; </symbol>\n"
        )
        self.advance()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</doStatement>\n"
            )
        return

    def compileReturn(self):
        if self.log:
            print(f"Started Return '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<returnStatement>\n"
            )
            self.indentation += 1

        self.xml_file.write(
            self.space() + "<keyword> return </keyword>\n"
        )
        self.advance()

        if self.token0 != ";":
            self.compileExpression()

        self.xml_file.write(
            self.space() + "<symbol> ; </symbol>\n"
        )
        self.advance()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</returnStatement>\n"
            )
        self.advance()
        if self.log:
            print(f"Finished Return '{self.token0}'")
        return

    def compileExpression(self, possibleUnary=False):
        if self.log:
            print(f"Started Expression '{self.token0}'")
        if self.token0 != ")":
            # start expression tag
            if self.all_tags:
                self.xml_file.write(
                    self.space() + "<expression>\n"
                )
                self.indentation += 1

            while self.token0 not in (";", ",", ")", "]"):
                if possibleUnary and self.token0 in ("~", "-"):
                    if self.all_tags:
                        self.xml_file.write(
                            self.space() + "<term>\n"
                        )
                        self.indentation += 1
                    self.xml_file.write(
                        self.space() + f"<symbol> {self.token0} </symbol>\n"
                    )
                    self.advance()
                    self.compileTerm()
                    if self.all_tags:
                        self.indentation -= 1
                        self.xml_file.write(
                            self.space() + "</term>\n"
                        )
                elif self.token0 in (".", "/", "*", "|", "+", "-", "~"):
                    self.xml_file.write(
                        self.space() + f"<symbol> {self.token0} </symbol>\n"
                    )
                    self.advance()
                elif self.token0 in ("<", ">", "&"):
                    switch = {"<": "&lt;", ">": "&gt;", "&": "&amp;"}
                    self.xml_file.write(
                        self.space() +
                        f"<symbol> {switch[self.token0]} </symbol>\n"
                    )
                    self.advance()
                elif self.token0 in ("="):
                    self.xml_file.write(
                        self.space() +
                        f"<symbol> {self.token0} </symbol>\n"
                    )
                    self.advance()
                else:
                    self.compileTerm()

            # end expression tag
            if self.all_tags:
                self.indentation -= 1
                self.xml_file.write(
                    self.space() + "</expression>\n"
                )
        if self.log:
            print(f"Finished Expression '{self.token0}'")
        return

    def compileTerm(self):
        if self.log:
            print(f"Started Term '{self.token0}'")
        # start term tag
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<term>\n"
            )
            self.indentation += 1
        if self.token1 == ".":
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()
            self.xml_file.write(
                self.space() + "<symbol> . </symbol>\n"
            )
            self.advance()
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()
            assert self.token0 == "(", f"Expected ( got {self.token0}"
            self.xml_file.write(
                self.space() + "<symbol> ( </symbol>\n"
            )
            self.advance()
            self.compileExpressionList()
            assert self.token0 == ")", f"Expected ) got {self.token0}"
            self.xml_file.write(
                self.space() + "<symbol> ) </symbol>\n"
            )
        elif self.token1 == "[":
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )
            self.advance()
            self.xml_file.write(
                self.space() + "<symbol> [ </symbol>\n"
            )
            self.advance()
            self.compileExpression()
            self.xml_file.write(
                self.space() + "<symbol> ] </symbol>\n"
            )
            assert self.token0 == "]", f"Expected ], got {self.token0}"
        elif self.token0 == "(":
            self.xml_file.write(
                self.space() + "<symbol> ( </symbol>\n"
            )
            self.advance()
            self.compileExpression(True)
            self.xml_file.write(
                self.space() + "<symbol> ) </symbol>\n"
            )
            assert self.token0 == ")", f"Expected ), got {self.token0}"
        elif self.token0 == "this":
            self.xml_file.write(
                self.space() + f"<keyword> {self.token0} </keyword>\n"
            )
        elif self.currentType() == "stringConstant":
            string = self.token0.strip('"')
            self.xml_file.write(
                self.space() +
                f"<stringConstant> {string} </stringConstant>\n"
            )
        elif self.currentType() == "integerConstant":
            self.xml_file.write(
                self.space() +
                f"<integerConstant> {self.token0} </integerConstant>\n"
            )
        elif self.token0 in ("false", "true", "null"):
            self.xml_file.write(
                self.space() + f"<keyword> {self.token0} </keyword>\n"
            )

        else:
            self.xml_file.write(
                self.space() + f"<identifier> {self.token0} </identifier>\n"
            )

        # end term tag
        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</term>\n"
            )
        self.advance()
        if self.log:
            print(f"Finished Term '{self.token0}'")
        return

    def compileExpressionList(self):
        if self.log:
            print(f"Started ExpressionList '{self.token0}'")
        if self.all_tags:
            self.xml_file.write(
                self.space() + "<expressionList>\n"
            )
            self.indentation += 1

        while self.token0 != ")":
            if self.token0 == ",":
                self.xml_file.write(
                    self.space() + "<symbol> , </symbol>\n"
                )
                self.advance()
            else:
                self.compileExpression()

        if self.all_tags:
            self.indentation -= 1
            self.xml_file.write(
                self.space() + "</expressionList>\n"
            )
        return

    def CompilationEngine(self):
        if self.log:
            print(f"Started Engine '{self.token0}'")
        i = 0
        while True:
            if self.token0 == "class":
                self.compileClass()

            self.advance()
            if self.token0 == "":
                break
            i += 1
            if i == 20000:
                break

    def close(self):
        self.xml_file.write("</class>")
        self.jack_file.close()
        self.xml_file.close()


if __name__ == "__main__":
    start = time.time()
    # JackAnalyzer - Asserts, Complete XML tags, Program logs
    analyzer = JackAnalyzer(True, True, False)
    analyzer.input_handler()
    end = time.time() - start
    print(f"\nProgram finished in {round(end * 1000, 3)} miliseconds")
