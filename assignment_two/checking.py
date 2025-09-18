from raybank import RayBank

class CheckingAcc(RayBank):
    def __init__(self, customer_name, current_balance, minimum_balance, overdraft_limit=100):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.current_balance - amount < -self.overdraft_limit:
            print(f" Withdrawal denied. You’ve exceeded your overdraft limit of {self.overdraft_limit}.")
        else:
            self.current_balance -= amount
            print(f" Withdrawal successful. Current balance: {self.current_balance}")

    def apply_fee(self, fee=25):
        if self.current_balance < self.minimum_balance:
            self.current_balance -= fee
            print(f" Fee applied! ${fee} deducted. New balance: {self.current_balance}")
        else:
            print(" No fees applied, balance is healthy.")
