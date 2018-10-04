# Utils Fn


import sys

# Clean StdOut Line
def clean_line():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line


def print_line():
    str = ''
    for i in range(30):
        str += '*'
    print(str)
