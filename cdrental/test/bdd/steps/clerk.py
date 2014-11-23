from customer import *
from cd import *
from clerk_test import *

class Clerk(object):
    def __init__(self):
        pass

    def checkout(self, customer, instance,customer_id, cd_id): 
        if ((type(customer_id) == str) and (type(cd_id) == str) and \
            (instance.isItRented(cd_id) == "false") and             \
            ((customer.HowManyIsRented()) <= 3) and 
            (len(customer.rentedArray )) < 3): 

            instance.changeRentStatus(cd_id, "true")  
            customer.updateAddrented(customer_id) 
            cdTitle = instance.getCdTitle()
            rentedBy = customer.getIdName()
            customer.updateRentedArray(customer_id, cdTitle)
            instance.updateRentedBy(cd_id, rentedBy)

            print "Rental Contract"
            print "Customer ID: ", customer_id
            print "Customer Name: ", rentedBy
            print "CD ID: ", cd_id
            print "CD Name: ", cdTitle
            print "Sign Here: ____________________"
        else:
            print "It might be an input Error, Try Again"

    def checkin(self, customer, instance, customer_id, cd_id):
        if ((type(customer_id) == str) and (type(cd_id) == str) and \
            (instance.isItRented(cd_id) == "true") and              \
            ((customer.HowManyIsRented()) > 0) and 
            (len(customer.rentedArray )) > 0): 
            
            instance.changeRentStatus(cd_id, "false")  
            customer.updateRemoverented(customer_id) 
        else:
            print "error input"


