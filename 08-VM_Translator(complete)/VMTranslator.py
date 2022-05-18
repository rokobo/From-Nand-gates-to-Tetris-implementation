"""Assembler for translating Jack to VM code."""

from sys import argv
from os import path, walk

SEGMENTS = {"local": 1, "argument": 2, "pointer": 3,
            "this": 3, "that": 4, "temp": 5, "static": 16}

# Variables for unique Clause and Call jump address
ClauseIndex = 0
CallIndex = 1

def raw_commands(vm_file: str):
    """Generator function for raw Jack commands."""
    raw_file = open(vm_file, "r")

    for line in raw_file:
        raw = line.rstrip()          # Remove blank lines
        raw = raw.split("//", 1)[0]  # Remove Hack comments

        if not raw:                  # Checks if given line is blank space
            continue
        yield raw
    raw_file.close()


def GoToStackTop():
    """Goes to the top of the Stack"""
    global file  # necessary for multi-function interaction

    file.write("%-30s %s" % ("@0", "// GoToStackTop\n"))
    file.write("A = M - 1\n")


def GoToSegment(segment: str, index: str, current_file: str = ""):
    """Go to specific segment and index (A becomes segment[index])"""
    global file  # necessary for multi-function interaction
    global file_name # used in some Hack assembly notation

    location = SEGMENTS[segment]

    match segment:
        case "temp" | "pointer":
            file.write("%-30s %s" % ("@{}".format(location + int(index)),
                                     "// Go to {} {} \n".format(segment, index)))
        case "static":
            file.write("%-30s %s" % ("@{}.{}".format(current_file, index),
                       "// Go to the {} {} of the {} file \n".format(segment, index, current_file)))
        case _:
            file.write("%-30s %s" % ("@{}".format(index),
                                     "// GoToSegment {} {}\n".format(segment, index)))
            file.write("D = A\n")
            file.write("@{}\n".format(location))
            file.write("A = D + M\n")


def UpdateSP(change: str):
    """Does SP++ or SP--."""
    global file  # necessary for multi-function interaction

    file.write("%-30s %s" % ("@0", "// UpdateSP({})\n".format(change)))
    file.write("M = M {} 1\n".format(change))


def StoreDTop():
    """Store the D value in the Stack top and do SP++"""
    global file  # necessary for multi-function interaction

    UpdateSP("+")
    file.write("%-30s %s" % ("A = M - 1", "// StoreDTop, used SP++\n"))
    file.write("M = D\n")


def DSavesMThenMoves(direction: str):
    """Saves M in D, then moves +-1 to a given direction."""
    global file  # necessary for multi-function interaction

    file.write("%-30s %s" %
               ("D = M", "// DSavesMThenMoves({})\n".format(direction)))
    file.write("A = A {} 1\n".format(direction))


def CreateTrueFalseClauses(condition: str):
    """Create a True or False clause for x condition y,
    with y being the top-most element in the Stack."""
    global file  # Necessary for multi-function interaction
    global ClauseIndex  # Necessary for unique label definitions

    # Do SP--, subtract two top-most in Stack as X - Y and go to Stack top
    UpdateSP("-")
    file.write("A = M - 1\n")
    DSavesMThenMoves("+")
    file.write("%-30s %s" % ("D = D - M", "// Do x - y\n"))

    # jumps to True case if condition passes, continues if false
    file.write("\n@TRUE_{}\n".format(ClauseIndex))
    file.write("%-30s %s" % ("D; {}".format(condition),
               "// Checks x - y for {}\n".format(condition[1::])))

    # If condition is False
    file.write("@0\n")
    file.write("A = M - 1\n")
    file.write("%-30s %s" % ("M = 0", "// False case\n"))  # 0 = False

    # Jumps to avoid computing the equal case
    file.write("%-30s %s" % ("\n@FALSE_{}".format(ClauseIndex),
               "// Jump to avoid computing True case\n"))
    file.write("0; JMP\n\n")

    # If condition is True
    file.write("%-30s %s" % ("(TRUE_{})".format(ClauseIndex),
               "// True case jump location\n"))
    file.write("@0\n")
    file.write("A = M - 1\n")
    file.write("%-30s %s" % ("M = -1", "// True case\n"))  # -1 = True
    file.write("%-30s %s" % ("(FALSE_{})".format(ClauseIndex),
               "// False case jump location\n"))

    ClauseIndex += 1


