import argparse
import random

def get_all_rotations(s):
    return [s[i:] + s[:i] for i in range(len(s))]

def parse_options():
    parser = argparse.ArgumentParser(description='Search subsequence in a genome following the strategy of the bowtie tool')
    parser.add_argument("infile", help="Input file containing the sequence to process")
    parser.add_argument("outfile", help="Output file")
    parser.add_argument("f", help="Index creation frequence", type=int)
    parser.add_argument("--compress", dest='compress', help="Compress bwt", action='store_true')
    parser.add_argument("--progressive", help="Construire l’index basé sur k graines", type=int, metavar='k')
    return parser.parse_args()

def create_output(args, bw_transform_str, positions_index):
    if (args.compress):
        ATGC_dict = {
            'A': 0b00,
            'C': 0b01,
            'G': 0b10,
            'T': 0b11
        }

        dollar_position = bw_transform_str.index('$')
        bw_transform_str = bw_transform_str.replace('$', '')

        A_number = (4 - (len(bw_transform_str) % 4)) % 4
        bw_transform_str += A_number * 'A'

        compressed_bw_transform_str = []
        for i in range(0, len(bw_transform_str), 4):
            byte = ATGC_dict[bw_transform_str[i + 3]]
            for j in range(2, -1, -1):
                byte = byte << 2
                byte += ATGC_dict[bw_transform_str[i + j]]
            compressed_bw_transform_str.append(byte)

    c = 1 if args.compress else 0
    n = dollar_position if args.compress else 0
    p = A_number if args.compress else 0
    f = args.f

    with open(args.outfile, 'w') as outfile:
        outfile.write("{} {} {} {}\n".format(c, n, p, f))
        outfile.write("{}\n".format(positions_index))
        if (not args.compress):
            outfile.write(bw_transform_str)

    if (args.compress):
        with open(args.outfile, "ab") as outfile:
            outfile.write(bytearray(compressed_bw_transform_str))

def get_positions_index(sorted_list, frequency):
    res = [str(len(sorted_list) - sorted_list[i].index('$') - 1) for i in range(0, len(sorted_list), frequency)]
    return ','.join(res)

def bw_build():
    args = parse_options()

    with open(args.infile, "r") as f:
        lines = f.readlines()[1:]

    sequence = "".join(lines).replace('\n', '') + '$'

    if args.progressive:
        # Initialize variables
        bw_transform_str = ""
        current_f_count = 0
        positions_index = []

        sample_indexes = random.sample(range(len(sequence)), args.progressive)
        splitters = sorted(sequence[i:] + sequence[:i] for i in sample_indexes)

        min_char = chr(0)
        max_char = chr(255)

        splitters.insert(0, min_char)
        splitters.append(max_char)

        for i in range(len(splitters) - 1):
            bucket = []

            # Create bucket between 2 splitters
            for j in range(len(sequence)):
                rotation = sequence[j:] + sequence[:j]

                if splitters[i] <= rotation < splitters[i + 1]:
                    bucket.append(rotation)

            bucket = sorted(bucket)

            last_col_str = [rotation[-1:] for rotation in bucket]

            bw_transform_str += ''.join(last_col_str)

            # Get position indexes
            for j in range(len(bucket)):
                if current_f_count == 0:
                    positions_index.append(str(len(sequence) - bucket[j].index('$') - 1))

                current_f_count = (current_f_count + 1) % args.f
        positions_index = ','.join(positions_index)

    else:
        all_rotations_sorted = sorted(get_all_rotations(sequence))

        positions_index = get_positions_index(all_rotations_sorted, args.f)

        last_col_str = [rotation[-1:] for rotation in all_rotations_sorted]

        bw_transform_str = "".join(last_col_str)

    create_output(args, bw_transform_str, positions_index)

if __name__ == "__main__":
    bw_build()
