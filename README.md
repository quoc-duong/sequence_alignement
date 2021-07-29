# Bio-Info Project

The goal of this project is to be able to efficiently search for subsequences in a genome by following the bowtie tool strategy.
It consists in computing an index of the reference sequence using the Burrow-Wheeler (BW) transform and then using an efficient search procedure on the transformed sequence.

## Usage

Using a Python interpreter:

### bw-build

bw-build.py [-h] [--compress] [--progressive k] infile outfile f

#### Example :

```
python3 src/bw-build.py cmv.fasta cmv.fasta.idxc 5 --compress
```

### bw-search

bw-search.py [-h] [--count-only] infile q

#### Example:

```
python3 src/bw-search.py --count-only data/cmv.fasta.idx ATT
```

## AUTHOR

quoc-duong.nguyen
