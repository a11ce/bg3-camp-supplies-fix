import sys
from collections import defaultdict
import greedy
import util

allAlgos = [greedy.greedy]


def compareAlgos(algos, maxItems, maxQuantity):
    results = defaultdict(int)

    for idx in range(1000):
        test = util.generate_random_inv(maxItems, maxQuantity)
        for algo in algos:
            solution = algo(test)
            if solution.totalSupplies == 40:
                results[algo.__name__] += 1

    for algo in algos:
        print(f"{algo.__name__} solved\t{results[algo.__name__]}/1000 tests")


if __name__ == "__main__":
    compareAlgos(allAlgos, maxItems=30, maxQuantity=10)
