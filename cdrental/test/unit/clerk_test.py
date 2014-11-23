import unittest
from customer import *
from cd import *
from clerk import *

class TestClerk(unittest.TestCase):

    def test_Clerk_can_update_data(self):
        customer = Customer("000-001","Jill",[],0)
        cd = Cd()
        cd.input(customer, "00-01","Edge of Tomorrow","false","none") 
        clerk = Clerk()
        clerk.checkout(customer,cd,'000-001','00-01') 
        self.assertEqual(cd.isRented,"true") 
        self.assertEqual(customer.rented,1)
        clerk.checkin(customer,cd,'000-001','00-01')
        self.assertEqual(cd.isRented,"false") 
        self.assertEqual(customer.rented,0)

    def test_clerk_object_can_recognize_info(self):
        customer = Customer("000-001","Jack",[],0) 
        self.assertEqual(customer.customer_id,"000-001")
        self.assertEqual(customer.name,"Jack")
        self.assertEqual(customer.rented,0)
        self.assertEqual(customer.rentedArray,[])

    def test_clerk_object_updates_rentANDcustomerStatus_when_checkedOut(self):
        customer = Customer("000-001","Jill",[],0)
        cd = Cd()
        cd.input(customer, "00-01","Edge of Tomorrow","false","none")
        clerk = Clerk()
        clerk.checkout(customer, cd,'000-001', '00-01')
        self.assertEqual(cd.isRented,"true") 
        self.assertEqual(customer.rented,1)
        self.assertEqual(customer.rentedArray,["Edge of Tomorrow"])
        self.assertEqual(cd.rentedBy,"Jill")

    def test_clerk_object_updates_rentANDcustomerStatus_when_checkedIn(self): 
        customer = Customer("000-001","Jack",[],0)
        cd = Cd()
        cd.input(customer, "00-01","Edge of Tomorrow","false","none")
        clerk = Clerk()
        clerk.checkout(customer,cd,"000-001","00-01")
        clerk.checkin(customer,cd,"000-001","00-01")
        self.assertEqual(cd.isRented,"false")

    def test_clerk_object_checks_rent_exceeds_three(self): 
        customer = Customer("000-001","Jack",[],0)
        cd = Cd()
        cd.input(customer, "00-01","Edge of Tomorrow","false","none")
        cd1 = Cd()
        cd1.input(customer, "00-02","3 Idiots","false","none")
        cd2 = Cd()
        cd2.input(customer, "00-03","Shaun of the Dead","false","none")
        cd3 = Cd()
        cd3.input(customer, "00-04","Lets be Cops","false","none")
        clerk = Clerk() 
        clerk.checkout(customer, cd, "000-001","00-01")
        clerk.checkout(customer, cd1, "000-001","00-02")
        clerk.checkout(customer, cd2, "000-001","00-03")
        clerk.checkout(customer, cd3, "000-001","00-04")
        print customer.rentedArray
        self.assertEqual(len(customer.rentedArray),3)
        self.assertEqual(customer.rentedArray,["Edge of Tomorrow","3 Idiots","Shaun of the Dead"])