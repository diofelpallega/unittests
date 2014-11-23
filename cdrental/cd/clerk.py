from cd import *
from customer import *
 

            
class Clerk(object):
    def __init__(self):
        pass
    
    def checkout(self, customer_id, cd_id):
        if (type(customer_id) == str) and (type(cd_id) == str) and (cd_id.isRented == "false"):           
            cd.isRented = "true"
            customer_id.rented = customer_id.rented + 1
            customer_id.rentedArray = customer_id.rentedArray + [cd_id.content_title]

        
        else: 
            print "Invalid Account"

    def checkin(self, customer_id, cd_id):
        if type(customer_id) == str and type(cd_id) == str and cd_id.isRented == "true":
            cd_id.isRented = "false"
            customer_id.rented = customer_id.rented - 1
            customer_id.rentedArray = (customer_id.rentedArray).remove(cd_id.content_title)
 