import random

supplies = None


def load_supplies() -> dict:
    global supplies
    if supplies is None:
        supplies = load_inventory("supplies.txt")
    return supplies


def load_inventory(path: str):
    items = {}
    with open(path, 'r') as reader:
        for line in reader.readlines():
            parts = line.split(':')
            if parts != []: items[parts[0]] = int(parts[1])
    return items


def sum_value(inv: list):
    sum = 0
    for item in inv:
        sum += supplies[item]
    return sum


def generate_random_inv(max_items: int, max_quantity: int):
    # pick random item from supplies and add it to inv with random quantity
    inv = {}
    items = list(supplies.keys())
    for _ in range(random.randint(1, max_items)):
        item = random.choice(items)
        inv[item] = random.randint(1, max_quantity)

    return inv


load_supplies()
