import json


def save(data: dict) -> None:
    """Save data to json file."""
    print("== Save to json file ==")
    with open('tree.json', 'w') as f:
        json.dump(data, f)


def load() -> None:
    """Load data from json file."""
    print("== Load data from json file ==")
    with open('tree.json', 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    for line in json_file:
        print(f"{line['name']} {line['parent']} {line['type']}"
              f" {line['size']}")
