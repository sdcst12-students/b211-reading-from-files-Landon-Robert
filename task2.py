"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
listA = open('task02a.txt', 'r').read().split()
listB = open('task02b.txt', 'r').read().split()
listC = open('task02c.txt', 'r').read().split()
a = 0
b = 0
c = 0
for i in listA:

triples = {'2a': a, '2b': b, '2c': c}
print(triples)