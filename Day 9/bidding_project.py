
class Biding:
    def __init__(self):
        self.bid_details = dict()
        self.highest_bidder = None
        self.bidding_finished = False
 

    def bid_func(self):
        while not self.bidding_finished:
            name = input("What is your name?:")
            bid_price = int(input("What's your bid?: $"))

            self.bid_details[name] = bid_price

            other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

            if other_bidders == "yes":
                self.high_bidder_update(name)
                
                
            elif other_bidders == "no":
                self.high_bidder_update(name)
                self.bidding_finished = True
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
    



