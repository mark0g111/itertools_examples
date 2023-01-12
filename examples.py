import itertools

# Make an iterator that returns object over and over again.
rep = itertools.repeat(8)
for _ in range(10):
    print(next(rep), end=' ')
print()

# Make an iterator that returns evenly spaced values starting with number start.
c = itertools.count(19, 5)
for _ in range(10):
    print(next(c), end=' ')
print()

# Make an iterator returning elements from the iterable and saving a copy of each.
pos_neg_ones = itertools.cycle([1, -1])
for _ in range(10):
    print(next(pos_neg_ones), end=' ')
print()

# Make an iterator that drops elements from the iterable as long as the predicate is true.
print(list(itertools.dropwhile(lambda x: x < 23, sorted([17, 19, 91, 62, 6, 12, 72]))))

# Make an iterator that returns elements from the iterable as long as the predicate is true.
print(list(itertools.takewhile(lambda x: x < 23, sorted([17, 19, 91, 62, 6, 12, 72]))))

# Make an iterator that returns elements from the first iterable until it is exhausted,
#                       then proceeds to the next iterable
letters = itertools.chain('abc', 'defg', 'hijklm', 'nopqrst', 'uvwxyz')
for letter in letters:
    print(letter, end=' ')
print()

# Return n independent iterators from a single iterable.
n = range(5)
a, b, c = itertools.tee(n, 3)
for i in a:
    print(i, end=' ')
print()

# Make an iterator that returns accumulated sums, or accumulated results of other binary functions
s = itertools.accumulate(range(7))
for i in s:
    print(i, end=' ')
print()

# Make an iterator that returns selected elements from the iterable.
x = itertools.islice(range(5), 3)
for i in x:
    print(i, end=' ')
print()

# Cartesian product of input iterables.
prod = itertools.product([1, 2, 3], 'ABC')
for i in prod:
    print(i, end=' ')
print()

# Return successive r length permutations of elements in the iterable.
perm = itertools.permutations([1, 2, 3], 2)
for i in perm:
    print(i, end=' ')
print()

# Return r length subsequences of elements from the input iterable.
s = itertools.combinations([1, 2, 3], 2)
for i in s:
    print(i, end=' ')
print()
