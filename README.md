# SIS

## Overview


SIS (Simple Instruction Set) is a custom bytecode interpreter that operates on a register-based system with a stack. It processes textual instructions from a .sis file and executes them sequentially. The system has four general-purpose registers (A, B, C, D) and a stack for temporary data storage. The SIS interpreter reads the instructions, parses them, and executes each operation accordingly.

## Execution Model
<ul>
  <li>The program counter starts at 0 and increments after each instruction execution.</li>
  <li>The interpreter maintains a stack (self.stack) and register set (self.registers).</li>
  <li>Instructions are parsed into an operation and arguments.</li>
  <li>Unrecognized instructions result in an error message.</li>
</ul> <br>
SIS contains four general-purpose registers:<br>

***A***, ***B***, ***C***, ***D*** <br>
Each can store an integer, float, or string. <br>

# Instruction Set

The following opcodes are supported by SIS:

### `set <register>, <value>`
Sets a register to a specified value.
- Accepts integer, float, or string values.
- **Example:** `set A, 20` (sets register A to 20)

### `mov <destination>, <source>`
Copies the value from one register to another.
- **Example:** `mov B, A` (sets B to the value of A)

### `ld <register>`
Pushes the value of a register onto the stack.
- **Example:** `ld A` (pushes the value in A onto the stack)

### `pt <register>`
Pops the top value from the stack and stores it in the specified register.
- **Example:** `pt C` (pops the top of the stack into C)

### `push <value>`
Pushes an immediate value onto the stack.
- Strings must be enclosed in double quotes (`"text"`).
- Floats are recognized by the presence of a decimal point (`.`).
- Integers are assumed by default.
- **Example:** `push "hello"` (pushes the string `"hello"` onto the stack)

### `add`
Pops the top two values from the stack, adds them, and pushes the result back onto the stack.
- **Example stack state:**
  - Before: `[2, 3]`
  - After `add`: `[5]`

### `sub`
Pops the top two values from the stack, subtracts the second value from the first, and pushes the result.
- **Example stack state:**
  - Before: `[7, 4]`
  - After `sub`: `[3]`

### `mul`
Pops the top two values from the stack, multiplies them, and pushes the result.
- **Example stack state:**
  - Before: `[3, 5]`
  - After `mul`: `[15]`

### `div`
Pops the top two values from the stack, divides the first by the second, and pushes the result.
- **Example stack state:**
  - Before: `[10, 2]`
  - After `div`: `[5]`

### `dump`
Prints the top value of the stack without modifying it.
- **Example output:**
  - Stack: `[42]`
  - Output: `42`
- If the stack is empty, it prints `Stack is empty`.

### `hlt`
Halts execution immediately.
- **Example:** `hlt` (stops the program)

### `// <comment>`
A comment line that is ignored by the interpreter. (Must be on its own line soz)
- **Example:** `// This is a comment`

# Usage:
To run your file, simply do: <br>
`py main.py yourfile.sis` <br>
And it should start at once!
## Check out
`/Examples` has some more in depth detailed programs, and as with all my projects, this was for fun, its a basic from scratch bytecode interpreter and I do not think this is anything more then a fun project I hope others can enjoy!<br>
Thank you!
