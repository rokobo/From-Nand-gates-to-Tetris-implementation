"""Assembler for the Hack assembly language."""

from sys import argv

# Pre-defined symbols
SYMBOLS_TABLE = {"R0": 0, "R1": 1, "R2": 2, "R3": 3,
                 "R4": 4, "R5": 5, "R6": 6, "R7": 7,
                 "R8": 8, "R9": 9, "R10": 10, "R11": 11,
                 "R12": 12, "R13": 13, "R14": 14, "R15": 15,
                 "SCREEN": 16384, "KBD": 24576, "SP": 0,
                 "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4}

COMPUTATION_TABLE = {"0": "101010", "1": "111111", "-1": "111010",
                     "D": "001100", "M": "110000", "!D": "001101",
                     "!M": "110001", "-D": "001111", "-M": "110011",
                     "D+1": "011111", "M+1": "110111", "D-1": "001110",
                     "M-1": "110010", "D+M": "000010", "D-M": "010011",
                     "M-D": "000111", "D&M": "000000", "D|M": "010101"}

DESTINATION_TABLE = {"M": "001", "D": "010", "MD": "011", "A": "100",
                     "AM": "101", "AD": "110", "AMD": "111", "null": "000"}

JUMP_TABLE = {"JMP": "111", "JLE": "110", "JNE": "101", "JLT": "100",
              "JGE": "011", "JEQ": "010", "JGT": "001", "null": "000"}


def raw_commands(asm_file=argv[1]):
    """Generator function for raw Hack commands."""
    file = open(asm_file, "r")

    for line in file:
        raw = line.rstrip()          # Remove blank lines
        raw = raw.split("//", 1)[0]  # Remove Hack comments
        raw = raw.replace(" ", "")   # Remove blank space

        if not raw:                  # Checks if given line is blank space
            continue
        yield raw
    file.close()


def first_pass(asm_file=argv[1]):
    """Creates the complete symbol table for the .asm file."""
    symbols_table = SYMBOLS_TABLE
    current_line = 0

    for line in raw_commands(asm_file):
        # Finds all label definitions and adds them to the table
        if line[0] == "(":
            symbols_table[line[1:-1]] = current_line
        else:
            current_line += 1
    return symbols_table


def second_pass(asm_file=argv[1], symbols_table=first_pass()):
    """
    Substitutes symbols and translates C-instructions.

    Substitutes all symbols for their correct address according to the symbols
    table and translates all C-instructions, then writes them to a .hack file.
    """
    variable_address = 16

    # Write to file with the same name as the .asm but with the .hack file type
    file = open(asm_file.split(".", 1)[0] + ".hack", "w")

    for line in raw_commands(asm_file):
        # Check if we reached a label definition
        if "(" == line[0]:
            continue
        # If line is known symbol, substitute it
        elif line[1:] in symbols_table:
            binary_number = bin(symbols_table[line[1:]]).replace("0b", "")
            binary_instruction = binary_number.zfill(16)
            file.write(binary_instruction + "\n")
            continue
        # If line is a number symbol, substitute it
        elif line[1:].isdigit():
            binary_number = bin(int(line[1:])).replace("0b", "")
            binary_instruction = binary_number.zfill(16)
            file.write(binary_instruction + "\n")
            continue
        # Else: add the symbol to the table starting from address 16
        elif line[0] == "@":
            symbol = line[1:]
            symbols_table[symbol] = variable_address

            binary_number = bin(variable_address).replace("0b", "")
            binary_instruction = binary_number.zfill(16)
            file.write(binary_instruction + "\n")

            variable_address += 1
            continue

        # Not being a symbol, it has to be a C-instruction
        C_instruction = "111"

        # If length of checks > 1, we know there is a jump
        jump_check = line.split(";", 1)
        if len(jump_check) > 1:
            jump_bits = JUMP_TABLE[jump_check[1]]
        else:
            jump_bits = JUMP_TABLE["null"]

        # If length of checks > 1, we know there is a destination
        # Note that there is always a computation
        destination_check = jump_check[0].split("=", 1)
        if len(destination_check) > 1:
            if "M" in destination_check[1]:
                a_bit = "1"
            elif "A" in destination_check[1]:
                destination_check[1] = destination_check[1].replace("A", "M")
                a_bit = "0"
            else:
                a_bit = "0"
            destination_bits = DESTINATION_TABLE[destination_check[0]]
            computation_bits = COMPUTATION_TABLE[destination_check[1]]
        else:
            if "M" in destination_check[0]:
                a_bit = "1"
            else:
                a_bit = "0"
            destination_bits = DESTINATION_TABLE["null"]
            computation_bits = COMPUTATION_TABLE[destination_check[0]]

        C_instruction += a_bit
        C_instruction += computation_bits
        C_instruction += destination_bits
        C_instruction += jump_bits

        file.write(C_instruction + "\n")


if __name__ == "__main__":
    second_pass()
