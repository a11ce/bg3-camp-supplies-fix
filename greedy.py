import util
from structs import Result


def greedy(inventory: dict, target=40, verbose=False) -> Result:
    dbgprint = print if verbose else lambda x: x

    selections = []
    supplies_so_far = 0

    # in case we can't get 40 without going over
    potential_overflow = None

    # sort inventory dict by item value
    inv_sorted = sorted(inventory.items(), key=lambda x: x[1], reverse=True)

    for item, quantity in inv_sorted:
        for _ in range(quantity):
            value = util.supplies[item]
            dbgprint(f"Evaluating item: {item}, value {value}")
            if util.supplies[item] + supplies_so_far <= target:
                selections.append(item)
                supplies_so_far += value
                dbgprint(
                    f"Added {item} to selections. Current supplies: {supplies_so_far}"
                )

                if supplies_so_far == target:
                    return Result(selections, supplies_so_far)
            else:
                if potential_overflow is None or value < util.supplies[
                        potential_overflow]:
                    potential_overflow = item
                dbgprint(
                    f"Skipped {item}. Current supplies: {supplies_so_far}")
                continue

    # if we can't get to 40 without going over, add the item that would put us over
    if potential_overflow is not None:
        selections.append(potential_overflow)
        supplies_so_far += util.supplies[potential_overflow]
        dbgprint(
            f"Can't reach 40! Added {potential_overflow} as overflow. Current supplies: {supplies_so_far}"
        )
        return Result(selections, supplies_so_far)

    # total failure
    if supplies_so_far < target:
        dbgprint("Couldn't reach 40!")
        return Result(selections, supplies_so_far)
