// File Sys.vm
// Bootstrap code
@256
D = A
@0
M = D

// Call Sys.init 0
@Sys.init$ret.1                // Save return address in Stack top
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
(Sys.init$ret.1)               // Declare return address

// function Sys.init 0
(Sys.init)                     // Declare label for function and intialize local vars

// push constant 4000	
@4000
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@3                             // Go to pointer 0 
M = D                          // Set pointer to D

// push constant 5000
@5000
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@4                             // Go to pointer 1 
M = D                          // Set pointer to D

// call Sys.main 0
@Sys.main$ret.2                // Save return address in Stack top
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
@Sys.main                      // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Sys.main$ret.2)               // Declare return address


// pop temp 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@6                             // Go to temp 1 
M = D                          // Set temp to D

// label LOOP
(LOOP)                         // Define label

// goto LOOP
@LOOP                          // Load jump coordinates
0; JMP                         // Unconditional jump to label

// function Sys.main 5
(Sys.main)                     // Declare label for function and intialize local vars
@0
A = M
M = 0                          // Set local 0 to 0
A = A + 1
M = 0                          // Set local 1 to 0
A = A + 1
M = 0                          // Set local 2 to 0
A = A + 1
M = 0                          // Set local 3 to 0
A = A + 1
M = 0                          // Set local 4 to 0
A = A + 1
D = A                          // Set SP to Stack top after pushing locals
@0
M = D

// push constant 4001
@4001
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@3                             // Go to pointer 0 
M = D                          // Set pointer to D

// push constant 5001
@5001
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@4                             // Go to pointer 1 
M = D                          // Set pointer to D

// push constant 200
@200
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop local 1
@1                             // GoToSegment local 1
D = A
@1
A = D + M
D = A                          // Record segment location in R13
@R13
M = D
@0                             // UpdateSP(-)
M = M - 1
A = M                          // D = Stack top
D = M
@R13                           // Go back to segment, place Stack top
A = M
M = D

// push constant 40
@40
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop local 2
@2                             // GoToSegment local 2
D = A
@1
A = D + M
D = A                          // Record segment location in R13
@R13
M = D
@0                             // UpdateSP(-)
M = M - 1
A = M                          // D = Stack top
D = M
@R13                           // Go back to segment, place Stack top
A = M
M = D

// push constant 6
@6
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop local 3
@3                             // GoToSegment local 3
D = A
@1
A = D + M
D = A                          // Record segment location in R13
@R13
M = D
@0                             // UpdateSP(-)
M = M - 1
A = M                          // D = Stack top
D = M
@R13                           // Go back to segment, place Stack top
A = M
M = D

// push constant 123
@123
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// call Sys.add12 1
@Sys.add12$ret.3               // Save return address in Stack top
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
@Sys.add12                     // Load jump coordinates
0; JMP                         // Unconditional jump to label
(Sys.add12$ret.3)              // Declare return address


// pop temp 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@5                             // Go to temp 0 
M = D                          // Set temp to D

// push local 0
@0                             // GoToSegment local 0
D = A
@1
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push local 1
@1                             // GoToSegment local 1
D = A
@1
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push local 2
@2                             // GoToSegment local 2
D = A
@1
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push local 3
@3                             // GoToSegment local 3
D = A
@1
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push local 4
@4                             // GoToSegment local 4
D = A
@1
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

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


// function Sys.add12 0
(Sys.add12)                    // Declare label for function and intialize local vars

// push constant 4002
@4002
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 0
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@3                             // Go to pointer 0 
M = D                          // Set pointer to D

// push constant 5002
@5002
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop pointer 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@4                             // Go to pointer 1 
M = D                          // Set pointer to D

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

// push constant 12
@12
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

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


