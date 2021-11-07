// File StaticTest.vm
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
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@StaticTest.8                  // Go to the static 8 of the StaticTest file 
M = D                          // Set static to D

// pop static 3
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@StaticTest.3                  // Go to the static 3 of the StaticTest file 
M = D                          // Set static to D

// pop static 1
@0                             // UpdateSP(-)
M = M - 1
A = M
D = M                          // Save stack top in D
@StaticTest.1                  // Go to the static 1 of the StaticTest file 
M = D                          // Set static to D

// push static 3
@StaticTest.3                  // Go to the static 3 of the StaticTest file 
D = M
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push static 1
@StaticTest.1                  // Go to the static 1 of the StaticTest file 
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
@StaticTest.8                  // Go to the static 8 of the StaticTest file 
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