def PushPop(command: str, current_file: str = ""):
    """Function for handling push and pop commands."""
    global file  # necessary for multi-function interaction
    global file_name # used in some Hack assembly notation

    match command.split():
        # On pop: Stack top will go to segment[index] (if pointer: changes pointer reference)
        # On push: Segment[index] will go to Stack top
        case["pop", ("pointer" | "temp" | "static") as segment, index]:
            UpdateSP("-")
            file.write("A = M\n")
            file.write("%-30s %s" % ("D = M", "// Save stack top in D\n"))
            GoToSegment(segment, index, current_file)
            file.write("%-30s %s" %
                       ("M = D", "// Set {} to D\n".format(segment)))
        case["pop", "constant", _]:
            raise Exception("Cannot pop constant")
        case["pop", segment, index]:
            # Load segment[index] in R13
            GoToSegment(segment, index)
            file.write("%-30s %s" %
                       ("D = A", "// Record segment location in R13\n"))
            file.write("@R13\n")
            file.write("M = D\n")

            # Set D to Stack top and do SP--
            UpdateSP("-")
            file.write("%-30s %s" % ("A = M", "// D = Stack top\n"))
            file.write("D = M\n")

            # Go back to segment[index] then place Stack top value
            file.write("%-30s %s" %
                       ("@R13", "// Go back to segment, place Stack top\n"))
            file.write("A = M\n")
            file.write("M = D\n")
        case["push", "constant", index]:
            file.write("@{}\n".format(index))
            file.write("D = A\n")
            StoreDTop()
        case["push", segment, index]:
            GoToSegment(segment, index, current_file)
            file.write("D = M\n")
            StoreDTop()
        case _:
            raise Exception(command)


def Label(label: str):
    """Function for handling label definitions."""
    global file  # necessary for multi-function interaction

    file.write("%-30s %s" % ("({})".format(label), "// Define label\n"))
    return


def GoTo(label: str, IsConditional: bool):
    """Function for handling goto commands."""
    global file  # necessary for multi-function interaction

    if IsConditional:
        UpdateSP("-")
        file.write("A = M\n")
        file.write("%-30s %s" % ("D = M", "// Save Stack top in D\n"))
        file.write("%-30s %s" % ("@{}".format(label), "// Load jump coordinates\n"))
        file.write("%-30s %s" % ("D; JNE", "// Jump to label if Stack top != 0\n"))
    else:
        file.write("%-30s %s" % ("@{}".format(label), "// Load jump coordinates\n"))
        file.write("%-30s %s" % ("0; JMP", "// Unconditional jump to label\n"))


def Function(name: str, local_vars: str):
    """Function for handling function definitions."""
    global file  # necessary for multi-function interaction

    file.write("%-30s %s" % ("({})".format(name),
               "// Declare label for function and intialize local vars\n"))

    if local_vars != "0":
        # Initialize local variables to 0
        file.write("@0\n")
        file.write("A = M\n")

        for i in range(int(local_vars)):
            file.write("%-30s %s" %
                    ("M = 0", "// Set local {} to 0\n".format(i)))
            file.write("A = A + 1\n")
        file.write("%-30s %s" %
                   ("D = A", "// Set SP to Stack top after pushing locals\n"))
        file.write("@0\n")
        file.write("M = D\n")


def Return():
    """Function for handling function returns."""
    global file  # necessary for multi-function interaction 

    # Save end of frame and return address
    file.write("%-30s %s" % ("@1", "// Save end of frame in R13\n"))
    file.write("D = M\n")
    file.write("@Endframe\n")
    file.write("M = D\n")

    file.write("%-30s %s" % ("@5", "// Save return address in R5\n"))
    file.write("A = D - A\n")
    file.write("D = M\n")
    file.write("@retAddr\n")
    file.write("M = D\n")

    # Place return value in ARG and set SP to ARG + 1
    file.write("%-30s %s" % ("@0", "// Place return value in ARG\n"))
    file.write("A = M - 1\n")
    file.write("%-30s %s" % ("D = M", "// Save return value in D\n"))
    file.write("@2\n")
    file.write("A = M\n")
    file.write("M = D\n")

    file.write("%-30s %s" % ("@2", "// Set SP to ARG + 1 (after return value)\n"))
    file.write("D = M + 1\n")
    file.write("@0\n")
    file.write("M = D\n")

    # Restore THAT, THIS, ARG and LCL
    for i in range(4, 0, -1):
        file.write("@{}\n".format(5 - i))
        file.write("D = A\n")
        file.write("%-30s %s" % ("@Endframe", "// Go to endframe - {}\n".format(5 - i)))
        file.write("A = M - D\n")
        file.write("%-30s %s" % ("D = M", "// Save original memory segment address\n"))
        file.write("%-30s %s" % ("@{}".format(i),
                   "// Restore original memory segment address at RAM[{}]\n".format(i)))
        file.write("M = D\n")

    # Go to caller's return address
    file.write("@retAddr\n")
    file.write("A = M\n")
    file.write("%-30s %s" % ("0; JMP", "// Unconditional jump to caller's return address\n\n"))


