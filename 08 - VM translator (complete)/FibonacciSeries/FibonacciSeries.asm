// File FibonacciSeries.vm
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

// pop pointer 1           
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@4                             // Go to pointer 1 
M = D                          // Set pointer to D

// push constant 0
@0
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop that 0              
@0                             // GoToSegment that 0
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

// push constant 1
@1
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// pop that 1              
@1                             // GoToSegment that 1
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

// label MAIN_LOOP_START
(MAIN_LOOP_START)              // Define label

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

// if-goto COMPUTE_ELEMENT 
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save Stack top in D
@COMPUTE_ELEMENT               // Load jump coordinates
D; JNE                         // Jump to label if Stack top != 0

// goto END_PROGRAM        
@END_PROGRAM                   // Load jump coordinates
0; JMP                         // Unconditional jump to label

// label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)              // Define label

// push that 0
@0                             // GoToSegment that 0
D = A
@4
A = D + M
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push that 1
@1                             // GoToSegment that 1
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

// pop that 2              
@2                             // GoToSegment that 2
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

// push pointer 1
@4                             // Go to pointer 1 
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

// add
@0                             // UpdateSP(-)
M = M - 1
A = M                          // Go to stack top and record y
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = M + D                      // Save addition in x

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

// goto MAIN_LOOP_START
@MAIN_LOOP_START               // Load jump coordinates
0; JMP                         // Unconditional jump to label

// label END_PROGRAM
(END_PROGRAM)                  // Define label

