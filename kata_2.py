from functools import reduce


def persistence(n):
    num_ranks_count = lambda x: len(str(x))
    multiplicity_count = 0
    while num_ranks_count(n) > 1:
        n = reduce(lambda x, y: x * y, [int(x) for x in str(n)])
        multiplicity_count += 1
    return multiplicity_count


test_num = 25
print(persistence(test_num))
#
# test.assert_equals(persistence(39), 3)ё
#        test.assert_equals(persistence(4), 0)
#        test.assert_equals(persistence(25), 2)
#        test.assert_equals(persistence(999), 4)
