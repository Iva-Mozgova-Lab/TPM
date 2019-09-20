#!/usr/bin/env python


import argparse
import pandas as pd
import os

    

parser = argparse.ArgumentParser(description='convert counts to tpm values')
parser.add_argument('-i', '--infile', help='counts values csv file', required =True)
parser.add_argument('-l', '--length', help='list of gene name and length', required =True)
parser.add_argument('-o', '--outfile', help='converted values csv file', required =True)

args = parser.parse_args()
length = args.length
infile = args.infile
out = args.outfile



df_counts = pd.read_csv(infile,sep='\t')

df_length = pd.read_csv(length,sep='\t')

df_col = pd.merge(df_length, df_counts, on='GeneID')
df_col ['length'] = df_col['length'].div(1000)

df_col.update(df_col.iloc[:,2:].div(df_col['length'], axis="index"))

df_permil= df_col.iloc[:,2:].sum(axis=0)
df_permil = df_permil/1000000

df_col.update(df_col.iloc[:,2:]/df_permil)
df_col.to_csv(out,sep='\t',index=False)