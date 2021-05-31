#Python Program to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
from collections import Counter
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
# Take input from user    
str = input("Please Enter a string: ")
d2 = Counter(most_frequent(str)).most_common()
print(d2)
