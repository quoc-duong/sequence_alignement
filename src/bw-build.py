import argparse

def parse_options():
    parser = argparse.ArgumentParser(description='Search subsequence in a genome following the strategy of the bowtie tool')
    parser.add_argument("infile", help="Input file containing the sequence to process", action='store_true')
    parser.add_argument("outfile", help="Output file", action='store_true')
    parser.add_argument("f", help="index creation frequence", action='store_true')
    parser.add_argument("--compress", dest='compress', help="Compress option", action='store_true')
    return parser.parse_args()

def bw_build():
    args = parse_options()
    print("Hello there !")

if __name__ == "__main__":
    bw_build()