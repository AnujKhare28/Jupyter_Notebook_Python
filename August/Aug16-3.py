class MinimumBalanceError(Exception):
    pass

balance = 10000

def withdraw(amt):
    global balance

    if balance - amt < 5000:
        raise MinimumBalanceError('Minimum balance should be 5000')
    else:
        balance -= amt
        print('Remaining balance is ', balance)

amt = int(input('Enter withdrawal amount: '))

try:
    withdraw(amt)
except MinimumBalanceError as m:
    print(m)