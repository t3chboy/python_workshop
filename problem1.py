"""
Simplify the code below
Target - Result should be in 4 lines
"""

words = 'a quick a brown fox jumped brown a fox'.split()
count = {}

for word in words:
    count[word] = count[word] + 1 if word in count else 1
print(count)
