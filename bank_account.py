"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
by Mwesigwa David Keneth
"""

def bank_account():
    # pass/

if __name__ == '__main__':
    key, value = input().split(',')
    bank_dict = {}
    bank_dict[key] = value
    print(bank_account(bank_dict))