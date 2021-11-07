// push constant 17
@17
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 17
@17
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// eq
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_0
D; JEQ                         // Checks x - y for EQ
@0
A = M - 1
M = 0                          // False case

@FALSE_0                      // Jump to avoid computing True case
0; JMP

(TRUE_0)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_0)                      // False case jump location

// push constant 17
@17
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 16
@16
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// eq
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_1
D; JEQ                         // Checks x - y for EQ
@0
A = M - 1
M = 0                          // False case

@FALSE_1                      // Jump to avoid computing True case
0; JMP

(TRUE_1)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_1)                      // False case jump location

// push constant 16
@16
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 17
@17
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// eq
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_2
D; JEQ                         // Checks x - y for EQ
@0
A = M - 1
M = 0                          // False case

@FALSE_2                      // Jump to avoid computing True case
0; JMP

(TRUE_2)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_2)                      // False case jump location

// push constant 892
@892
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 891
@891
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

@TRUE_3
D; JLT                         // Checks x - y for LT
@0
A = M - 1
M = 0                          // False case

@FALSE_3                      // Jump to avoid computing True case
0; JMP

(TRUE_3)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_3)                      // False case jump location

// push constant 891
@891
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 892
@892
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

@TRUE_4
D; JLT                         // Checks x - y for LT
@0
A = M - 1
M = 0                          // False case

@FALSE_4                      // Jump to avoid computing True case
0; JMP

(TRUE_4)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_4)                      // False case jump location

// push constant 891
@891
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 891
@891
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

@TRUE_5
D; JLT                         // Checks x - y for LT
@0
A = M - 1
M = 0                          // False case

@FALSE_5                      // Jump to avoid computing True case
0; JMP

(TRUE_5)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_5)                      // False case jump location

// push constant 32767
@32767
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 32766
@32766
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// gt
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_6
D; JGT                         // Checks x - y for GT
@0
A = M - 1
M = 0                          // False case

@FALSE_6                      // Jump to avoid computing True case
0; JMP

(TRUE_6)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_6)                      // False case jump location

// push constant 32766
@32766
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 32767
@32767
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// gt
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_7
D; JGT                         // Checks x - y for GT
@0
A = M - 1
M = 0                          // False case

@FALSE_7                      // Jump to avoid computing True case
0; JMP

(TRUE_7)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_7)                      // False case jump location

// push constant 32766
@32766
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 32766
@32766
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// gt
@0                             // UpdateSP(-)
M = M - 1
A = M - 1
D = M                          // DSavesMThenMoves(+)
A = A + 1
D = D - M                      // Do x - y

@TRUE_8
D; JGT                         // Checks x - y for GT
@0
A = M - 1
M = 0                          // False case

@FALSE_8                      // Jump to avoid computing True case
0; JMP

(TRUE_8)                       // True case jump location
@0
A = M - 1
M = -1                         // True case
(FALSE_8)                      // False case jump location

// push constant 57
@57
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 31
@31
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// push constant 53
@53
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

// push constant 112
@112
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

// neg
@0                             // GoToStackTop
A = M - 1
M = -M

// and
@0                             // GoToStackTop
A = M - 1
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = D&M
@0                             // UpdateSP(-)
M = M - 1

// push constant 82
@82
D = A
@0                             // UpdateSP(+)
M = M + 1
A = M - 1                      // StoreDTop, used SP++
M = D

// or
@0                             // GoToStackTop
A = M - 1
D = M                          // DSavesMThenMoves(-)
A = A - 1
M = D|M
@0                             // UpdateSP(-)
M = M - 1

// not
@0                             // GoToStackTop
A = M - 1
M = !M

