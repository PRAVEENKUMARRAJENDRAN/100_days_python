
class Biding:
    def __init__(self):
        self.bid_details = dict()
        self.highest_bidder = None
 

    def bid_func(self):
        name = input("What is your name?:")
        bid_price = int(input("What's your bid?: $"))

        self.bid_details[name] = bid_price

        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

        if other_bidders == "yes":
            self.high_bidder_update(name)
            self.bid_func()
            
        elif other_bidders == "no":
            self.high_bidder_update(name)
            return f"The winner is {self.highest_bidder} with the bid price of {self.bid_details[self.highest_bidder]} "


    def high_bidder_update(self, name):
        if self.highest_bidder is not None and self.bid_details[self.highest_bidder] < self.bid_details[name]:
            self.highest_bidder = name
        else: 
            self.highest_bidder = name
            






if __name__ == '__main__':
    logo = '''
                            ___________
                            \         /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-' `'---------'` '-'
                            )"""""""(
                            /_________\\
                        .-------------.
                        /_______________\\
    '''

    print(logo)
    print("Welcome to the secret auction program.")
    b = Biding()
    print(b.bid_func())
    



