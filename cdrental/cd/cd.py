
class Cd(object):
    def __init__(self, cd_id, content_title, isRented, rentedBy):
        if type(cd_id) == str and type(content_title) == str:
            cd_id.isRented = isRented
            self.cd_id = cd_id
            self.content_title = content_title
            self.isRented = isRented
            self.rentedBy = rentedBy
        else:
            print "error inputs"

class CdCollection(object):
    def __init__(self):
        self.cdisRented = {} 

    def id_is_rented(self, cd_id):
        return cdStatus[cd_id]

