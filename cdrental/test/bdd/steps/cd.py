

class Cd(object):
    def __init__(self): 
        self.isCdRented = {} 
        self.titleOfCd = {} 

    def input(self, customer, cd_id, content_title, isRented, rentedBy): 
        if ((customer.HowManyIsRented() <= 3) and (type(rentedBy) == str) and \
           (type(cd_id) == str) and (type(content_title) == str) and \
           (len(customer.rentedArray )) < 3):

            self.isCdRented[cd_id] = isRented
            self.titleOfCd[cd_id] = content_title
            self.cd_id =  cd_id
            self.content_title = content_title 
            self.isRented = self.isCdRented[cd_id]   
            self.rentedBy = rentedBy

        else:
            print "Rent Amount Exceeded"
    
    def isItRented(self, cd_id): 
        return self.isCdRented[cd_id]

    def changeRentStatus(self, cd_id,isRented): 
        self.isCdRented[cd_id]= isRented
        self.isRented = isRented 
 

    def get_status(self, cd_id): 
        return self.isCdRented.get(cd_id)
         
    def getCdTitle(self):
        return self.content_title

    def updateRentedBy(self, cd_id, rentedBy): 
        self.rentedBy = rentedBy