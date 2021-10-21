// push constant 3030
@3030
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
@3                             // Go to pointer 0 base address
M = D                          // Set stack top to base address

// push constant 3040
@3040
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
@4                             // Go to pointer 1 base address
M = D                          // Set stack top to base address

// push constant 32
@32
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop this 2
@2                             // GoToSegment this 2
D = A
@3
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

// push constant 46
@46
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop that 6
@6                             // GoToSegment that 6
D = A
@4
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

// push pointer 0
@3
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push pointer 1
@4
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

// push this 2
@2                             // GoToSegment this 2
D = A
@3
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

// push that 6
@6                             // GoToSegment that 6
D = A
@4
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

