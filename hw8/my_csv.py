import csv


def save(data):
    """Save data to csv file."""
    print("== Save to csv file ==")
    with open('tree.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=["name",
                                                        "parent",
                                                        "type",
                                                        "size"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(data)


def load() -> None:
    """Load data from csv file."""
    print("== Load data from csv file ==")
    with open('tree.csv', 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, fieldnames=["name", "parent",
                                                 "type", "size"],
                                  dialect='excel',
                                  quoting=csv.QUOTE_NONNUMERIC)
        for line in csv_file:
            print(f"{line['name']} {line['parent']} {line['type']}"
                  f" {line['size']}")
