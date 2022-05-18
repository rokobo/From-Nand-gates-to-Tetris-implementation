// File Sys.vm
// Bootstrap code
@256
D = A
@0
M = D

// Call Sys.init 0
@Sys.init$ret.8                // Save return address in Stack top
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@LCL                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@ARG                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THIS                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THAT                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@0                             // Reposition LCL
D = M
@1
M = D
@5                             // Reposition ARG
D = D - A
@2
M = D
@Sys.init                      // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Sys.init$ret.8)               // Declare return address

// function Sys.init 0
(Sys.init)                     // Declare label for function and intialize local vars

// push constant 6
@6
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 8
@8
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// call Class1.set 2
@Class1.set$ret.9              // Save return address in Stack top
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@LCL                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@ARG                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THIS                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THAT                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@0                             // Reposition LCL
D = M
@1
M = D
@7                             // Reposition ARG
D = D - A
@2
M = D
@Class1.set                    // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Class1.set$ret.9)             // Declare return address


// pop temp 0 
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@5                             // Go to temp 0 
M = D                          // Set temp to D

// push constant 23
@23
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 15
@15
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// call Class2.set 2
@Class2.set$ret.10             // Save return address in Stack top
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@LCL                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@ARG                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THIS                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THAT                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@0                             // Reposition LCL
D = M
@1
M = D
@7                             // Reposition ARG
D = D - A
@2
M = D
@Class2.set                    // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Class2.set$ret.10)            // Declare return address


// pop temp 0 
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@5                             // Go to temp 0 
M = D                          // Set temp to D

// call Class1.get 0
@Class1.get$ret.11             // Save return address in Stack top
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@LCL                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@ARG                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THIS                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THAT                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@0                             // Reposition LCL
D = M
@1
M = D
@5                             // Reposition ARG
D = D - A
@2
M = D
@Class1.get                    // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Class1.get$ret.11)            // Declare return address


// call Class2.get 0
@Class2.get$ret.12             // Save return address in Stack top
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@LCL                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@ARG                           // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THIS                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@THAT                          // Load segment
D = M                          // Save pointer address in D
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D
@0                             // Reposition LCL
D = M
@1
M = D
@5                             // Reposition ARG
D = D - A
@2
M = D
@Class2.get                    // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Class2.get$ret.12)            // Declare return address


// label WHILE
(WHILE)                        // Define label

// goto WHILE
@WHILE                         // Load jump coordinates
0; JMP                         // Unconditional jump to label

// File Class1.vm
// function Class1.set 0
(Class1.set)                   // Declare label for function and intialize local vars

// push argument 0
@0                             // GoToSegment argument 0
D = A
@2
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop static 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@Class1.0                      // Go to the static 0 of the Class1 file 
M = D                          // Set static to D

// push argument 1
@1                             // GoToSegment argument 1
D = A
@2
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop static 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@Class1.1                      // Go to the static 1 of the Class1 file 
M = D                          // Set static to D

// push constant 0
@0
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// return
@1                             // Save end of frame in R13
D = M
@Endframe
M = D
@5                             // Save return address in R5
A = D - A
D = M
@retAddr
M = D
@0                             // Place return value in ARG
A = M - 1
D = M                          // Save return value in D
@2
A = M
M = D
@2                             // Set SP to ARG + 1 (after return value)
D = M + 1
@0
M = D
@1
D = A
@Endframe                      // Go to endframe - 1
A = M - D
D = M                          // Save original memory segment address
@4                             // Restore original memory segment address at RAM[4]
M = D
@2
D = A
@Endframe                      // Go to endframe - 2
A = M - D
D = M                          // Save original memory segment address
@3                             // Restore original memory segment address at RAM[3]
M = D
@3
D = A
@Endframe                      // Go to endframe - 3
A = M - D
D = M                          // Save original memory segment address
@2                             // Restore original memory segment address at RAM[2]
M = D
@4
D = A
@Endframe                      // Go to endframe - 4
A = M - D
D = M                          // Save original memory segment address
@1                             // Restore original memory segment address at RAM[1]
M = D
@retAddr
A = M
0; JMP                         // Unconditional jump to caller's return address


// function Class1.get 0
(Class1.get)                   // Declare label for function and intialize local vars

// push static 0
@Class1.0                      // Go to the static 0 of the Class1 file 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push static 1
@Class1.1                      // Go to the static 1 of the Class1 file 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// sub
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M
A = A - 1
M = D

