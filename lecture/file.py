import sys

# take an argument
# load the values from that file and put it in an array

print(sys.argv)

# open the file
if len(sys.argv) != 2:
    print("ERROR: must have file name")
    sys.exit(1)

try:
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

            print(value)
            num = int(value)
            memory[mem_pointer] = num
            mem_pointer += 1

            print(f"{num:08b}: {num}")

except FileNotFoundError:
    print("File not found")
    sys.exit(2)

# populate a memory array 