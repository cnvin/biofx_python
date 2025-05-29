# -*- coding: utf-8 -*-
"""Tetranucleotide frequency analysis.
This script calculates the frequency of each tetranucleotide in a given DNA sequence.
It reads a DNA sequence from a file, counts the occurrences of each tetranucleotide,
and prints the results in a sorted order.
"""
import argparse

#--------------------------------------------
#get the arguments
def get_args():
    """Get command line arguments."""
    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency analysis",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("file", metavar="FILE", help="Input file containing DNA sequence")
    return parser.parse_args()

#--------------------------------------------
# read the file and return the sequence
def read_file(file: str) -> str:
    """Read the file and return the sequence."""
    try:
        with open(file, "r") as f:
            sequence = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found at {file}")
        exit(1) # Exit the program if the file is not found

    # Remove any whitespace or newline characters
    sequence = sequence.replace(" ", "").replace("\n", "")
    # Convert to uppercase to handle case insensitivity
    sequence = sequence.upper()

    # Basic validation for DNA characters
    valid_chars = set("ACGT")
    if not all(char in valid_chars for char in sequence):
        print("Warning: Input sequence contains non-DNA characters.")
        # You might choose to remove invalid characters or handle differently
        sequence = "".join(char for char in sequence if char in valid_chars)
        print("Non-DNA characters removed.")

    return sequence
#--------------------------------------------
# count the tetranucleotides
def count_tetranucleotides(sequence):
    """Count the tetranucleotides in the sequence."""
    tetranucleotide_counts = {}
    for i in range(len(sequence) - 3):
        tetranucleotide = sequence[i:i + 4]
        if tetranucleotide in tetranucleotide_counts:
            tetranucleotide_counts[tetranucleotide] += 1
        else:
            tetranucleotide_counts[tetranucleotide] = 1
    return tetranucleotide_counts
#--------------------------------------------
# print the tetranucleotide counts
def print_tetranucleotide_counts(tetranucleotide_counts):
    """Print the tetranucleotide counts in sorted order."""
    for tetranucleotide in sorted(tetranucleotide_counts):
        print(f"{tetranucleotide}: {tetranucleotide_counts[tetranucleotide]}")
#--------------------------------------------
def main():
    """Main function to execute the tetranucleotide frequency analysis."""
    sequence = read_file(get_args().file)
    tetranucleotide_counts = count_tetranucleotides(sequence)
    print_tetranucleotide_counts(tetranucleotide_counts)
#--------------------------------------------
if __name__ == "__main__":
    main()
#--------------------------------------------
# This code is a solution to the tetranucleotide frequency analysis problem.
# It reads a DNA sequence from a file, counts the occurrences of each tetranucleotide,
# and prints the results in a sorted order.