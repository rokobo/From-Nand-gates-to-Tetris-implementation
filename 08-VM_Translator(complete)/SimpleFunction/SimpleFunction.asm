// File SimpleFunction.vm
// function SimpleFunction.test 2
(SimpleFunction.test)          // Declare label for function and intialize local vars
@0
A = M
M = 0                          // Set local 0 to 0
A = A + 1
M = 0                          // Set local 1 to 0
A = A + 1
D = A                          // Set SP to Stack top after pushing locals
@0
M = D

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

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

// not
@0                             // GoToStackTop
A = M - 1
M = !M

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

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

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


