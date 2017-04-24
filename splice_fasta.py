#!/usr/bin/env python3

###########
#
# Created by Bruno Costa @ITQB
# 24/04/2017
# This allows the extraction of specific coordinates from a fasta file
#
############

import argparse
import re

parser = argparse.ArgumentParser(description='This allows the extraction of specific coordinates from a fasta file')

## blast result, output, cutoff,
#parser.add_argument('--flag', type=str, nargs=1, metavar='', dest='', required=True, help='')
parser.add_argument('--fa', type=str, metavar='input file', dest='input', required=True, help='Input fasta file.')
parser.add_argument('--seq', type=str, metavar='Sequence', dest='seq', required=False, help='Sequence selector.')
parser.add_argument('--wildSeq', type=str, metavar='Sequence', dest='wildSeq', required=False, help='Sequence selector with wild-cards.')
parser.add_argument('--cStart', type=int, metavar='Coordinate', dest='cStart', required=True, help='Coordinate start.')
parser.add_argument('--cStop', type=int, metavar='Coordinate', dest='cStop', required=True, help='Coordinate end.')


args = parser.parse_args()
fasta_file=args.input
sequence=args.seq
Start=args.cStart
Stop=args.cStop
wildSequence=args.wildSeq


def FASTA_parser(fasta_file):
        """Franciso P.Martins - From https://github.com/StuntsPT/4Pipe4/blob/master/pipeutils.py 
        Parse, convert and return fasta files into a dict like: 'name':'seq'."""
        fasta = open(fasta_file, 'r')
        d = {}
        for lines in fasta:
                if lines.startswith('>'):
                        name = lines[1:].strip()
                        d[name] = ''
                else:
                        d[name] += lines.strip().upper()
        fasta.close()
        return d

fasta=FASTA_parser(fasta_file)




if(sequence is not None):
  print("Using provided sequence")
  print(">"+sequence+"\n"+fasta[sequence][Start:Stop])
elif(wildSequence is not None):
  print("Using wild-card sequence")
  for seq in fasta.keys():
    if(re.match(wildSequence,seq)):
      print(">"+seq+"\n"+fasta[seq][Start:Stop])
else:
  #Stop
  print("No sequence provided - Splice done on all sequences")
  for seq in fasta.keys():
    print(">"+seq+"\n"+fasta[seq][Start:Stop])
