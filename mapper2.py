#!/usr/bin/env python
import sys

for line in sys.stdin:
    doc_id, text = line.split(',')
    words = text.split()
    
    for word in words:
        print(f'{doc_id}\t{word}')