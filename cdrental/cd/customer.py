
class Customer(object):
    def __init__(self, customer_id, name, rented, rentedArray):
        if type(customer_id) == str and type(name) == str and type(rented) == int:
            customer_id.rented = rented
            customer_id.rentedArray = rentedArray
            self.customer_id = customer_id
            self.name = name
            self.rentedArray = rentedArray
            self.rented = rented
        else:
            print "error inputs"
 
class GetCustomerName(object):
    def __init__(self,customer_id):
        if type(customer_id) == str:
            return 
    