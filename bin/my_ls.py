""" Lists the files in a given directory with a given suffix. """
import argparse
import glob

def main(args):
    """Run the program"""
    direc = args.dir
    suff = args.suffix
    listoffiles = glob.glob(args.dir+"*."+args.suffix)
    listoffiles.sort()
    for i in range(len(listoffiles)):
        print(listoffiles[i])
        
if __name__ == '__main__':
    USAGE = 'Lists the files in a given directory with a given suffix.'
    parser = argparse.ArgumentParser(description=USAGE)
    parser.add_argument('dir', type=str,
    help='Directory (e.g. data/ or zipf/data/)')
    parser.add_argument('suffix', type=str,
    help='File suffix (e.g. py, sh)')
    args = parser.parse_args()
    main(args)
