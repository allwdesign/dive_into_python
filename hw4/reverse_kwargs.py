def rev_kwargs(**kwargs: dict) -> dict:
    """The function for reverse key and value in kwargs.

    The function accepts only key parameters as input and returns a
    dictionary, where the key is the value of the passed argument,
    and the value is the name of the argument. If the key is not
    hashable, use it string representation.

    :param kwargs: dict
    :return: dict
    """
    d = dict()
    for key, val in kwargs.items():
        if isinstance(val, (list, dict)):
            val = str(val)
        d.update({val: key})

    return d


if __name__ == '__main__':
    print(rev_kwargs(name="tony", age=42))
    print(rev_kwargs(res=1, reverse=[1, 2, 3]))
    print(rev_kwargs(
        res=1,
        reverse={1: "Moscow", 2: "Novosibirsk", 3: "Tula"}))
