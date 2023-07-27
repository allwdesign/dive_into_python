friends_and_things = {
    "Irina": ('tent', 'bowler hat', 'flashlight', 'mug', 'water'),
    "Lucy": ('flashlight',
             'mug',
             'spoon',
             'salt',
             'food',
             'flint',
             'walkie-talkie',
             'socks',
             'underwear',
             't-shirt',
             'spare shoes',
             'sports trousers',
             ),
    "Olga": ('flashlight',
             'mug',
             'spoon',
             'food',
             'sleeping bag',
             'flint',
             'walkie-talkie',
             'socks',
             'underwear',
             't-shirt',
             'spare shoes',
             'sports trousers',
             'notebook',
             'pencil',
             ),
}

friends_things_sets = dict()
for friend_name, things in friends_and_things.items():
    things_set = set()

    for thing in friends_and_things[friend_name]:
        things_set.add(thing)

    friends_things_sets[friend_name] = things_set


all_things = set()
all_friends_have_except_one = set()
only_one_friend_has = set()

for t_set in friends_things_sets.values():
    all_things |= t_set

# The dictionary has become less than one friend
fr_name, fr_things = friends_things_sets.popitem()

for friend_name, t_set in friends_things_sets.items():
    all_friends_have_except_one |= t_set

print(f"Things that all three friends took: {', '.join(all_things)}")
print(f"all_friends_have_except_one = {all_friends_have_except_one}")

only_one_friend_has = fr_things - all_friends_have_except_one
print(f"Things are unique, only one friend has {fr_name}: "
      f"{', '.join(only_one_friend_has)}.")

all_friends_have_except_one -= fr_things
print(f"Things that all friends have except one: "
      f"{', '.join(all_friends_have_except_one)}. This thing is "
      f"missing: {fr_name}.")

