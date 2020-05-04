"""
pdf_to_png.py: convert pdf pages to png images
Author: Nicolas Poirier - @NicolasPoirie19
GitHub: https://github.com/nicolas-poirier
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

# need to install pymupdf (python -m pip install pymupdf) to use fitz
import fitz
from os import listdir, getcwd
from os.path import isfile, join, abspath
from argparse import ArgumentParser

if __name__ == '__main__':

    # script arguments
    parser: ArgumentParser = ArgumentParser(description='Convert pdf pages to png images')
    parser.add_argument('-d', '--directory', help='Input directory where the pdf files can be found', default=abspath(getcwd()))
    parser.add_argument('-z', '--zoom', help='zoom to apply to the pages before exctration', default=1, type=int)
    args = parser.parse_args()

    # list files and directory in input directory
    for file in listdir(args.directory):
        # convert only pdf files
        if isfile(join(args.directory, file)) and file.endswith(".pdf"):            
            doc = fitz.open(join(args.directory, file))
            for page in doc:
                matrice = fitz.Matrix(args.zoom, args.zoom)
                pix = page.getPixmap(matrix = matrice)
                pix.writeImage(f"{join(args.directory, file).rstrip('.pdf')}_page-{str(page.number)}.png")