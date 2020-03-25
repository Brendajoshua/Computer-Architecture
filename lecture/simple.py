import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4  # save a value to a register
PRINT_REGISTER = 5  # print the value in a register
ADD = 6  # add 2 registers, store the result in 1st reg

memory = [0] * 256

def load_memory(filename):
    try:
        address = 0
        with open(sys.argv[1]) as f:
            # read all the lines
            for line in f:
                # parse out comments
                comment_split = line.strip().split("#")

                # cast the numbers from strings to ints
                value = comment_split[0].strip()

                # ignore blank lines
                if value == "":
                    continue

                num = int(value)
                memory[address] = num
                address += 1


    except FileNotFoundError:
        print("File not found")
        sys.exit(2)

register = [0] * 8

# program counter
pc = 0

if len(sys.argv) != 2:
    print("ERROR: must have file name")
    sys.exit(1)

load_memory(sys.argv[1])


# processor
while True:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
    elif command == HALT:
        sys.exit(0)
    else:
        print(f"I did not understand that command: {command}")
        sys.exit(1)