"""
program for generating coinflips with the results printed

for help:
    -h, --help

optimization:
    using random.randint(0,1) to generate 0's and 1's
    representing heads or tails is much slower  than equal
    or greater than evaluation of random.random() floats
"""
import argparse
import random


# cmd line arguments
parser = argparse.ArgumentParser(
    description='FliPy: a coinflip simulation tool, coded in Python'
)
parser.add_argument(
    '--coinflips', '-n',
    type=int,
    default=1,
    dest='num',
    help='Accepts an integer and executes that many coinflips.'
)

options = parser.parse_args()


def coinflip(num):
    """
    Generate coinflips, print human-readable results as a table.
    Original function for generating flips.
    """
    heads = 0
    tails = 0
    for n in xrange(0, num):
        result = random.randint(0, 1)
        if result is 0:
            heads += 1
        else:
            tails += 1
    pctheads = float(heads)/num * 100
    pcttails = float(tails)/num * 100
    print '''
          coinflips: %i
        
              heads: %i  %f%%
        
              tails: %i  %f%% 
          ''' % (num,
                 heads, pctheads,
                 tails, pcttails)

def coinopt(num):
    """
    coinflip optimization
    """
    heads = 0
    tails = 0
    for n in xrange(0, num):
        result = random.random()
        if result <= .50:
            heads += 1
        else:
            tails += 1
    result_list = [['coinflips',num], ['heads', heads], ['tails', tails]]
    print_tab(result_list)

def print_tab(result_list):
    """
    data presentation structure:
    [[type,total],[sub,total],[sub,total],...]
    """
    count = result_list[0][1]
    print 'FliPY results:'
    print '    %s: %i' % (result_list[0][0], count)

    for item in result_list[1:]:
        pct = float(item[1])/count * 100
        print '        %s: %i %f%%' % (item[0], item[1], pct)


if __name__ == '__main__':
    #coinflip(options.num,options.printseq)
    coinopt(options.num)
