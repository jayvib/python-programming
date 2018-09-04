"""
split and interactively page a string or file of text
"""

def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunks = lines[:numlines]
        lines = lines[numlines:]
        for line in chunks:
            print(line)
        if lines and input("more?") not in ["y", "Y"]:
            break 

if __name__ == "__main__":
    import sys
    more(open(sys.argv[1]).read(), 10)
