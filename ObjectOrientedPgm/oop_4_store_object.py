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
        print "___ PRODUCT INFORMATION (" + self.item_name + ") ___"
        for attr, value in sorted(self.__dict__.iteritems()):
            # call external function to print float price with two decimals
            if attr == 'price':
                value = print_price(value)
            if attr == 'cost':
                value = print_price(value)
            # call external function to remove _ from attribute name
            print key_no_line(attr.upper()), ":", value
        return self

class Store(object):
    def __init__(self, products, address, city, state, owner):
        self.products = products
        self.address = address
        self.city = city
        self.state = state
        self.owner = owner
    def add_product(self, Product):
        # method adds product to the store inventory
        # can add existing or new products
        # for new products - pass Product(attributes)
        self.products.append(Product)
        return self
    def remove_product(self, Product):
        # method removes product by reference to the Product object
        # if pointer does not exist to the Product object,
        # then must search for product object before invoking the method
        self.products.remove(Product)
        return self
    def print_inventory(self):
        # method prints full inventory of store
        for product_item in self.products:
            product_item.display_info()
        return self


def print_price(price):
    # returns price with $ and two decimals
    return "$%.2f" % (price)
def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")


# MAIN PROGRAM
# create new objects of class product
shirt1 = Product(19.99, 'polo shirt', 0.25, 'Branding', 15.00)
shirt2 = Product(24.00, 't-shirt', 0.1, 'Better Brand', 15.00)
pants1 = Product(49.99, 'jeans', 0.5, 'Best Jeans', 40.00)
pants2 = Product(89.99, 'slacks', 0.33, 'Business Attire', 75.00)

# create new object of class store
store1 = Store([shirt1, shirt2], '123 Main Street', 'Chicago', 'IL', 'Bob Allen')

# add existing products to store
store1.add_product(pants1)
# print store1.products[2].item_name

# add non-existing product to store
store1.add_product(Product(100.00, 'bike', 65, 'MountainTrek', 50))
# print store1.products[3].item_name

# remove pants product from store inventory
# store1.remove_product(pants1)
# for product_item in store1.products:
#     print product_item.item_name

# find and remove the bike we added to the store inventory without reference
# for product_item in store1.products:
#     if product_item.item_name == 'bike':
#         store1.remove_product(product_item)
# for product_item in store1.products:
#     print product_item.item_name

# print full store inventory
store1.print_inventory()