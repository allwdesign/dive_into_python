class MyDict(dict):
    def my_get(self, key, default_value=None):
        """Method analogous to get for a dictionary."""
        try:
            return self[key]
        except KeyError:
            return default_value


def my_get(data: dict, key, default_value):
    """Function analogous to get for a dictionary."""
    try:
        data[key]
    except KeyError:
        return default_value


if __name__ == '__main__':
    my_dict = MyDict({'name': 'Alice', 'age': 7})
    name = my_dict.my_get('name', 'My default value')
    print(name)

    print(my_dict.my_get('src', 'My default value'))
    
    print(my_dict.my_get('name', 'Name') == my_dict.get('name', 'Name'))


