#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} ".format(len(sys.argv) - 1), end="")
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("argument:")
        elif len(sys.argv) > 2:
            print("arguments:")
        for i in range(len(sys.argv) - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
    elif len(sys.argv) == 1:
        print("arguments.")
