import argparse

def parse_options():
    parser = argparse.ArgumentParser(description='Search subsequence in a genome following the strategy of the bowtie tool')
    parser.add_argument("infile", help="Input file that is generated by bw-build")
    parser.add_argument("q", help="Sequence to process")
    parser.add_argument("--count-only", dest='count-only', help="Only print the number of matches", action='store_true')
    return parser.parse_args()

def bw_search():
    args = parse_options()

    with open(args.infile, "r") as f:
        lines = f.readlines()[2:]

    P = "".join(lines)
    p = len(p)
    c, i = P[p], p
    sp = 

if __name__ == "__main__":
    bw_search()