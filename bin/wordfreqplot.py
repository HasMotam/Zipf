import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),nargs='?',default
    = '-', help='Input file name')
    parser.add_argument('--outfile',
    type=str, default="plotcounts.png",
    help='storage location and type of the plot in the form of a a string e.g. "results/myplot.png" ')
    parser.add_argument('--xlim',
    type=tuple, default = None,
    help='x-axis limits in the form of a tuple e.g. (0,500)')
    args = parser.parse_args()
    
    df = pd.read_csv(args.infile, header=None,
    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
    method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
    y='rank',loglog=True,
    figsize=[12, 6],
    grid=True,xlim=args.xlim)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)

