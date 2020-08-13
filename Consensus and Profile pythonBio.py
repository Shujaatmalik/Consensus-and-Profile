# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:45:37 2020

@author: Shujaat
"""

from Bio import motifs
from Bio import SeqIO
Seqlist=list()
for seq_record in SeqIO.parse("FASTA_test.fasta", "fasta"):
    Seqlist.append(seq_record.seq)
m = motifs.create(Seqlist)
print(m.consensus)
print(m.counts)