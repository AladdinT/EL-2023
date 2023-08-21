import sys

def main():
    # Get the list of command-line arguments
    arguments = sys.argv

    # The first argument (index 0) is the script name itself
    script_name = arguments[0]

    # The remaining arguments are the command-line arguments
    command_line_arguments = arguments[1:]

    print("Script name:", script_name)
    print("Command-line arguments:", command_line_arguments)

if __name__ == "__main__":
    main()


#################################### Moatasem
def test(*ls):
    ln = len(ls)
    for i in range(0, ln):
        print(ls[i], end=" ")
    print("")


test("moatasem", "Essam")
test("moatasem", "Essam", "Zein")
test("moatasem", "Essam", "Zein", "mona")


def test2(**args):
    print(f"length of args {len(args)}")
    ls = []
    for i in args.keys():
        ls.append(i)
        print(args[i])
    # print(ls[0])
    for i in ls:
        print(args[i])


test2(first="red", second="yellow")
test2(first="red", second="yellow", third="green")

