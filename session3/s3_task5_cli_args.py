import sys

# Get the list of command-line arguments
arguments = sys.argv
print(arguments)

# The first argument (index 0) is the script name itself
script_name = arguments[0]
# The remaining arguments are the command-line arguments
command_line_arguments = arguments[1:]

print("Script name:", script_name)
print("Command-line arguments:", command_line_arguments)


print('####################### Another Solution ####################')

import argparse 

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    args = parser.parse_args()

    return args

## Argument parsing ##
args = get_args()

cap_device = args.device
cap_width = args.width
cap_height = args.height
