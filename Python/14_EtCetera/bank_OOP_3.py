# Creating bank using OOP:

class Account:
    def __init__(self):
         self._balance = 0;#_balace means it is aprivate var and only class methods can access it.


    @property
    def balance(self):
         return self._balance;


    def deposit(self, n):
         self._balance += n;

    def withdraw(self, n):
         self._balance -= n;


def main():
     account = Account();
     print(f"Balance: {account.balance}");
     account.deposit(1000000);
     account.withdraw(3000);
     print(f"Balance: {account.balance}");


if __name__ == "__main__":
     main();