# From Nand gates to Tetris implementation

This project's goal is to implement Tetris on a computer implemented from the ground up (starting with an abstraction of Nand gates). This project was done in 13 subprojects, each in their respective folder.

## 1 - Elementary logic gates

In this part, Hardware Description Language (HDL) was used to create 15 elementary logic gates: `Not`, `And`, `Or`, `Xor`, `Mux`, `DMux`, `Not16`, `And16`, `Or16`, `Mux16`, `Or8Way`, `Mux4Way16`, `Mux8Way16`, `DMux4Way`, `DMux8Way`. These gates were built either from the primitive `Nand` gate or from previously built gates.

Together with the .hdl files, there is also a .tst and a .cmp file for each logic gate. They are used to test and compare the functionality of the logic gate, respectively. To test a logic gate, simply:

1. Open the Simulation tools folder and open the HardwareSimulator.bat.
2. Press file > load chip, then select the chip you want to test.
3. Press file > load script, then select the .tst file for the chip you selected.
4. Press run > run, to run the script (you can adjust the speed in the slow-fast dial).

## 2 - Arithmetic gates

In this part, logic gates were implemented to create an Arithmetic Logic Unit (ALU), specifically: 

+ `HalfAdder` - Sums two input bits and outputs the sum and the carry bit.
+ `FullAdder` - Sums two input bits and one carry bit and outputs the sum and the carry bit.
+ `Add16` - Adds two 16-bit integers in Two's complement.
+ `Inc16` - Adds 1 to 16-bit integers.
+ `ALU` - Arithmetic Logic Unit, used to compute various operations, according to the following table:

![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/ALU_truth_table.png?raw=true)

## 3 - Memory chips

## 4 - Machine language programs

## 5 - Computer architecture

## 6 - Hack assembler

## 7 -

## 8 -

## 9 -

## 10 -

## 11 -

## 12 -

## 13 -