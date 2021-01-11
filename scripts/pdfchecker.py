#!/usr/bin/env python3

# Invoke Datalogics PDF Checker & parse its output

# USAGE: ./pdfchecker.py $pdf_filepath

import sys
from subprocess import check_call, check_output


def analyze_pdf_file(pdf_filepath):
    output = check_output([
        'PDF_Checker/pdfchecker',
        '--profile',
        'PDF_Checker/CheckerProfiles/everything.json',
        '--input',
        pdf_filepath]).decode()
    parse_output(output)

def parse_output(output):
    pass # TODO


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(sys.argv, file=sys.stderr)
        print('Exactly one argument must be passed to pdfchecker.py', file=sys.stderr)
    analyze_pdf_file(sys.argv[1])
