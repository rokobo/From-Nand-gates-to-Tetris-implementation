// File BasicLoop.vm
// push constant 0
@0
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop local 0         
@0                             // GoToSegment local 0
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

// label LOOP_START
(LOOP_START)                   // Define label

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

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

// pop local 0	        
@0                             // GoToSegment local 0
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

// pop argument 0      
@0                             // GoToSegment argument 0
D = A
@2
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

// if-goto LOOP_START  
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save Stack top in D
@LOOP_START                    // Load jump coordinates
D; JNE                         // Jump to label if Stack top != 0

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

