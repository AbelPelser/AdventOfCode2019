import sys
from typing import Callable, Dict, List
from types import FunctionType


class Program:
    def __init__(self, memory: List[int], noun: int = None, verb: int = None):
        self.memory: List[int] = memory
        self.instruction_pointer: int = 0
        if noun:
            self.memory[1] = noun
        if verb:
            self.memory[2] = verb
        self.stop: bool = False

    def add(self, param1: int, param2: int, param3: int) -> None:
        self.memory[param3] = self.memory[param1] + self.memory[param2]

    def multiply(self, param1: int, param2: int, param3: int) -> None:
        self.memory[param3] = self.memory[param1] * self.memory[param2]

    def input_int(self, param1: int) -> None:
        input_int = int(input('Please enter an int'))
        self.memory[param1] = input_int

    def output_int(self, param1: int) -> None:
        print(self.memory[param1])

    def quit(self) -> None:
        self.stop = True

    def handle_opcode(self, opcode):
        opcode_map = {
            1: self.add,
            2: self.multiply,
            3: self.input_int,
            4: self.output_int,
            99: self.quit
        }
        opcode_str = str(opcode)
        func_code = int(opcode_str[-2:])
        func = opcode_map[func_code]
        nargs = func.func_code.co_argcount - 1

        param_modes = [0] * nargs
        for i in range(len(opcode_str) - 2):
            param_modes[i] = int(opcode_str[-2 - i])
        param_modes = [0] * nargs

        args = [self.memory[self.instruction_pointer + i + 1] for i in range(nargs)]
        func(*args)
        self.instruction_pointer += nargs + 1

    def run(self):
        opcode_map = {
            1: self.add,
            2: self.multiply,
            3: self.input_int,
            4: self.output_int,
            99: self.quit
        }
        while not self.stop:
            opcode = self.memory[self.instruction_pointer]
            if opcode in opcode_map.keys():
                self.handle_opcode(opcode)
            else:
                print('Bad OPcode ' + str(opcode))
                sys.exit(0)
        return self.memory[0]


class ProgramRunner:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        for noun in range(100):
            for verb in range(100):
                output = Program(self.memory[:], noun=noun, verb=verb).run()
                break


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        numbers = list(map(lambda s: int(s), filter(None, f.read().split(','))))
    print(ProgramRunner(numbers).run())
