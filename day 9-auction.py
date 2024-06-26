import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

def main():
    print("Welcome to the secret auction program!")
    
    bids = {}
    bidding_finished = False
    
    while not bidding_finished:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        bids[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            bidding_finished = True
        elif should_continue == 'yes':
            clear()
    
    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid}")

if __name__ == "__main__":
    main()
