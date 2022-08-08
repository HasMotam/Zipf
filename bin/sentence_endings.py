""" Counts the occurence of full stops, question marks and exclamation marks. """

import string
from collections import Counter
import sys
import csv
import argparse

def count_punctuation(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    num_exclamation = 0
    num_fullstop = 0
    num_questionmark = 0
    for word in chunks:
        num_exclamation += word.count('!')
        num_fullstop += word.count('.')
        num_questionmark += word.count('?')
    return num_fullstop,num_questionmark,num_exclamation


    
def main(args):
    """Run the command line program."""
    punc_counts = count_punctuation(args.infile)
    
    print("Number of . is ", punc_counts[0])
    print("Number of ? is ", punc_counts[1])
    print("Number of ! is ", punc_counts[2])
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),nargs='?', 
    default = '-', help='Input file name')
    args = parser.parse_args()
    main(args)

