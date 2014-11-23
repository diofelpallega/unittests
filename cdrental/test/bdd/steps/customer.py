class Customer(object):
	def __init__(self, customer_id, name, rentedArray, rented): 
		self.customerHasRented = {}
		self.customerHasRentedArray = {}
		self.customerHasRented[customer_id] = rented
		self.customerHasRentedArray[customer_id] = rentedArray
		self.customer_id = customer_id
		self.name = name
		self.rentedArray = self.customerHasRentedArray[customer_id]
		self.rented = self.customerHasRented[customer_id]

	def updateAddrented(self,customer_id): 	
		self.rented = self.customerHasRented[customer_id] + 1
		self.customerHasRented[customer_id] += 1

	def updateRemoverented(self,customer_id):
		self.rented = self.customerHasRented[customer_id] - 1
		self.customerHasRented[customer_id] -= 1

	def updateRentedArray(self,customer_id,cdTitle):
		self.rentedArray = self.customerHasRentedArray[customer_id] + [cdTitle]
		self.customerHasRentedArray[customer_id] += [cdTitle]

	def getIdName(self):
		return self.name

	def HowManyIsRented(self):
		return self.rented