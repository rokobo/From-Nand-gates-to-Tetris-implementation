// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen.
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen.
// the screen should remain fully clear as long as no key is pressed.

(LOOP)
    @8192
    D=A
    @remaining
    M=D    

    @KBD
    D=M    
    @BLACK
    D; JNE      // If KBD != 0 jump to BLACK

    @remaining
    D=M

(WHITE)
    @SCREEN
    A=D+A
    M=0
    @remaining
    MD=M-1
    @WHITE
    D; JGE     // Checks if all pixels have been painted

    @LOOP
    0; JMP

(BLACK)
    @SCREEN
    A=D+A
    M=-1
    @remaining
    MD=M-1
    @BLACK
    D; JGE     // Checks if all pixels have been painted

    @LOOP
    0; JMP