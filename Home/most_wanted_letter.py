#!/usr/bin/env checkio --domain=py run most-wanted-letter
from collections import Counter


def checkio(text: str) -> str:
    letters = sorted(filter(str.isalpha, text.lower()))
    counter = Counter(letters)
    most = counter.most_common(1)[0][0]
    return most
