"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # memory
        self.ram = [0] * 256
        # register
        self.reg = [0] * 8

        # internal registers:
        # program counter
        self.pc = 0
        # flags

    def load(self):
        """Load a program into memory."""
        # check for filename arg
        if len(sys.argv) != 2:
            print("ERROR: must have file name")
            sys.exit(1)

        address = 0

        try:
            with open(sys.argv[1]) as f:
                # read all the lines
                for line in f:
                    # parse out comments
                    comment_split = line.strip().split("#")

                    value = comment_split[0].strip()

                    # ignore blank lines
                    if value == "":
                        continue

                    # cast the numbers from strings to ints
                    num = int(value, 2)

                    self.ram[address] = num
                    address += 1

        except FileNotFoundError:
            print("File not found")
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            # instruction Register
            ir = self.pc
            # read command
            op = self.ram_read(ir)
            # read operands
            operand_a = self.ram_read(ir + 1)
            operand_b = self.ram_read(ir + 2)

            # execute command
            if op == HLT:
                # halt program
                break
            elif op == LDI:
                # set value of register to an int
                self.reg[operand_a] = operand_b
            elif op = PRN:
                # print value stored in given register
                print(self.reg[operand_a])
            else:
                print(f"Command not found: {bin(op)}")

            # check if command sets pc
            # if not, update pc
            if op & 16 == 0:
                num_operands = 0
                if op & 64 != 0:
                    num_operands += 1
                elif op & 128 != 0:
                    num_operands += 2
                self.pc += num_operands + 1


    def ram_read(self, mar):
        # return value stored at address
        mdr = self.ram[mar] # mdr - Memory Data Register
        return mdr

    def ram_write(self, mar, mdr):
        # write value to address
        self.ram[mar] = mdr
