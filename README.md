[![Open Source Society University - Computer Science](https://img.shields.io/badge/OSSU-computer--science-blue.svg)](https://github.com/ossu/computer-science)

# From Nand gates to Tetris implementation

This project's goal is to go from a `Nand` gates abstraction, all the way to a fully working computer that is capable os playing Tetris. This project was done in 13 subprojects, each in their respective folder. Since this project is focused on Computer Science, the physical hardware part was hidden behind various abstractions and emulation tools. This project is aimed at dealing with the software-side of the computer (including the theoretical hardware design).

## Testing

<details>
<summary>Open me to see how testing was done!</summary>

### Testing `.hdl` files

Together with the `.hdl` files, there is also a .tst and a .cmp file for each logic gate. They are used to test and compare the functionality of the logic gate, respectively. To test a logic gate, simply:

1. Open the Simulation tools folder and open the `HardwareSimulator.bat` file.
2. Press file > load chip, then select the chip you want to test.
3. Press file > load script, then select the .tst file for the chip you selected.
4. Press run > run, to run the script (you can adjust the speed in the slow-fast dial).

After the script is run, the program will output a .out file that will be compared to the .cmp file. If they are equal, the test will be considered sucessful.

### Testing `.asm` files

Like `.hdl` files, `.asm` files will have a .tst and .cmp file together. However, `.asm` files are test in the CPU emulator:

1. Open the Simulation tools folder and open the `CPUEmulator.bat` file.
2. Press file > load program, then select the program you want to test.
3. Press file > load script, then select the .tst file for the program you selected.
4. Press run > run, to run the script (you can adjust the speed in the slow-fast dial).
5. Press the keyboard icon to link your keyboard to the emulator.

### Testing `.hack` files

`.hack` files are programs that can be used to test the `Computer.hdl` file in subproject 5. They do not have to be directly interacted with, since the .tst file will load the appropriate `.hack` file into the computer's ROM.

### Testing the Hack assembler

To test the conversion of `.asm` files into `.hack` files in subproject 6, use the Assembler program:

1. Open the Simulation tools folder and open the `Assembler.bat` file.
2. Press file > load source file, then select the `.asm` file you want to test.
3. Press file > load comparison file, then select the `.hack` file you got from your assembler.
4. Press run > fast translation, to run the script.

### Testing the `.vm` file's logic

Sometimes it is useful to see what a `.vm` file should do in order to correctly translate it `.asm`. To see a simulation of the program, use the VMEmulator:

1. Open the Simulation tools folder and open the `VMEmulator.bat` file.
2. Press file > load script file, then select the `.VME` file you want to test.
3. Press run > fast translation, to run the script.

### Testing `.jack` files

To test how a Jack file runs:

1. Open the directory a Jack program's folder is in.
2. Drag the folder onto the `JackCompiler.bat` in the tools folder (or to a shortcut, like the one in project 9) to translate it. Note that the translated files will be placed inside the input folder.
3. Test the resulting VM files in the `VMEmulator.bat` by seleting the project folder.

To have better control of problems, consider using the Jack compiler in a CLI. Simply navigate to the Simulation Tools folder and use the compiler as `JackCompiler {FileLocation}` or use the link in the project 9 folder as `JackCompiler.bat.lnk {FileLocation}`.

</details>

## 1 - Elementary logic gates

First we begin by creating some basic elementary logic gates that will be the foundation of the Hack computer (this project's computer architecture). The chips were programmed from an abstraction of the `Nand` gate and the Hardware Description Language (HDL) was used to create the following 15 elementary logic gates:

- `Not` - Inverts the input bit.
- `And` - Outputs 1 if both inputs are 1.
- `Or` - Outputs 1 if either input is 1.
- `Xor` - Outputs 1 if only one input is 1.
- `Mux` - Has two inputs, one selector bit and one output. The selector bit chooses which input to output.
- `DMux` - Has one input, one selector bit and two outputs. The selector bit chooses which output the input will go through. In case it chooses the `a` output, the `b` output will be 0.
- `Not16` - `Not` gate for 16-bit integer.
- `And16` - `And` gate for 16-bit integer.
- `Or16` - `Or` gate for 16-bit integer.
- `Mux16` - `Mux` gate for 16-bit integer.
- `Or8Way` - `Or` gate for 8-bit integer.
- `Mux4Way16` - `Mux` gate for 16-bit integer with 4 inputs instead of 2.
- `Mux8Way16` - `Mux` gate for 16-bit integer with 8 inputs instead of 2.
- `DMux4Way` - `DMux` gate with 4 outputs instead of 2.
- `DMux8Way` - `DMux` gate with 8 outputs instead of 2.

Note that all of these gates were built either from the primitive `Nand` gate or from previously built gates.

## 2 - Arithmetic gates

In this part, logic gates were implemented to create the Hack computer's Arithmetic Logic Unit (ALU):

- `HalfAdder.hdl` - Sums two input bits and outputs the sum and the carry bit.
- `FullAdder.hdl` - Sums two input bits and one carry bit and outputs the sum and the carry bit.
- `Add16.hdl` - Adds two 16-bit integers in Two's complement.
- `Inc16.hdl` - Adds 1 to 16-bit integers.
- `ALU.hdl` - Arithmetic Logic Unit, used to compute various operations, according to the following table:

<p align="center">
  <img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/ALU_truth_table.png?raw=true"/>
</p>

## 3 - Memory chips

In this part, from the abstraction of the Data Flip-Flop gate (DFF), the memory chips of the Hack computer were created:

- `Bit.hdl` - 1-bit Register.
- `Register.hdl` - 16-bit Register.
- `RAM8.hdl` - 16-bit RAM with 8 register of memory.
- `RAM64.hdl` - 16-bit RAM with 64 register of memory.
- `RAM512.hdl` - 16-bit RAM with 512 register of memory.
- `RAM4K.hdl` - 16-bit RAM with 4096 register of memory.
- `RAM16K.hdl` - 16-bit RAM with 16384 register of memory.
- `PC.hdl` - 16-bit program counter.

## 4 - Machine language programs

In this part, two programs that will eventually run on the Hack computer were created, in order to start learning the Hack Assembly language:

- `Mult.asm` - Multiplies `RAM[0]` and `RAM[1]` and stores the result in `RAM[2]`.
- `Fill.asm` - Runs an infinite loop that listens to the keyboard input. When a key is pressed (any key), the program blackens the screen and should remain fully black as long as the key is pressed. When no key is pressed, the program clears the screen. The screen should remain fully clear as long as no key is pressed.

## 5 - Computer architecture

In this part, the Hack computer architecture is finalized through the following chips:

- `Memory.hdl` - Entire RAM address space for the computer (`RAM16K`, Keyboard and Screen).
- `CPU.hdl` - The Hack CPU.
- `Computer.hdl` - The Hack computer platform.

Additionally, the followig programs were used to test the Hack computer:

- `Add.hack` - Adds up the two constants 2 and 3 and writes the result in `RAM[0]`.
- `Max.hack` - Computes the maximum of `RAM[0]` and `RAM[1]` and writes the result in `RAM[2]`.
- `Rect.hack` - Draws a rectangle of width 16 pixels and length `RAM[0]` at the top left of the screen.

## 6 - Hack assembler

In this part, an assembler needed to be built to translate `.asm` files into `.hack` files. All `.hack` instructions are a single 16-bit integer that can be translated according to:

- A-instructions - Used for addressing, where `@value` sets the A register to `value` and consequently, the `RAM[value]` register becomes selected. To translate A-instructions, we use a 0 plus the binary form of `value`.

  `0000000000010101` = `@21`

- C-intructions - Used for calculation. To translate C-instructions, we use a 111, plus a selector bit (to choose between using A or M), plus six computation bits, plus 3 destination bits (where to save the computation) and 3 jump bits (go to instruction in the A register if the jump condition is met by the computation):

  `1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3` = `destination = computation; jump`

| ![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Computation_bits.png?raw=true) | ![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Destination_bits.png?raw=true) | ![ALU truth table](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Jump_bits.png?raw=true) |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |

Additionally, the followig programs were used to test the assembler:

- Programs without labels and symbols: `AddL.asm`, `MaxL.asm`, `RectL.asm`.
- Programs with labels and symbols: `Add.asm`, `Max.asm`, `Rect.asm` and `Pong.asm`.

## 7 - VM Translator (partial)

In this part, a translator needed to be built to translate VM code into Hack assembly. A Python file was create to be operated in a CLI like:

`python VMTranslator.py StackTest\StackTest.vm`.

The `.vm` files are translated into `.asm` files and placed in the same directory. At this stage, the translator was supposed to be able to handle a total of 9 arithmetic and logic operations:

- `add` - Does `x + y`
- `sub` - Does `x - y`.
- `neg` - Does `-y`.
- `eq` - Does `x == y`.
- `or` - Does `x | y`.
- `gt` - Does `x > y`.
- `lt` - Does `x < y`.
- `and` - Does `x & y`.
- `not` - Does `!x`.

With `y` being the top-most element in the VM Stack. Additionally, the translator also need to be ale to translate `push` and `pop` commands to the VM Stack and to 8 distinct memory segments. The mapping for the VM translator is:

- VM Stack or `SP` - Base address in `RAM[0]`. Located between `RAM[256]` and `RAM[2047]`.
- `local` - Base address in `RAM[1]`.
- `argument` - Base address in `RAM[2]`.
- `this` - Base address in `RAM[3]`.
- `that` - Base address in `RAM[4]`.
- `temp` - Located between `RAM[5]` and `RAM[12]`, used for temporary storage.
- General purpose registers - Located between `RAM[13]` and `RAM[15]`.
- `static` - Located between `RAM[16]` and `RAM[255]`. Maps global variables. Each `static i` reference in a `Foo.vm` file is translated to Hack as `@Foo.i`.
- `pointer` - Used for accessing `this` and `that` (`pointer 0` = `this`).
- `constant` - Virtual segment for supplying constant values.

To test this project, the Python translator was used in the `.vm` files to translate them to `.asm`, then the CPU emulator was used to check if it was a correct translation. The tests were done in the following order:

- `SimpleAdd.vm` - Tests `push` and `add`.
- `BasicTest.vm` - Tests the basic virtual memory segments.
- `StackTest.vm` - Tests Stack arithmetic and logic operations.
- `PointerTest.vm` - Tests the `pointer`, `this` and `that` memory segments.
- `StaticTest.vm` - Tests the `static` memory segment.

## 8 - VM Translator (complete)

Part 8 complements the VM translator in part 7 by adding the following functionality:

- Support for `function` and `return` translation.
- Support for function calling using `call`.
- Support for `goto` and `if-goto` commands.
- Directory translation: `python VMTranslator.py NestedCall`, the endfile will be named after the directory and all files in the directory will be translated into this one file.
- Multi-argument translation: `python VMTranslator.py NestedCall StackTest BasicTest\BasicTest.vm`.
- Bootstrap code in case there is a `Sys.vm` file in the directory (Resets Stack top and calls `Sys.init`).

Besides the test available in part 7, part 8 offers 6 more test files for the new features:

- `BasicLoop.vm` - Tests a basic branching scenario using `if-goto`.
- `FibonacciSeries.vm` - Tests a more complex branching scenario using `goto` and `if-goto`.
- `SimpleFunction.vm` - Tests `function` and `return`.
- `NestedCall.vm` - Tests a more complex scenario of the function calling protocol and bootstrap code.
- `FibonacciElement.vm` - Tests function calling, bootstrap code and multi-file directory handling.
- `StaticsTest.vm` - Tests the per-file nature of the Static memory segment.

The biggest challenge of this part was correctly implementing the global Stack changes of the function protocols, which was essentially:

1. `call` - Saves the working Stack of the callee through: Setting `ARG` to be `SP` - function arguments, pushed return address, pushed `LCL`, pushed `ARG`, pushed `THIS`, pushed `THAT`, set `LCL` to be equal to `SP`, used `goto` + the function's name and finally declared the return address used pushed previously.
2. `function` - Declared the label to indicate the start of the function (so that `call` can jump the the start of the function) and pushed as many zeros as there were function arguments.
3. `return` - Saved the return value of the function in `RAM[ARG]`, set `SP` to `ARG` + 1, restored the `LCL`, `ARG`, `THIS` and `THAT` memory segments and used `goto` to go to the return address defined when the function was called.

Additionally, there were 4 special symbols that needed to be properly translated:

1. `fileName.i` - Used for each static variable `i` from a given file `fileName.vm`. Each time a new static variable in that file is found, `i` is incremented by 1.
2. `fileName.functionName$label` - Used to translate `goto label` and `if-goto label` used inside of a function `funtionName` and file `fileName.vm`.
3. `functionName.fileName` - Used to translate a function `functionName`'s label when inside file `fileName.vm`.
4. `functionName$ret.i` - Used to translate the return address for `call functionName` when used inside of a file `fileName.vm`. Each time a function is called, the variable `i` is incremented by 1 (made for unique return addresses).

## 9 - Jack program

Part 9 intoduces the Jack language, a simple Java-like OOP language. The goal of this part is to get used to the language before implementing a Jack compiler in parts 10 and 11. To do that, a creative and well designed Jack program must me made. To create the program, the following features were used:

- A bitmap editor - The `BitmapEditor.html` file is a useful tool to quickly convert sprite bitmaps into Jack code.
- The Jack language's OS - Offers a few built in functions to facilitite the coding process:
  |![Jack OS API](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Jack_OS_API_1.png?raw=true)|![Jack OS API](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Jack_OS_API_2.png?raw=true)|![Jack OS API](https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Jack_OS_API_3.png?raw=true)|
  |-|-|-|

The theme for this project was a simple restaurant. The challenges of this project included:

1. Learning a new programming language.
2. Correctly manipulating screen elements with the primitive libraries available to the language.
3. Handling the overall lack of high-level features that programmers are often used to.
4. Optimizing low-level graphics.
5. Developing interactive applications.

Here is a picture of how the game turned out:

<p align="center">
  <img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/RokoboKitchenPreview.png?raw=true"/>
</p>

## 10 - Jack Analyzer

Part 10 is the first of two parts of a Jack to VM compiler. In this part, the program `JackTokenizer.py` translates Jack code into a XML parse tree. Challenges for this project included:

1. Tokenizing a Jack file.
2. Understanding the Jack grammar rules.
3. Identifying language constructs.
4. Parsing language constructs to a XML parse tree.

The way the translator worked was by enclosing terminal tokens in one of 5 categories and those categories inside other non-terminal tokens (the top-most token being `<class>`). Here are the grammar rules for the Jack language:

  |<img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Lexical_elements.png?raw=true"/>|<img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Program_structure.png?raw=true"/>|
  |-|-|

  |<img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Statements.png?raw=true"/>|<img src="https://github.com/rokobo/From-Nand-gates-to-Tetris-implementation/blob/main/images/Expressions.png?raw=true"/>|
  |-|-|

The files in project 10 were design to test the Tokenizer. Files like `Main.jack` are the files that will be translated, `Main.xml` are the translated files, `MainT.xml` are the files that have no non-terminal tags or indentation and `MainO.xml` are what the translated files are supposed to look like.

## 11 - Jack Compiler

Part 11 is the second of two parts of a Jack to VM compiler. In this part, the program `JackCompiler.py` was built by modifying the `JackAnalyzer.py` program from part 10, making Jack files compile directly to VM code. Challenges for this project included:

1. Compiling procedural code.
2. Compiling the construction and manipulation of arrays and objects.
3. Code generation techniques.
4. Recursive compilation engine.
5. Symbol tables.
6. Memory management.

The files in project 11 were designed to test different functionalities of the compiler:

1. `Seven` → Arithmetic expressions with constants only, `do` statement and `return` statement.
2. `ConvertToBin` → Expressions (no arrays or method calls) and procedural constructs (`if`, `while`, `do`, `let`, `return`).
3. `Square` → Constructors, methods and expressions that include method calls.
4. `Average` → Arrays and strings.
5. `Pong` → Object handling and static variables.
6. `ComplexArrays` → Array manipulation with index expressions and other complex array references.

## 12 - Jack OS

Part 12 was comprised of 8 Jack classes that make up the Jack OS:

1. `Array` → Provides support for `Arrays`.
2. `Keyboard` → Handles user input.
3. `Math` → Implements useful mathematical operations.
4. `Memory` → Provides `RAM` access functionality, as well as memory allocation for objects.
5. `Output` → Enables writing text on the screen.
6. `Screen` → Enables drawing graphics on the screen.
7. `String` → Provides support for `Strings`.
8. `Sys` → Implements program execution services.

Challenges for this project include:

1. Running-time analysis and optimization.
2. Resource allocation and deallocation.
3. Heap management.
4. Input handling.
5. Vector graphics, fonts and textual outputs.
6. Type conversions and string processing.
7. Booting process and OS implementation issues.

Noteworthy sections of this project include:

1. `multiply()` and `divide()` in `Math.jack`.
2. `drawLine()` in `Screen.jack`.
3. `alloc()` in `Memory.jack`.
