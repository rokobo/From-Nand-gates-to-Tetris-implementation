// Multiplies RAM[0] and RAM[1] and stores the result in RAM[2].
// This program handles arguments that satisfy:
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    @R2 
    M=0    // Sets answer to 0 (avoid RAM[2] alredy having a number)

    @R0
    D=M
    @END
    D; JEQ // Terminates program if R0 == 0 (makes the program faster)

    @R1
    D=M
    @END
    D; JEQ // Terminates program if R1 == 0 (makes the program faster)

    @count // Sets how many times we should sum 
    M=D    // R1 is alredy loaded into D

(LOOP)
    @R0    // Load RAM[0] in D for sum
    D=M
    @R2
    M=M+D  // Accumulates result
    @count
    M=M-1  // Increments count because we added RAM[1] one more time
    D=M    // Loads the count for checking if we finished multiplying

    @LOOP
    D; JGT // Does the loop again if count != RAM[0]

(END)
    @END
    0; JMP // End of program