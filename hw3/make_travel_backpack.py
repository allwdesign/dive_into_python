from itertools import combinations
from decimal import Decimal

MAX_WEIGHT_BACKPACK = 10
THINGS_QUANTITY = 15

travel_things = {
    'tent': Decimal("3"),
    'bowler hat': Decimal("1.7"),
    'flashlight': Decimal("0.230"),
    'mug': Decimal("0.047"),
    'spoon': Decimal("0.018"),
    'salt': Decimal("0.020"),
    'water': Decimal("5"),
    'food': Decimal("3"),
    'sleeping bag': Decimal("4.2"),
    'flint': Decimal("0.045"),
    'walkie-talkie': Decimal("0.1"),
    'socks': Decimal("0.070"),
    'underwear': Decimal("0.070"),
    't-shirt': Decimal("0.200"),
    'spare shoes': Decimal("1.1"),
    'sports trousers': Decimal("0.350"),
    'notebook': Decimal("0.250"),
    'pencil': Decimal("0.006"),
}


def pack_backpack(things: dict) -> tuple[list, float]:
    """Pack travel backpack

    We add things to the backpack only if the thing, together with the
    things already collected, does not exceed the maximum carrying
    capacity of the backpack.

    :return: tuple[list, float]. List of travel things in backpack
            and weight.
    """
    travel_backpack = list()
    current_weight = 0

    while current_weight <= MAX_WEIGHT_BACKPACK:
        # Are there any other things to pack?
        if things:
            key, val = things.popitem()

            if current_weight + val <= MAX_WEIGHT_BACKPACK:
                current_weight += val
                travel_backpack.append(key)
            else:
                continue
        else:
            break

    return travel_backpack, current_weight


def get_weight_things(things: tuple[str]) -> Decimal:
    """Get weight of things in current combinations

    :param things: tuple[str]
    :return: Decimal
    """
    global travel_things
    current_weight = 0

    for item in things:
        current_weight += travel_things[item]

    return current_weight


def get_possible_combinations() -> list[tuple]:
    """Get possible combinations of travel items and their weight

    :return: list[tuple]
    """
    global travel_things
    travel_backpack = list()

    for items in combinations(travel_things.keys(), THINGS_QUANTITY):
        if get_weight_things(items) <= MAX_WEIGHT_BACKPACK:
            travel_backpack.append((items, get_weight_things(items)))

    return travel_backpack


if __name__ == '__main__':
    backpack, weight = pack_backpack(travel_things.copy())
    backpack.reverse()
    print(f"Backpack contain: {', '.join(backpack)}.")
    print(f'Weight: {weight:.3f} kg.')

    # Print possible combinations of travel things
    combinations_str = (f'Possible combinations for travel backpack '
                        f'where weight < {MAX_WEIGHT_BACKPACK} kg:')
    print(len(combinations_str) * '=')
    print(combinations_str)
    print(len(combinations_str) * '=')

    for i, items in enumerate(get_possible_combinations(), 1):
        things, weight = items
        print(f"{i} things: {', '.join(things)}. Weight: {weight:.3f} kg.")
