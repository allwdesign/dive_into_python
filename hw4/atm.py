import sys
from decimal import Decimal

TOP_UP_ACTION = 1
WITHDRAWAL_ACTION = 2
EXIT_ACTION = 3
LOG = 4
MULTIPLICITY_OF_THE_AMOUNT = 50
WITHDRAWAL_INTEREST = Decimal("0.015")  # 1.5%
MIN_WITHDRAWAL_INTEREST_LIMIT = 30
MAX_WITHDRAWAL_INTEREST_LIMIT = 600
TRANSACTION_NUMBER = 3
ACCRUE_INTEREST = Decimal("0.030")  # 3%
EXCEEDING_THE_AMOUNT = 5_000_000
WEALTH_ORDER = Decimal("0.100")  # 10%
FORMAT_STRING_SIZE = 65

balance = Decimal("0.000")
count_top_up = 0
count_withdrawal = 0
operations_log = list()


def print_log() -> None:
    """Print information from operations log."""
    for data in operations_log:
        print(f'Action: {data["action"]}. Amount: {data["amount"]:.3f}$')


def add_to_log(action: str, amount: Decimal) -> None:
    """Add data about top-up or withdrawal operation to log.

    :param action: str
    :param amount: Decimal
    :return: None
    """
    operations_log.append(
        {"action": action, "amount": amount})


def help_info() -> None:
    """The function shows the help menu for the user."""
    print(FORMAT_STRING_SIZE * '=', 'Available actions:',
          FORMAT_STRING_SIZE * '=', sep='\n')
    print('\t1 - top-up', '\t2 - withdrawal', '\t3 - exit', '\t4 - log',
          FORMAT_STRING_SIZE * '=', sep='\n')


def print_balance() -> None:
    """The function displays the current account balance to the user."""
    print(FORMAT_STRING_SIZE * '=',
          f'Balance: {get_account_balance(): .3f} $',
          sep='\n')


def get_account_balance() -> Decimal:
    """The function returns the current balance of funds on the account.

    :return: Decimal
    """
    return balance


def deduct_tax(amount: Decimal) -> Decimal:
    """Deducts 10% wealth tax.

    Deducts 10% wealth tax before each transaction, if the amount
    exceeds 5,000,000.

    :param amount: Decimal
    :return: Decimal
    """
    amount -= (amount * WEALTH_ORDER)
    add_to_log("deducts 10% wealth tax", amount * WEALTH_ORDER)
    return amount


def accrue_interest() -> None:
    """Accrue interest 3%.

    After every third top-up or withdrawal transaction, interest - 3%

    :return: None
    """
    global balance
    interest = balance * ACCRUE_INTEREST
    balance += interest
    add_to_log("accrue interest 3%", interest)
    print(FORMAT_STRING_SIZE * '=',
          f'Accrue interest 3%: {interest: .3f}',
          sep='\n')


def withdrawal(amount: Decimal) -> None:
    """Mechanism for withdrawing funds from the account.

    :param amount: Decimal
    :return: None
    """
    global balance, count_withdrawal

    msg = ''
    interest = calculate_withdrawal_interest(amount)
    amount += interest

    # You can't withdraw more than you have on your account
    if balance - amount > 0:
        balance -= amount
        msg = f'For this operation, the bank is withdrawn: {interest: .3f} $'

        count_withdrawal += 1

        if count_withdrawal % TRANSACTION_NUMBER == 0:
            accrue_interest()
    else:
        msg = 'Insufficient funds in the account'

    print(FORMAT_STRING_SIZE * '=')
    print(msg)


def calculate_withdrawal_interest(amount: Decimal) -> Decimal:
    """Calculate withdrawal interest.

    Withdrawal interest — 1.5% of the withdrawal amount, but not less
    than 30 and not more than 600 $.

    :param amount: Decimal
    :return: Decimal
    """
    one_and_half_percent = amount * WITHDRAWAL_INTEREST

    if one_and_half_percent < MIN_WITHDRAWAL_INTEREST_LIMIT:
        # < 30
        limit = MIN_WITHDRAWAL_INTEREST_LIMIT
    elif one_and_half_percent > MAX_WITHDRAWAL_INTEREST_LIMIT:
        # > 600
        limit = MAX_WITHDRAWAL_INTEREST_LIMIT
    else:
        limit = one_and_half_percent
    return limit


def top_up(amount: Decimal) -> None:
    """Mechanism of replenishment of funds on the account.

    :param amount: Decimal
    :return: None
    """
    global balance, count_top_up

    balance += amount
    count_top_up += 1
    if count_top_up % TRANSACTION_NUMBER == 0:
        accrue_interest()


def menu_exit() -> None:
    """System exit function from the application."""
    print_balance()
    print(FORMAT_STRING_SIZE * '=')
    sys.exit()


def get_amount(action: int) -> Decimal:
    """Get amount from user for complete the transaction

    If an incorrect amount is entered, an error message will be
    displayed, and you will be prompted enter another amount.

    :param action: int. Action selected by the user
    :return: Decimal. The amount of user funds to complete the transaction
    """
    msg = ''
    while True:
        print(FORMAT_STRING_SIZE * '=')
        amount = Decimal(input('Enter amount: '))

        if amount <= 0:
            msg = 'The amount must be greater than zero'
            amount = Decimal("0.000")
        else:
            # amount > 0
            if amount % MULTIPLICITY_OF_THE_AMOUNT != 0:
                # The amount of top-up and withdrawal is a multiple 50$
                msg = ('The amount of top-up and withdrawal must be'
                       ' a multiple of 50')
                amount = Decimal("0.000")

            if amount > EXCEEDING_THE_AMOUNT:
                # If the amount exceeds 5 million, deduct 10% wealth tax
                # before each transaction, even an erroneous one
                amount = deduct_tax(amount)
                msg = f'Order of wealth 10%: {amount: .3f}'

        if msg:
            print(FORMAT_STRING_SIZE * '=')
            print(msg)
        break

    return amount


def do_action() -> None:
    """Perform the action selected by the user."""
    actions = {
        TOP_UP_ACTION: top_up,
        WITHDRAWAL_ACTION: withdrawal,
        EXIT_ACTION: menu_exit,
        LOG: print_log}

    help_info()
    user_input = int(input("Enter action number: "))

    if user_input not in actions:
        print(FORMAT_STRING_SIZE * '=')
        raise ValueError("You entered an invalid number")

    # Call the withdrawal(amount) or top-up(amount), or menu_exit()
    if (user_input == TOP_UP_ACTION) or (user_input == WITHDRAWAL_ACTION):
        amount = get_amount(user_input)
        if amount:
            action = actions.get(user_input, 0)
            add_to_log(action.__name__, amount)
            action(amount)

    else:
        # menu_exit() or print_log()
        actions.get(user_input, 0)()


def run() -> None:
    """Run the app."""
    print(FORMAT_STRING_SIZE * '=',
          f"{int(FORMAT_STRING_SIZE / 2.5) * ' '} "
          f"ATM app",
          sep='\n')
    while True:
        try:
            do_action()
            print_balance()
        except TypeError:
            print("You enter incorrect type data")
        except ValueError as exp:
            print(exp)


if __name__ == '__main__':
    run()
