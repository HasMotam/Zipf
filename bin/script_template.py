""" Brief description of what the script does. """
import argparse

def main(args):
    """Run the program"""
    print('Input file:', args.infile)
    print('Outputfile:', args.outfile)


if __name__ == '__main__':
    USAGE = 'Brief descriptionofwhatthescriptdoes.'
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('infile', type=str,
    help='Input filename')
    parser.add_argument('outfile', type=str,
    help='Output filename')
    args = parser.parse_args()
    main(args)
