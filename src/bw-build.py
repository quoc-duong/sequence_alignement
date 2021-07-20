import argparse
import numpy as np
from numpy.core.fromnumeric import sort

def get_all_rotations(s):
    return [s[i:] + s[:i] for i in range(len(s))]

def parse_options():
    parser = argparse.ArgumentParser(description='Search subsequence in a genome following the strategy of the bowtie tool')
    parser.add_argument("infile", help="Input file containing the sequence to process")
    parser.add_argument("outfile", help="Output file")
    parser.add_argument("f", help="index creation frequence", type=int)
    parser.add_argument("--compress", dest='compress', help="Compress option", action='store_true')
    return parser.parse_args()

def create_output(args, bw_transform_str, positions_index):
    outfile = open(args.outfile, 'w')

    c = 1 if args.compress else 0
    n = bw_transform_str.index('$') if args.compress else 0
    p = 0 if args.compress else 0
    f = args.f

    outfile.write("{} {} {} {}\n".format(c, n, p, f))
    outfile.write("{}\n".format(positions_index))
    outfile.write(bw_transform_str)
    outfile.close()

def get_positions_index(sorted_list, frequency):
    res = [str(len(sorted_list) - sorted_list[i].index('$') - 1) for i in range(0, len(sorted_list), frequency)]
    return ','.join(res)

def bw_build():
    args = parse_options()

    f = open(args.infile, "r")
    lines = f.readlines()[1:]
    f.close()

    sequence = "".join(lines).replace('\n', '') + '$'

    all_rotations_sorted = sorted(get_all_rotations(sequence))

    positions_index = get_positions_index(all_rotations_sorted, args.f)

    last_col_str = [rotation[-1:] for rotation in all_rotations_sorted]

    bw_transform_str = "".join(last_col_str)

    create_output(args, bw_transform_str, positions_index)

if __name__ == "__main__":
    bw_build()
