from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]  # We want the most recent version
    account = (get_account())  # We need an account as we are going to make some state changes
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]        #Most recent version
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()