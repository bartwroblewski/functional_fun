from functools import reduce, partial

def merging_reducer(host, guest):
    def inner(acc, curr, host, guest):
        print(acc, curr)
        if curr == host:
            return (*acc, (host, guest))
        if curr == guest:
            return acc
        return acc + (curr,)
    return partial(inner, host=host, guest=guest)

tup = (1, 2, 3, 4)
def reduce_tup(f): return reduce(f, tup, tuple())

assert reduce_tup(merging_reducer(1, 2)) == ((1, 2), 3, 4)
assert reduce_tup(merging_reducer(2, 3)) == (1, (2, 3), 4)
assert reduce_tup(merging_reducer(3, 4)) == (1, 2, (3, 4))
assert reduce_tup(merging_reducer(1, 3)) == ((1, 3), 2, 4)
assert reduce_tup(merging_reducer(1, 4)) == ((1, 4), 2, 3)
assert reduce_tup(merging_reducer(4, 1)) == (2, 3, (4, 1))
assert reduce_tup(merging_reducer(2, 4)) == (1, (2, 4), 3)
assert reduce_tup(merging_reducer(4, 3)) == (1, 2, (4, 3))
