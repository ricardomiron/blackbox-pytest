#import the Counter module
from collections import Counter

def main():

    #user inputs file names separated by spaces
    file = input('Enter the name of the text file(s): ')
    files = file.split(" ")

    #read the file with the words we want to exclude and make a list
    with open(r'exceptions.txt') as e:
        exceptions = [exception for line in e for exception in line.split()]

    #iterate over each file name
    for y in files:

        with open(y) as f:

            words = [word for line in f for word in line.split()]
            #ignore the intersection between the current list and the excpetions list
            words = [x for x in words if x not in exceptions]
            print("\nThe total word count is:", len(words), "from file", y)

            c = Counter(words)
            #show the list of words by the frequency of appearance
            for word, count in c.most_common():
                print(word, count)
main()
