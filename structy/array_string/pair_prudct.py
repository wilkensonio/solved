
"""
pair product
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
"""

def pair_product(numbers, target_product):
    seen = {}

    for i , num in enumerate(numbers):
        comp = target_product // num
        if comp in seen:
            return (seen[comp], i)
        seen[num] = i

print(pair_product([3, 2, 5, 4, 1], 8))