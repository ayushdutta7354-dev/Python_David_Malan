# bank app:

balance = 0;

def main():
    global balance;
    deposit(1000000);
    withdraw(3700);
    print(f"Balance: {balance}");


def deposit(amount):
    global balance;
    balance += amount;
    return balance;

def withdraw(amount):
    global balance;
    balance -= amount;
    return balance;

if __name__ == "__main__":
    main();