def Call(name: str, pushed_arguments: str):
    """Function for handling call commands."""
    global file  # necessary for multi-function interaction
    global CallIndex # necessary for calling a function multiple times

    # Push return address (defined below)
    file.write("%-30s %s" % ("@{}$ret.{}".format(name, CallIndex),
               "// Save return address in Stack top\n"))
    file.write("D = A\n")
    StoreDTop()

    # Push LCL, ARG, THIS and THAT
    for address in ["@LCL", "@ARG", "@THIS", "@THAT"]:
        file.write("%-30s %s" % (address, "// Load segment\n"))
        file.write("%-30s %s" % ("D = M", "// Save pointer address in D\n"))
        StoreDTop()

    # Reposition ARG and LCL
    file.write("%-30s %s" % ("@0", "// Reposition LCL\n"))
    file.write("D = M\n")
    file.write("@1\n")
    file.write("M = D\n")

    file.write("%-30s %s" % ("@{}".format(int(pushed_arguments) + 5), "// Reposition ARG\n"))
    file.write("D = D - A\n")
    file.write("@2\n")
    file.write("M = D\n")

    # Frame complete, go to desired function
    GoTo(name, False)

    # Declare return address
    file.write("%-30s %s" % ("({}$ret.{})".format(name, CallIndex), 
               "// Declare return address\n\n"))
    CallIndex += 1


def Bootstrap(HasSysInit: bool):
    """Hardware convention bootstrap code."""
    global file  # necessary for multi-function interaction

    file.write("// Bootstrap code\n")
    file.write("@256\n")
    file.write("D = A\n")
    file.write("@0\n")
    file.write("M = D\n")

    if HasSysInit:
        file.write("\n// Call Sys.init 0\n")
        Call("Sys.init", "0")


def translator(absolute_path: str, HasSysInit: bool, current_file: str = ""):
    """Translates each instruction as a comment, then the asm translation."""
    global file  # necessary for multi-function interaction
    global file_name # used in some Hack assembly notation

    if HasSysInit:
        Bootstrap(True)

    for line in raw_commands(absolute_path):
        file.write("// {}\n".format(line))
        match line.split():
            case["pop" | "push", *args]:
                PushPop(line, current_file)
            case["label", label]:
                Label(label)
            case["if-goto", label]:
                GoTo(label, True)
            case["goto", label]:
                GoTo(label, False)
            case["function", name, local_vars]:
                Function(name, local_vars)
            case["return"]:
                Return()
            case["call", name, arguments]:
                Call(name, arguments)
            case["add"]:
                # SP-- and add two top-most in Stack (y is top-most in x+y)
                UpdateSP("-")
                file.write("%-30s %s" %
                           ("A = M", "// Go to stack top and record y\n"))
                DSavesMThenMoves("-")
                file.write("%-30s %s" %
                           ("M = M + D", "// Save addition in x\n"))
            case["sub"]:
                # SP--, subtract x-y, record in Stack top
                UpdateSP("-")
                file.write("A = M - 1\n")
                DSavesMThenMoves("+")
                file.write("D = D - M\n")
                file.write("A = A - 1\n")
                file.write("M = D\n")
            case["neg"]:
                GoToStackTop()
                file.write("M = -M\n")
            case["not"]:
                GoToStackTop()
                file.write("M = !M\n")
            case["or"]:
                # Use the inner most element to calculate OR and store in M
                GoToStackTop()
                DSavesMThenMoves("-")
                file.write("M = D|M\n")
                UpdateSP("-")
            case["and"]:
                # Use the inner most element to calculate AND and store in M
                GoToStackTop()
                DSavesMThenMoves("-")
                file.write("M = D&M\n")
                UpdateSP("-")
            case["eq"]:
                CreateTrueFalseClauses("JEQ")
            case["gt"]:
                CreateTrueFalseClauses("JGT")
            case["lt"]:
                CreateTrueFalseClauses("JLT")
            case _:
                raise Exception(line, line.split())
        file.write("\n")


def input_handler(input: str):
    """Handles the various inputs the program might receive."""
    global file  # necessary for multi-function interaction
    global file_name # used in some Hack assembly notation

    file_name = path.basename(input).replace(".vm", "")
    script_directory = path.dirname(__file__)
    absolute_path = path.join(script_directory, input)
    folder_name = path.basename(path.dirname(absolute_path))

    if ".vm" in input: # For handling .vm file as input
        if file_name == "Sys": # If sys.vm, name the .asm file with folder name
            location = path.join(script_directory, folder_name, folder_name + ".asm")
            HasSysInit = True
        else: # Else, name it with the same name as the original .vm file
            location = absolute_path.replace(".vm", ".asm")
            HasSysInit = False

        file = open(location, "w")
        translator(absolute_path, HasSysInit)

    else: # For handling directory as input
        file = open(path.join(absolute_path, file_name + ".asm"), "w")

        # Check if Sys.vm exists (it has to be executed first)
        if path.isfile(path.join(absolute_path, "Sys.vm")):
            file.write("// File Sys.vm\n")
            translator(path.join(absolute_path, "Sys.vm"), True)

        # translate all .vm files in directory
        for _, _, files in walk(absolute_path):
            for DirFile in files:
                if DirFile.endswith(".vm") and DirFile != "Sys.vm":
                    # current_file is used for per-file static segments
                    current_file = DirFile.replace(".vm", "") 
                    file.write("// File {}\n".format(DirFile))
                    location = path.join(absolute_path, DirFile)
                    translator(location, False, current_file)

    file.close()


if __name__ == "__main__":
    # Allows the translatation of multiple files at the same time
    
    for argument in argv[1:]:
        input_handler(argument)
