#!/bin/sh

# extract_x_seqs.sh
# 
# Modified by Bruno Costa on 01/06/2015
# Copyright 2015 ITQB / UNL. All rights reserved.

# Call: extract_x_seqs.sh  [fasta] [start] [Num of Seqs]

FILE=$1
START=$2
N_SEQS=$(( $3 + $START )) 

#Get dir of this script
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

awk -v N_SEQS=$N_SEQS -v START=$START '{ tmp = match($0, /^>.*/)      
  if(tmp){
    a++;
  }      
  if(tmp && a < N_SEQS && a >= START ){
    print $0; newline;
  }
  if( tmp==false && a < N_SEQS && a >= START ){
    print $0;
  }        
  if( a >= N_SEQS ){
    exit 0
  }
}' ${FILE}


