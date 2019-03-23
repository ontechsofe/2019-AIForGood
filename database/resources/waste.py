from random import randint

class Waste:
    def __init__(self, b, t, id=None):
        self.id = id if id else randint(100000, 999999)
        self.bin_id = b
        self.category = t
    
    def get_id(self):
        return self.id
    
    def get_bin_id(self):
        return self.bin_id
    
    def set_bin_id(self, id):
        self.bin_id = id

    def get_category(self):
        return self.category
    
    def set_id(self, c):
        self.category = c