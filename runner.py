import random

supplies = {}
target = 40

def load_inventory(fname):
    items = {}
    with open(fname, 'r') as reader:
        for line in reader.readlines():
            parts = line.split(':')
            if parts != []: items[parts[0]] = int(parts[1])
    return items

def process(fname: str):
    inv = load_inventory(fname)
    process(inv)

def process(inventory: dict):
    selections = []
    supplies_so_far = 0
    for item, quantity in inventory.items():
        for _ in range(quantity):
            if quantity <= 0: break

            value = supplies[item]
            if value + supplies_so_far <= target:
                selections.append(item)
                supplies_so_far += value
                if supplies_so_far == target: return selections
            else:
                

def process_random(inventory: dict):
    selections = []
    supplies_so_far = 0
    while (supplies_so_far < target):
        item, quantity = random.choice(list(inventory.items()))
        value = supplies[item]
        for _ in quantity:
            if value + supplies_so_far <= target:
                selections.append(item)
                supplies_so_far += value
            else:
                continue


        
        



    
  
  
 
if __name__== "__main__": 
    supplies = load_inventory("values.txt")