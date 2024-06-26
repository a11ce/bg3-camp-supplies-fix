import random
import sys
import util
import greedy

target = 40
spacer = "----------------------------------"


def process_inv_file(path: str):
    inv = util.load_inventory(path)
    print("Inventory: ")
    print(inv)
    print(spacer)
    return greedy.greedy(inv, verbose=True)


if __name__ == "__main__":
    results = None
    util.load_supplies()
    # first arg is the file name

    if len(sys.argv) < 2:
        print(
            """Help:\n\npython runner.py <args>\n\tArgument options:\n\t--file <path>: path to inventory file\n\t--random <max_items> <max_quantity>: generates random inventory"""
        )
        exit(1)

    if sys.argv[1] == "--random":
        if len(sys.argv) < 4:
            print(
                "Please provide the max number of unique items and max quantity of each item."
            )
            exit(1)
        inv = util.generate_random_inv(int(sys.argv[2]), int(sys.argv[3]))
        results = greedy.greedy(inv, verbose=True)

    elif sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Please provide the path to the inventory file.")
            exit(1)
        results = process_inv_file(sys.argv[2])

    print(spacer)
    print("Results:")
    print(results)
    print(spacer)
