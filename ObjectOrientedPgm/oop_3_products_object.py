class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
        self.return_desc = ''       # optional attribute can hold description later
    def sell(self):
        # method changes status
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        # method adds tax (parameter) to price
        return round(self.price * (1 + tax), 2)
    def return_item(self, return_desc):
        # method evaluates return description to change status and price (optionally)
        self.return_desc = return_desc
        if return_desc == 'defective':
            self.status = return_desc
            self.price = 0
        elif return_desc == 'in box, like new':
            self.status = 'for sale'
        elif return_desc == 'open box, used':
            self.status = 'used'
            self.price = round(self.price * 0.8, 2)
        return self
    def display_info(self):
        # method prints all attributes and values
        print "___ PRODUCT INFORMATION ___"
        for attr, value in sorted(self.__dict__.iteritems()):
            # call external function to print float price with two decimals
            if attr == 'price':
                value = print_price(value)
            if attr == 'cost':
                value = print_price(value)
            # call external function to remove _ from attribute name
            print key_no_line(attr.upper()), ":", value
        return self

def print_price(price):
    # returns price with $ and two decimals
    return "$%.2f" % (price)
def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")


# MAIN PROGRAM
shirt1 = Product(19.99, 'polo shirt', 0.25, 'Branding', 15.00)
shirt2 = Product(24.00, 't-shirt', 0.1, 'Better Brand', 15.00)

shirt2.sell().return_item('open box, used').display_info()