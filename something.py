"""
Usage:
    something --help
    something --version
    something name [--first | --last | --full]

Options:
  -h --help        Show this info.
  -v --version     Show version.
  name <type>      Name type [default:  --full].
"""

VERSION = "version 0.1.0"

from docopt import docopt
from src.somenames import generateName, NameType


def main(args):
    if args["--version"]:
        print(VERSION)
        return

    if args["name"]:
        if args["--first"]:
            print(generateName(NameType.FIRST))
        elif args["--last"]:
            print(generateName(NameType.LAST))
        else:
            print(generateName(NameType.FULL))


if __name__ == "__main__":
    main(docopt(__doc__))
