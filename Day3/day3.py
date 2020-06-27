import sys


class Program:
    def __init__(self, memory, noun=None, verb=None):
        self.memory = memory
        self.instruction_pointer = 0
        if noun:
            self.memory[1] = noun
        if verb:
            self.memory[2] = verb
        self.stop = False

    def add(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] + self.memory[param2]

    def multiply(self, param1, param2, param3):
        self.memory[param3] = self.memory[param1] * self.memory[param2]

    def quit(self):
        self.stop = True

    def handle_opcode(self, f):
        nargs = f.func_code.co_argcount - 1  # -self
        args = [self.memory[self.instruction_pointer + i + 1] for i in range(nargs)]
        f(*args)
        self.instruction_pointer += nargs + 1
    
    def run(self):
        opcode_map = {
            1: self.add,
            2: self.multiply,
            99: self.quit
        }
        while not self.stop:
            opcode = self.memory[self.instruction_pointer]
            if opcode in opcode_map.keys():
                self.handle_opcode(opcode_map[opcode])
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
                if output == 19690720:
                    return noun * 100 + verb


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        numbers = list(map(lambda s: int(s), filter(None, f.read().split(','))))
    print(ProgramRunner(numbers).run())