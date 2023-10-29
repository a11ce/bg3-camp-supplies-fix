import random
import sys
import util

target = 40
spacer = "----------------------------------"

def process_inv_file(path: str):
    inv = util.load_inventory(path)
    print("Inventory: ")
    print(inv)
    print(spacer)
    return process_inv(inv)

def process_inv(inventory: dict):
    selections = []
    supplies_so_far = 0

    # in case we can't get 40 without going over
    potential_overflow = None

    # sort inventory dict by item value
    inv_sorted = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    
    for item, quantity in inv_sorted:
        for _ in range(quantity):
            value = util.supplies[item]
            print(f"Evaluating item: {item}, value {value}")
            if util.supplies[item] + supplies_so_far <= target:
                selections.append(item)
                supplies_so_far += value
                print(f"Added {item} to selections. Current supplies: {supplies_so_far}")

                if supplies_so_far == target:
                    return selections
            else:
                if potential_overflow is None or value < util.supplies[potential_overflow]:
                    potential_overflow = item
                print(f"Skipped {item}. Current supplies: {supplies_so_far}")
                continue

    # if we can't get to 40 without going over, add the item that would put us over
    if potential_overflow is not None:
        selections.append(potential_overflow)
        supplies_so_far += util.supplies[potential_overflow]
        print(f"Can't reach 40! Added {potential_overflow} as overflow. Current supplies: {supplies_so_far}")
        return selections
    
    # total failure
    if supplies_so_far < target:
        print("Couldn't reach 40!")
        return selections
                
 
if __name__== "__main__": 
    results = None
    util.load_supplies()
    # first arg is the file name

    if len(sys.argv) < 2:
        print("""Help:\n\npython runner.py <args>\n\tArgument options:\n\t--file <path>: path to inventory file\n\t--random <max_items> <max_quantity>: generates random inventory""")
        exit(1)

    if sys.argv[1] == "--random":
        if len(sys.argv) < 4:
            print("Please provide the max number of unique items and max quantity of each item.")
            exit(1)
        inv = util.generate_random_inv(int(sys.argv[2]), int(sys.argv[3]))
        results = process_inv(inv)

    elif sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Please provide the path to the inventory file.")
            exit(1)
        results = process_inv_file(sys.argv[2])

    print(spacer)
    print("Results:")
    print(results)
    print(spacer)