names = ['Tony', 'Alex', 'Petr', 'Lucy']
rates = [1000, 850, 1200, 600]
premiums = ["18.00%", "10.25%", "5.75%", "3.5%"]

person_and_bonus = {
    name: rates[i]*float(premiums[i][:-1]) for i, name in enumerate(names)}

if __name__ == '__main__':
    # {'Tony': 18000.0, 'Alex': 8712.5, 'Petr': 6900.0, 'Lucy': 2100.0}
    print(person_and_bonus)
