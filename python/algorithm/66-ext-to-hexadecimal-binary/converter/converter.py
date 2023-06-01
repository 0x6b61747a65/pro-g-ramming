import argparse


parser = argparse.ArgumentParser(
    description="CLI tool for converting from text to hexadecimal or binary")
parser.add_argument(
    "-b", "--binary", help="Convert text to binary.", action="store_true")
parser.add_argument(
    "-f", "--file", help="Get text from textfile.", metavar="FILENAME")
parser.add_argument(
    "-o", "--output", help="Output result into file.", metavar="FILENAME")
parser.add_argument(
    "-s", "--string", help="Get text from provided string. In quotes.", metavar="\"STRING OF TEXT\"")
parser.add_argument("-x", "--hexadecimal",
                    help="Convert text to hexadecimal.", action="store_true")


args = parser.parse_args()
