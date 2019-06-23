from pizzapy import *

first_name = ''
last_name = ''
email = ''
number = ''
address_zip = ''
credit_card = ''
expire = ''
zipcode = ''
code = ''


customer = Customer(first_name,last_name,email,number,address_zip)
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

menu = my_local_dominos.get_menu()

order = Order.begin_customer_order(customer, my_local_dominos)
order.add_item('10SCPFEAST')
order.add_item('20BCOKE')

card = CreditCard(credit_card,expire,code,zipcode)
order.place(card)

my_local_dominos.place_order(order, card)
