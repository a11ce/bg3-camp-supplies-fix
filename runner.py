import random
import sys

supplies = {}
target = 40
spacer = "----------------------------------"

def load_inventory(path: str):
    items = {}
    with open(path, 'r') as reader:
        for line in reader.readlines():
            parts = line.split(':')
            if parts != []: items[parts[0]] = int(parts[1])
    return items

def process_inv_file(path: str):
    inv = load_inventory(path)
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
            print(f"Evaluating item: {item}, Current supplies: {supplies_so_far}")
            if supplies[item] + supplies_so_far <= target:
                selections.append(item)
                supplies_so_far += supplies[item]
                print(f"Added {item} to selections. Current supplies: {supplies_so_far}")

                if supplies_so_far == target:
                    return selections
            else:
                if potential_overflow is None:
                    potential_overflow = item
                print(f"Skipped {item}. Current supplies: {supplies_so_far}")
                continue

    # if we can't get to 40 without going over, add the item that would put us over
    if potential_overflow is not None:
        selections.append(potential_overflow)
        supplies_so_far += supplies[item]
        print(f"Can't reach 40! Added {potential_overflow} as overflow. Current supplies: {supplies_so_far}")
        return selections
    
    # total failure
    if supplies_so_far < target:
        print("Couldn't reach 40!")
        return selections
                
 
if __name__== "__main__": 
    supplies = load_inventory("supplies.txt")
    # first arg is the file name
    chosen = process_inv_file(sys.argv[1])
    print(spacer)
    print(chosen)