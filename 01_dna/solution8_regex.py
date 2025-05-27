#!/usr/bin/env python3
""" Tetranucleotide frequency using re.findall() """

import argparse
import os
import re
from typing import NamedTuple, Tuple  # Removed List (fixed E261)


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency using re.findall()',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(  # Reformatted for line length (fixed E261)
        'dna',
        metavar='DNA',
        help='Input DNA sequence or path to a file containing DNA sequence'
    )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        with open(args.dna, 'r', encoding='utf-8') as dna_file:
            args.dna = dna_file.read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def count_bases_regex(dna_sequence: str) -> Tuple[int, int, int, int]:
    """
    Counts the occurrences of each DNA base (A, C, G, T) in a sequence
    using re.findall().
    """
    count_a = len(re.findall('A', dna_sequence))
    count_c = len(re.findall('C', dna_sequence))
    count_g = len(re.findall('G', dna_sequence))
    count_t = len(re.findall('T', dna_sequence))
    return count_a, count_c, count_g, count_t


# --------------------------------------------------
def main() -> None:
    """ Main function to parse args and print counts """

    args = get_args()
    count_a, count_c, count_g, count_t = count_bases_regex(args.dna)
    print(f'{count_a} {count_c} {count_g} {count_t}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
