from math import comb


def combination(list_val, int_val):
    list_len = len(list_val)
    if 1 < sum(list_val) <= 1000 and 1 < list_len < 20 and 1 < int_val < 20:
        return comb(list_len, int_val)
    else:
        return "No valid subsequence"


def test(a=[], b=0, output=None):
    result = combination(a, b)
    print(f"List A:{a}, Integer B:{b},Result:{result}, test:{result == output}")


# example 1 passing case
test(a=[1, 2, 8], b=2, output=3)
# example 2 edge case
test(a=[5, 17, 1000, 11], b=4, output="No valid subsequence")
# edge case all zeros
test(a=[0,0,0,0], b=2, output="No valid subsequence")
# empty list
test([], 3, output="No valid subsequence")
# passing string instead of list
test("", "2", output="No valid subsequence")
