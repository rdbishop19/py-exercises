stockDict = {
    "GE": "General Electric",
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 ),
    ( 'GM', 250, '11-sep-1987', 32 ),
    ( 'EK', 150, '23-may-1986', 44 ),
]

'''
Create a purchase history report that computes the full purchase price 
(shares times dollars) for each block of stock and uses the stockDict 
to look up the full company name. This is the basic relational database 
join algorithm between two tables.

Example output for one block: 
I purchased General Electric stock for $4800
'''
for purchase in purchases:
    stock_abbrev = purchase[0]
    for k, v in stockDict.items():
        if k == stock_abbrev:
            stock = v
    print(f'I purchased {stock} stock for ${purchase[1]*purchase[3]}')

'''
Create a second purchase summary that which 
accumulates total investment by ticker symbol. 
In the above sample data, there are two blocks of GE. 
These can easily be combined by creating a dict 
where the key is the ticker and the value is the 
list of blocks purchased. The program makes one pass 
through the data to create the dict. A pass through the 
dict can then create a report showing each ticker symbol 
and all blocks of stock.

------ GE ------
100 shares at 48 dollars each on 01-jul-1998
200 shares at 56 dollars each on 10-sep-2001

Total value of stock in portfolio: $16000
'''
print('-------------')

purchase_summary = {}

for purchase in purchases:
    stock_abbrev = purchase[0]
    if stock_abbrev in purchase_summary.keys():
        purchase_summary[stock_abbrev].append(purchase)
    else:
        purchase_summary[stock_abbrev] = [purchase]
    
# trying out python decorator function to add spaces around output
def formatted(fn):
    def formatted_summary():
        print()
        fn()
        print()
    return formatted_summary

# function to print stock summary for each stock
@formatted
def print_summary():
    print(f'Total value of stock in portfolio: ${total_value}')

def header_dashes(text):
    dashes = 10
    def wrapper(text):
        padding = '-'*dashes
        print(padding + text + padding)
    return wrapper

@header_dashes
def print_header(text):
    return text
    
# general p
for stock, purchases in purchase_summary.items():
    total_value = 0
    print_header(stock)
    for purchase in purchases:
        num_shares = purchase[1]
        date = purchase[2]
        price = purchase[3]
        print(f'{num_shares} shares at {price} dollars each on {date}')
        total_value += (num_shares * price)
    print_summary()


