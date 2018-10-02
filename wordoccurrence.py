from collections import Counter
from re import split

BANNER = "-" * 35

def format_print(counter, is_reverse=False):

    lst = list(counter.items())
    lst.sort(key=lambda a_b: (a_b[1], a_b[0]), reverse=is_reverse)
    print(("[Unique Words: %d]" % len(lst)).center(35, "="))
    print("%-16s | %16s" % ("Word", "Count"))
    print(BANNER)
    for word, count in lst:
        print("%-16s | %16d" % (word, count))

def count_words(filename):
    counter = Counter()
    with open(filename, "rU") as f:
        for line in f:
            line = line.strip().lower()
            if not line:
                continue
            counter.update(x for x in split("[^a-zA-Z']+", line) if x)
    return counter

format_print(count_words("test.txt"), is_reverse=False)
