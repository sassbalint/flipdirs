# -*- coding: utf-8 -*-
"""
This module creates a copy of a directory structure
outer (1st) and inner (2st) level flipped.
"""

import argparse
import os

# https://stackoverflow.com/questions/273192
def makedir(dirname):
    """Safe mkdir."""
    try:
        os.makedirs(dirname)
    except FileExistsError:
        pass

def symlink(src, dst):
    """Safe ln -s."""
    try:
        os.symlink(src, dst)
    except FileExistsError:
        pass

# starting point: https://stackoverflow.com/questions/16953842
def flipdirs(origdir, flipdir, inner_READMEs):
    """
    Starting from `origdir` directory structure
    create a new directory structure at `flipdir`
    outer (level#1) and inner (level#2) directories flipped,
    and populate it with symlinks
    pointing to appropriate files in `origdir`.
    """
    outer = ''
    for root, dirs, files in os.walk(origdir):
        current = os.path.basename(root)

        path = root.split(os.sep)
        length = len(path)

        if length == 1: # root=level0
            os.mkdir(flipdir) # if (not) exists? XXX
        elif length == 2: # outer=level1 ~ by corpus
            outer = current
        elif length == 3: # inner=level2 ~ by format
            inner = current
            makedir(os.path.join(flipdir, inner))

            rootdir = os.path.join(os.pardir, os.pardir, origdir)

            # dir
            symlink(
                os.path.join(rootdir, outer, inner),
                os.path.join(flipdir, inner, outer))
                # note that outer and inner are in reverse order :)

            # README
            readme_name = 'README.' + inner + '.md'
            symlink(
                os.path.join(rootdir, inner_READMEs, readme_name),
                os.path.join(flipdir, inner, readme_name))
            # XXX I'd like this:
            # if os.path.isfile(readme_path):
            #     symlink...
            # else:
            #     some warning like "Create README.md please."
            # but I was not able to find out how to determine
            # whether the README.md exists or not.
            # isfile() always returns False.

        # for f in files: -- not needed

def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '--origdir',
        help='original root directory',
        required=True,
        type=str),
    parser.add_argument(
        '--flipdir',
        help='target root directory for flipped directory structure',
        required=True,
        type=str)
    parser.add_argument(
        '--inner_READMEs',
        required=True,
        help='directory under --origdir containing inner (2nd) level README.md files',
        type=str)

    return parser.parse_args()

def main():
    """Main."""
    args = get_args()
    flipdirs(args.origdir, args.flipdir, args.inner_READMEs)

if __name__ == '__main__':
    main()
