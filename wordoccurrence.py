from collections import Counter
from re import split

BANNER = "-" * 35

def format_print(counter, is_reverse=False):

    palabrasvac = ['a', 'about', 'above', 'across', 'after', 'afterwards']
    palabrasvac += ['again', 'against', 'all', 'almost', 'alone', 'along']
    palabrasvac += ['already', 'also', 'although', 'always', 'am', 'among']
    palabrasvac += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
    palabrasvac += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
    palabrasvac += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
    palabrasvac += ['because', 'become', 'becomes', 'becoming', 'been']
    palabrasvac += ['before', 'beforehand', 'behind', 'being', 'below']
    palabrasvac += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
    palabrasvac += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
    palabrasvac += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
    palabrasvac += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
    palabrasvac += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
    palabrasvac += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
    palabrasvac += ['every', 'everyone', 'everything', 'everywhere', 'except']
    palabrasvac += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
    palabrasvac += ['five', 'for', 'former', 'formerly', 'forty', 'found']
    palabrasvac += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
    palabrasvac += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
    palabrasvac += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
    palabrasvac += ['herself', 'him', 'himself', 'his', 'how', 'however']
    palabrasvac += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
    palabrasvac += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
    palabrasvac += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
    palabrasvac += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
    palabrasvac += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
    palabrasvac += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
    palabrasvac += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
    palabrasvac += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
    palabrasvac += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
    palabrasvac += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
    palabrasvac += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
    palabrasvac += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
    palabrasvac += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
    palabrasvac += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
    palabrasvac += ['some', 'somehow', 'someone', 'something', 'sometime']
    palabrasvac += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
    palabrasvac += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
    palabrasvac += ['then', 'thence', 'there', 'thereafter', 'thereby']
    palabrasvac += ['therefore', 'therein', 'thereupon', 'these', 'they']
    palabrasvac += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
    palabrasvac += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
    palabrasvac += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
    palabrasvac += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
    palabrasvac += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
    palabrasvac += ['whatever', 'when', 'whence', 'whenever', 'where']
    palabrasvac += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
    palabrasvac += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
    palabrasvac += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
    palabrasvac += ['within', 'without', 'would', 'yet', 'you', 'your']
    palabrasvac += ['yours', 'yourself', 'yourselves']

    lst = list(counter.items())
    lst = [x for x in lst if x not in palabrasvac]
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
