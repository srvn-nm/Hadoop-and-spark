#!/usr/bin/env python
"""mapper.py - This mapper script reads text input from standard input, in the format "document_id,text".
It processes each line to extract words and emits each word along with the document ID it appeared in. 
Each word is emitted only once per document to ensure uniqueness.
"""
import sys

for line in sys.stdin:
    # Split the input line into document ID and text
    document_id, text = line.strip().split('\t')

    # For each word in the text, emit a unique pair of (word, document ID)
    for word in text.split():
        sys.stdout.write('%s\t%s\n' % (word, document_id))