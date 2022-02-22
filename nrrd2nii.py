#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DESCRIPTION:
#   Python 3 command line tool designed to convert nrrd (or nrrd header
#   and image) files to NIFTI-1 images. The corresponding output
#   file is of the same name with a different file extension.
#
# NOTE:
#   Constructed from answer as shown on StackOverflow: https://stackoverflow.com/a/48469229
#
# Adebayo B. Braimah 17:12 Feb 22, 2022


"""Command line tool designed to convert nrrd (or nrrd header and image) files 
to NIFTI-1 images. The corresponding output file is of the same name with a 
'.nii' or '.nii.gz' file extension.
"""


# Import modules
import os
import sys
import nrrd
import nibabel as nib
import numpy as np

import argparse
from typing import Any, Dict, Tuple


def main():
    """Main function."""
    args, parser = arg_parser()

    # Print help message in the case of no arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        args: Dict[str, Any] = vars(args)

    outfile: str = nrrd2nii(nrrd_file=args.get("nrrd"), gzip=args.get("gzip"))

    if os.path.exists(outfile):
        exit_status: int = 0
    else:
        exit_status: int = 1

    sys.exit(exit_status)


def nrrd2nii(nrrd_file: str, gzip: bool = False) -> str:
    """Converts a nrrd (or nhdr, complete with raw image data) file(s) to
    a NIFTI-1 image file. The resulting output NIFTI file will be an image
    file of the same name with the NIFTI file extension.

    Usage example:
        >>> nrrd2nii('image.nrrd')
        'image.nii'

    Arguments:
        nrrd_file: Input nrrd file to be converted.
        gzip: Gzip output NIFTI-1 file.

    Returns:
        Path to output file.
    """
    if gzip:
        ext: str = "nii.gz"
    else:
        ext: str = "nii"

    nrrd_file: str = os.path.abspath(nrrd_file)
    out_file: str = f"{nrrd_file[:-4]}{ext}"

    data: Tuple = nrrd.read(nrrd_file)
    img: nib.Nifti1Image = nib.Nifti1Image(data[0], np.eye(4))
    nib.save(img, out_file)
    return out_file


def arg_parser() -> Tuple[argparse.ArgumentParser.parse_args, argparse.ArgumentParser]:
    """Argument parser."""
    # Init parser
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=55, width=100
        ),
    )

    # Parse Arguments
    reqoptions = parser.add_argument_group("Required Arguments")

    reqoptions.add_argument(
        "-n",
        "--nrrd",
        dest="nrrd",
        type=str,
        metavar="<STR>",
        default=None,
        help="REQUIRED: Input nrrd or nhdr file.",
    )

    optoptions = parser.add_argument_group("Optional Arguments")

    optoptions.add_argument(
        "-z",
        "--gzip",
        dest="gzip",
        default=False,
        action="store_true",
        help="OPTIONAL: Gzips output file.",
    )

    args: argparse.ArgumentParser.parse_args = parser.parse_args()
    return args, parser


if __name__ == "__main__":
    main()
