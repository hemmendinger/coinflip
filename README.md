Coinflip
========
Coinflip generator

Prints formatted results to standard output.

Usage:

    -h, --help

    --coinflips NUM, -n NUM
    where NUM is the number of flips

    default with no options is a single flip

optimization:
    using random.randint(0,1) to generate 0's and 1's
    representing heads or tails is much slower than
    evaluation of random.random() floats

