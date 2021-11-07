// File Sys.vm
// Bootstrap code
@256
D = A
@0
M = D

// Call Sys.init 0
@Sys.init$ret.4                // Save return address in Stack top
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
(Sys.init$ret.4)               // Declare return address

// function Sys.init 0
(Sys.init)                     // Declare label for function and intialize local vars

// push constant 4
@4
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// call Main.fibonacci 1   
@Main.fibonacci$ret.5          // Save return address in Stack top
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
@6                             // Reposition ARG
D = D - A
@2
M = D
@Main.fibonacci                // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Main.fibonacci$ret.5)         // Declare return address


// label WHILE
(WHILE)                        // Define label

// goto WHILE              
@WHILE                         // Load jump coordinates
0; JMP                         // Unconditional jump to label

// File Main.vm
// function Main.fibonacci 0
(Main.fibonacci)               // Declare label for function and intialize local vars

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

// push constant 2
@2
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// lt                     
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_9
D; JLT                         // Checks x - y for LT
@0
A = M - 1
M = 0                          // False case

@FALSE_9                      // Jump to avoid computing True case
0; JMP

(TRUE_9)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_9)                      // False case jump location

// if-goto IF_TRUE
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save Stack top in D
@IF_TRUE                       // Load jump coordinates
D; JNE                         // Jump to label if Stack top != 0

// goto IF_FALSE
@IF_FALSE                      // Load jump coordinates
0; JMP                         // Unconditional jump to label

// label IF_TRUE          
(IF_TRUE)                      // Define label

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


// label IF_FALSE         
(IF_FALSE)                     // Define label

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

// push constant 2
@2
D = A
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

// call Main.fibonacci 1  
@Main.fibonacci$ret.6          // Save return address in Stack top
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
@6                             // Reposition ARG
D = D - A
@2
M = D
@Main.fibonacci                // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Main.fibonacci$ret.6)         // Declare return address


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

// push constant 1
@1
D = A
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

// call Main.fibonacci 1  
@Main.fibonacci$ret.7          // Save return address in Stack top
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
@6                             // Reposition ARG
D = D - A
@2
M = D
@Main.fibonacci                // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Main.fibonacci$ret.7)         // Declare return address


// add                    
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

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


