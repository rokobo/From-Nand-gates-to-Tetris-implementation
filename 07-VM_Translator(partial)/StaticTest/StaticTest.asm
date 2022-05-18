// push constant 111
@111
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 333
@333
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 888
@888
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop static 8
@24                            // Go to static 8 
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

// pop static 3
@19                            // Go to static 3 
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

// pop static 1
@17                            // Go to static 1 
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

// push static 3
@19                            // Go to static 3 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push static 1
@17                            // Go to static 1 
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

// push static 8
@24                            // Go to static 8 
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

