"""Assembler for translating Jack to VM code."""

from sys import argv

SEGMENTS = {"local": 1, "argument": 2, "pointer": 3,
            "this": 3, "that": 4, "temp": 5, "static": 16}
ClauseIndex = 0


def raw_commands(vm_file):
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


def GoToSegment(segment, index):
    """Go to specific segment and index (A becomes segment[index])"""
    global file  # necessary for multi-function interaction

    match segment:
        case "temp" | "static":
            location = SEGMENTS[segment]
            file.write("%-30s %s" % ("@{}".format(location + int(index)),
                                     "// Go to {} {} \n".format(segment, index)))
        case 'pointer':
            location = SEGMENTS["pointer"]
            file.write("%-30s %s" % ("@{}".format(location + int(index)),
                                     "// GoToSegment Pointer {}\n".format(index)))
        case _:
            location = SEGMENTS[segment]
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


def CreateTrueFalseClauses(condition):
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


def PushPop(command):
    """Push and Pop commands are the most used, so it made sense to separate them,
    specially because in the some other commands, delegating push and pop makes
    the code more organized and more efficient."""
    global file  # necessary for multi-function interaction

    match command.split():
        # On pop: Stack top will go to segment[index] (if pointer: changes pointer reference)
        # On push: Segment[index] will go to Stack top
        case["pop", ("pointer" | "temp") as segment, index]:
            UpdateSP("-")
            file.write("A = M\n")
            file.write("%-30s %s" % ("D = M", "// Save stack top in D\n"))
            GoToSegment(segment, index)
            location = SEGMENTS[segment]
            file.write("%-30s %s" %
                       ("M = D", "// Set {} to D\n".format(segment)))
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
            # Load constant in D
            file.write("@{}\n".format(index))
            file.write("D = A\n")
            StoreDTop()
        case["push", ("pointer" | "temp") as segment, index]:
            # Push the base address of given pointer
            GoToSegment(segment, index)
            file.write("D = M\n")
            StoreDTop()
        case["push", segment, index]:
            # Load value of segment[index] in D
            match segment:
                case["static"]:
                    file.write("@Foo.{}\n".format(index + 16))
                case["temp"]:
                    file.write("@{}\n".format(index + 5))
                case _:
                    GoToSegment(segment, index)
            file.write("D = M\n")
            StoreDTop()


def translator(vm_file):
    """Translates each instruction as a comment, then the asm translation."""
    global file  # necessary for multi-function interaction
    # Write to file with the same name as the .vm but with the .asm file type
    file = open(vm_file.split(".", 1)[0] + ".asm", "w")

    for line in raw_commands(vm_file):
        file.write("// {}\n".format(line))
        match line.split():
            case["pop" | "push", *args]:
                PushPop(line)
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
    file.close


if __name__ == "__main__":
    for file in argv[1:]:
        translator(file)
