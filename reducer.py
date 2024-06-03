#!/usr/bin/env python
"""reducer.py - Processes key-value pairs received from the mapper, where each key is a word 
and each value is a document ID where the word appeared. This script aggregates the document IDs 
for each word and outputs the word alongside the set of unique document IDs where the word was found.
The reducer reads lines of input from standard input, where each line has a format of 'word,document_id'.
The input lines are expected to be sorted by the word. The reducer uses this sorted order to efficiently
aggregate document IDs by using a set data structure, transitioning between different words as it processes
the input lines one-by-one.
"""
import sys
from collections import defaultdict

unique_document_ids = defaultdict(list)

for line in sys.stdin:
    # Split the input line into word and document IDs
    word, document_id = line.strip().split('\t')

    # Add the document ID to the list for the current word
    unique_document_ids[word].append(document_id)

# Emit each word and its unique document IDs
for word, document_ids in unique_document_ids.items():
    unique_document_ids_string = ','.join(document_ids)
    sys.stdout.write('%s\t%s\n' % (word, unique_document_ids_string))
    print(f"{word}\t, {unique_document_ids_string}")