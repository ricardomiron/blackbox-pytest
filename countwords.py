from collections import Counter
def main():

    file = input('Enter the name of the text file: ')

    with open(r'exceptions.txt') as e:

        exceptions = [exception for line in e for exception in line.split()]

    with open(file) as f:

        words = [word for line in f for word in line.split()]
        words = [x for x in words if x not in exceptions]
        print("The total word count is:", len(words))

        c = Counter(words)
        for word, count in c.most_common():
            print(word, count)
main()
