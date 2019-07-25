

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

a = map( lambda x,y : print(y) , [ x for x in mcase.items() ] ,[ y for y in mcase.items() ] )
print(set(a))
#a = dict(map( lambda a : 1 if a[0] in {a[0],a[1]} else a[0]  ,[(x,y) for x,y in mcase.items()]))
#print(a)



input = [1, 1, 2]

c = map( lambda x : x ** 2 , input)
# print(set(c))

# for n in range(2, 10):
#     set = 1
#     for x in range(2, n):
#         if n % x != 0:
#             pass
#         else:
#             print(n, 'equals', x, '*', n / x)
#             set = 0
#             break
#     if set == 1:
#         print(n," is a prime number")
