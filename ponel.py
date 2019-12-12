import sys
import PONELParser as parser


print("Welcome to PONEL")
print("(pre-alpha) ver. 1.0.0")
print("")

while True:
    try:
        s = input('PONEL >>')
    except EOFError:
        break
    print("")
    parser.do_parse(s)
    print("")
