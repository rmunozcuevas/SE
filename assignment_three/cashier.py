class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = 0
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """
        Return True when the payment is accepted,
        or False if money is insufficient.
        """
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print("Payment successful ✅")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
