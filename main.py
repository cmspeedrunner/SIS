import os
import sys
class sis:
    def __init__(self):
        
        self.registers = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        self.stack = []
        self.program_counter = 0
        self.instructions = []

    def load_program(self, program):
        
        self.instructions = self.parse_instructions(program)

    def parse_instructions(self, program):
        lines = [line.strip() for line in program.strip().split('\n') if line.strip()]

        instructions = []

        for line in lines:
            parts = line.split(maxsplit=1)
            operation = parts[0]
            args = parts[1].split(', ') if len(parts) > 1 else []

            instructions.append({'operation': operation, 'args': args})

        return instructions

    def execute(self):
        while self.program_counter < len(self.instructions):
            instruction = self.instructions[self.program_counter]
            self.execute_instruction(instruction)
            self.program_counter += 1

    def execute_instruction(self, instruction):
        operation_map = {
            'hlt': self.halt,
            'push': self.push,
            'add': self.add,
            'sub': self.sub,
            'mul': self.mul,
            'div': self.div,
            'mov': self.move,
            'set': self.set_register,
            'dump': self.dump,
            'ld': self.load,
            'pt': self.push_to_register,
            '//': self.comment
        }
        operation = instruction['operation']
        if operation in operation_map:
            operation_map[operation](instruction['args'])
        else:
            self.handle_invalid_instruction(operation)
    def comment(self, args):
        
        pass


    def halt(self, args):
        
        self.program_counter = len(self.instructions)

    def push(self, args):
        
        value = args[0]
        if str(value).startswith("\""):
            self.stack.append(self.convert_value('str', str(value).replace("\"", "")))
        elif "." in str(value):
            self.stack.append(self.convert_value('flt', value))
        else:
            self.stack.append(self.convert_value('int', value))


    def add(self, args):
        
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def sub(self, args):
        
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def mul(self, args):
        
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def div(self, args):
        
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a / b)

    def move(self, args):
        
        dest, src = args
        self.registers[dest] = self.registers[src]

    def set_register(self, args):
        
        reg, val = args
        if str(val).startswith("\""):
            self.registers[reg] = self.convert_value('str', str(val).replace("\"", ""))
        elif "." in str(val):
            self.registers[reg] = self.convert_value('flt', val)
        else:
            self.registers[reg] = self.convert_value('int', val)
        

    def dump(self, args):
        
        if self.stack:
            print(self.stack[-1])
        else:
            print("Stack is empty")

    def load(self, args):
        
        reg = args[0]
        self.stack.append(self.registers[reg])

    def push_to_register(self, args):
        
        reg = args[0]
        if self.stack:
            self.registers[reg] = self.stack.pop()

    def handle_invalid_instruction(self, operation):
        
        print(f"Invalid instruction: {operation}")

    def convert_value(self, var_type, value):
        if var_type == 'int':
            return int(value)
        elif var_type == 'flt':
            return float(value)
        elif var_type == 'str':
            return str(value)
        else:
            raise ValueError(f"Unknown type: {var_type}")

sis = sis()
sisfile = sys.argv[1]
with open(sisfile, "r") as f:
    program = f.read()
    f.close()
sis.load_program(program)
sis.execute()
