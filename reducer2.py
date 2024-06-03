#!/usr/bin/env python
import sys
from collections import defaultdict


def print_max_word(doc_id, word_counts):
    max_word = max(word_counts, key=word_counts.get)
    max_count = word_counts[max_word]
    print(f"{doc_id}\t{max_word}\t{max_count}")


current_doc = None
word_counts = defaultdict(int)

for line in sys.stdin:
    doc_id, word = line.strip().split('\t')
    
    if doc_id != current_doc:
        if current_doc is not None:
            print_max_word(current_doc, word_counts)
        current_doc = doc_id
        word_counts.clear()
    
    word_counts[word] += 1

if current_doc is not None:
    print_max_word(current_doc, word_counts)
