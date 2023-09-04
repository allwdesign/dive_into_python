import pickle


def save(data) -> None:
    """Save data to pickle file."""
    print("== Save to pickle file ==")
    with open('tree.pickle', 'wb') as f:
        pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)


def load() -> None:
    """Load data from pickle file."""
    print("== Load data from pickle file ==")
    with open('tree.pickle', 'rb') as f:
        data = pickle.load(f)

    for line in data:
        print(f"{line['name']} {line['parent']} {line['type']}"
              f" {line['size']}")


