"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""



'''
listA = open('task02a.txt', 'r').read().split()
listB = open('task02b.txt', 'r').read().split()
listC = open('task02c.txt', 'r').read().split()
a = 0
b = 0
c = 0
for i in range(int(len(listA)/3)):
    d = int(listA.index(i+1))*3
    e = int((listA.index(i+1))*3)-1
    f = int((listA.index(i+1))*3)-2
    if (d**2+e**2)**0.5 == f or (d**2+f**2)**0.5 == e or (f**2+e**2)**0.5 == d:
        a = a + 1
for i in listB:
    d = listB.index(i)-1
    e = (listB.index(i)*2)-1
    f = (listB.index(i)*3)-1
    if (d**2+e**2)**0.5 == f or (d**2+f**2)**0.5 == e or (f**2+e**2)**0.5 == d:
        b = b + 1
for i in listC:
    d = listC.index(i)-1
    e = (listC.index(i)*2)-1
    f = (listC.index(i)*3)-1
    if (d**2+e**2)**0.5 == f or (d**2+f**2)**0.5 == e or (f**2+e**2)**0.5 == d:
        c = c + 1
triples = {'2a': a, '2b': b, '2c': c}
print(triples)

for i in range()
'''

def attempt(file)
    splitContents = open(file,'r').read().split('\n')
    num = 

