#!/usr/bin/env python
"""Provides a command-line API to ABX.score"""

import argparse
import os

from ABXpy.score import score

def parse_args():
    parser = argparse.ArgumentParser(usage="%(prog)s task distance [score]",
                                     description='ABX score computation')

    parser.add_argument(
        'task', help=('task file generated by the task module '
                      'containing the triplets and the pairs associated to '
                      'the task specification'))

    parser.add_argument(
        'distance', help=('distance file generated by the distance package, '
                          'containing the distance between pairs of a task'))

    parser.add_argument(
        'score', nargs='?', default=None,
        help='optional: score file, where the computation results will be put')

    return parser.parse_args()


def main():
    args = parse_args()

    if os.path.exists(args.score):
        print("Warning: overwriting score file {}".format(args.score))
        os.remove(args.score)

    score(args.task, args.distance, args.score)


if __name__ == '__main__':
    main()
