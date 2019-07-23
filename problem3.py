import os
from psutil import *
def fetch_squares(max_root):
    squares = []
    for n in range(max_root):
        squares.append(n ** 2)
    return squares


MAX = 5

for square in fetch_squares(MAX):
    print(square)




process = Process(os.getpid())
mi = process.memory_info()[0] / float(2 ** 20)
print(mi)