// return
@1                             // Save end of frame in R13
D = M
@Endframe
M = D
@5                             // Save return address in R5
A = D - A
D = M
@retAddr
M = D
@0                             // Place return value in ARG
A = M - 1
D = M                          // Save return value in D
@2
A = M
M = D
@2                             // Set SP to ARG + 1 (after return value)
D = M + 1
@0
M = D
@1
D = A
@Endframe                      // Go to endframe - 1
A = M - D
D = M                          // Save original memory segment address
@4                             // Restore original memory segment address at RAM[4]
M = D
@2
D = A
@Endframe                      // Go to endframe - 2
A = M - D
D = M                          // Save original memory segment address
@3                             // Restore original memory segment address at RAM[3]
M = D
@3
D = A
@Endframe                      // Go to endframe - 3
A = M - D
D = M                          // Save original memory segment address
@2                             // Restore original memory segment address at RAM[2]
M = D
@4
D = A
@Endframe                      // Go to endframe - 4
A = M - D
D = M                          // Save original memory segment address
@1                             // Restore original memory segment address at RAM[1]
M = D
@retAddr
A = M
0; JMP                         // Unconditional jump to caller's return address


// File Class2.vm
// function Class2.set 0
(Class2.set)                   // Declare label for function and intialize local vars

// push argument 0
@0                             // GoToSegment argument 0
D = A
@2
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop static 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@Class2.0                      // Go to the static 0 of the Class2 file 
M = D                          // Set static to D

// push argument 1
@1                             // GoToSegment argument 1
D = A
@2
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop static 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@Class2.1                      // Go to the static 1 of the Class2 file 
M = D                          // Set static to D

// push constant 0
@0
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// return
@1                             // Save end of frame in R13
D = M
@Endframe
M = D
@5                             // Save return address in R5
A = D - A
D = M
@retAddr
M = D
@0                             // Place return value in ARG
A = M - 1
D = M                          // Save return value in D
@2
A = M
M = D
@2                             // Set SP to ARG + 1 (after return value)
D = M + 1
@0
M = D
@1
D = A
@Endframe                      // Go to endframe - 1
A = M - D
D = M                          // Save original memory segment address
@4                             // Restore original memory segment address at RAM[4]
M = D
@2
D = A
@Endframe                      // Go to endframe - 2
A = M - D
D = M                          // Save original memory segment address
@3                             // Restore original memory segment address at RAM[3]
M = D
@3
D = A
@Endframe                      // Go to endframe - 3
A = M - D
D = M                          // Save original memory segment address
@2                             // Restore original memory segment address at RAM[2]
M = D
@4
D = A
@Endframe                      // Go to endframe - 4
A = M - D
D = M                          // Save original memory segment address
@1                             // Restore original memory segment address at RAM[1]
M = D
@retAddr
A = M
0; JMP                         // Unconditional jump to caller's return address


// function Class2.get 0
(Class2.get)                   // Declare label for function and intialize local vars

// push static 0
@Class2.0                      // Go to the static 0 of the Class2 file 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push static 1
@Class2.1                      // Go to the static 1 of the Class2 file 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// sub
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M
A = A - 1
M = D

// return
@1                             // Save end of frame in R13
D = M
@Endframe
M = D
@5                             // Save return address in R5
A = D - A
D = M
@retAddr
M = D
@0                             // Place return value in ARG
A = M - 1
D = M                          // Save return value in D
@2
A = M
M = D
@2                             // Set SP to ARG + 1 (after return value)
D = M + 1
@0
M = D
@1
D = A
@Endframe                      // Go to endframe - 1
A = M - D
D = M                          // Save original memory segment address
@4                             // Restore original memory segment address at RAM[4]
M = D
@2
D = A
@Endframe                      // Go to endframe - 2
A = M - D
D = M                          // Save original memory segment address
@3                             // Restore original memory segment address at RAM[3]
M = D
@3
D = A
@Endframe                      // Go to endframe - 3
A = M - D
D = M                          // Save original memory segment address
@2                             // Restore original memory segment address at RAM[2]
M = D
@4
D = A
@Endframe                      // Go to endframe - 4
A = M - D
D = M                          // Save original memory segment address
@1                             // Restore original memory segment address at RAM[1]
M = D
@retAddr
A = M
0; JMP                         // Unconditional jump to caller's return address


