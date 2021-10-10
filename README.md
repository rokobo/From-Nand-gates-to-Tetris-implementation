# From Nand gates to Tetris implementation

This project's goal is to implement Tetris on a computer (specifically the Hack computer) implemented from the ground up (starting with an abstraction of Nand gates). This project was done in 13 subprojects, each in their respective folder.

## Testing

### Testing .hdl files

Together with the .hdl files, there is also a .tst and a .cmp file for each logic gate. They are used to test and compare the functionality of the logic gate, respectively. To test a logic gate, simply:

1. Open the Simulation tools folder and open the HardwareSimulator.bat.
2. Press file > load chip, then select the chip you want to test.
3. Press file > load script, then select the .tst file for the chip you selected.
4. Press run > run, to run the script (you can adjust the speed in the slow-fast dial).

After the script is run, the program will output a .out file that will be compared to the .cmp file. If they are equal, the test will be considered sucessful.

### Testing .asm files

Like .hdl files, .asm files will have a .tst and .cmp file together. However, .asm files are test in the CPU emulator:

1. Open the Simulation tools folder and open the CPUEmulator.bat.
2. Press file > load program, then select the program you want to test.
3. Press file > load script, then select the .tst file for the program you selected.
4. Press run > run, to run the script (you can adjust the speed in the slow-fast dial).
5. Press the keyboard icon to link your keyboard to the emulator.

### Testing .hack files

.hack files are programs that can be used to test the `Computer.hdl` file in subproject 5. They do not have to be directly interacted with, since the .tst file will load the appropriate .hack file into the computer's ROM.

### Testing the Hack assembler

To test the conversion of .asm files into .hack files in subproject 6, use the Assembler program:

1. Open the Simulation tools folder and open the Assembler.bat.
2. Press file > load source file, then select the .asm file you want to test.
3. Press file > load comparison file, then select the .hack file you got from your assembler.
4. Press run > fast translation, to run the script.

## 1 - Elementary logic gates

In this part, Hardware Description Language (HDL) was used to create 15 elementary logic gates: 

+ `Not` - Inverts the input bit.
+ `And` - Outputs 1 if both inputs are 1.
+ `Or` - Outputs 1 if either input is 1.
+ `Xor` - Outputs 1 if only one input is 1.
+ `Mux` - Has two inputs, one selector bit and one output. The selector bit chooses which input to output.
+ `DMux` - Has one input, one selector bit and two outputs. The selector bit chooses which output the input will go through. In case it chooses the `a` output, the `b` output will be 0.
+ `Not16` - `Not` gate for 16-bit integer.
+ `And16` - `And` gate for 16-bit integer.
+ `Or16` - `Or` gate for 16-bit integer.
+ `Mux16` - `Mux` gate for 16-bit integer.
+ `Or8Way` - `Or` gate for 8-bit integer.
+ `Mux4Way16` - `Mux` gate for 16-bit integer with 4 inputs instead of 2.
+ `Mux8Way16` - `Mux` gate for 16-bit integer with 8 inputs instead of 2.
+ `DMux4Way` - `DMux` gate with 4 outputs  instead of 2.
+ `DMux8Way` - `DMux` gate with 8 outputs  instead of 2.

These gates were built either from the primitive `Nand` gate or from previously built gates.


## 2 - Arithmetic gates

In this part, logic gates were implemented to create an Arithmetic Logic Unit (ALU), specifically: 

+ `HalfAdder.hdl` - Sums two input bits and outputs the sum and the carry bit.
+ `FullAdder.hdl` - Sums two input bits and one carry bit and outputs the sum and the carry bit.
+ `Add16.hdl` - Adds two 16-bit integers in Two's complement.
+ `Inc16.hdl` - Adds 1 to 16-bit integers.
+ `ALU.hdl` - Arithmetic Logic Unit, used to compute various operations, according to the following table:

![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/ALU_truth_table.png?raw=true)

## 3 - Memory chips

In this part, the following memory chips were implemented from the abstraction of the primitive Data Flip-Flop (DFF) gate:

+ `Bit.hdl` - 1-bit Register.
+ `Register.hdl` - 16-bit Register.
+ `RAM8.hdl` - 16-bit RAM with 8 register of memory.
+ `RAM64.hdl` - 16-bit RAM with 64 register of memory.
+ `RAM512.hdl` - 16-bit RAM with 512 register of memory.
+ `RAM4K.hdl` - 16-bit RAM with 4096 register of memory.
+ `RAM16K.hdl` - 16-bit RAM with 16384 register of memory.
+ `PC.hdl` - 16-bit program counter.

## 4 - Machine language programs

In this part, we used Assembly to create two programs that will run eventually run on the Hack computer:

+ `Mult.asm` - Multiplies `RAM[0]` and `RAM[1]` and stores the result in `RAM[2]`.
+ `Fill.asm` - Runs an infinite loop that listens to the keyboard input. When a key is pressed (any key), the program blackens the screen and should remain fully black as long as the key is pressed. When no key is pressed, the program clears the screen. The screen should remain fully clear as long as no key is pressed.

## 5 - Computer architecture

In this part, the following memory chips were implemented to complete the construction of the Hack computer:

+ `Memory.hdl` - Entire RAM address space for the computer (`RAM16K`, Keyboard and Screen).
+ `CPU.hdl` - The Hack CPU.
+ `Computer.hdl` - The Hack computer platform.

Additionally, the followig programs can be used to test the Hack computer:

+ `Add.hack` - Adds up the two constants 2 and 3 and writes the result in `RAM[0]`.
+ `Max.hack` - Computes the maximum of `RAM[0]` and `RAM[1]` and writes the result in `RAM[2]`.
+ `Rect.hack` - Draws a rectangle of width 16 pixels and length `RAM[0]` at the top left of the screen.

## 6 - Hack assembler

In this part, a assembler needed to be built to translate .asm files into .hack files. All .hack instructions are a single 16-bit integer that can be translated according to:

+ A-instructions - Used for addressing, where `@value` sets the A register to `value` and consequently, the `RAM[value]` register becomes selected. To translate A-instructions, we use a 0 plus the binary form of `value`.

    `0000000000010101` = `@21`
+ C-intructions - Used for calculation. To translate C-instructions, we use a 111, plus a selector bit (to choose between using A or M), plus six computation bits, plus 3 destination bits (where to save the computation) and 3 jump bits (go to instruction in the A register if the jump condition is met by the computation):

    `1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3` = `destination = computation; jump`

|![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Computation_bits.png?raw=true)|![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Destination_bits.png?raw=true) |![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Jump_bits.png?raw=true)|
|-|-|-|

Additionally, the followig programs can be used to test the assembler:

+ Programs without symbols: `AddL.asm`, `MaxL.asm`, `RectL.asm`.
+ Programs with symbols: `Add.asm`, `Max.asm`, `Rect.asm` and `Pong.asm`.

## 7 -

In progress...

## 8 -

In progress...

## 9 -

In progress...

## 10 -

In progress...

## 11 -

In progress...

## 12 -

In progress...

## 13 -

In progress...
