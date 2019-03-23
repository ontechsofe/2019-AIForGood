from random import randint
from waste import Waste
class Bin:
    def __init__(self, l, id=None):
        self.id = id if id else randint(100000, 999999)
        self.loc = l
        self.num_waste[0, 0, 0, 0]
        self.waste = []
        self.filled = [False, False, False, False]
        print(self.all_filled())
    
    def get_id(self):
        return self.id
    
    def get_loc(self):
        return self.loc

    def set_loc(self, l):
        self.loc = l
    
    def get_num_waste(self, category=None):
        if category > -1 and category < 4:
            return self.num_waste[category]
    
    def all_filled(self):
        return all(self.filled)
    
    def get_filled(self):
        return self.filled

    def set_filled(self, category, value=True):
        self.filled[category] = value

    def new_garbage(self, category)
        self.waste.append(Waste(self.get_id(), category))
        num_waste[category] += 1
    
    def empty(self, category=None):
        if not category:
            self.waste = []
            self.num_waste[0, 0, 0, 0]
            self.filled = [False, False, False, False]
        else:
            for x in self.waste:
                if x.get_category() == category:
                    self.waste.remove(x)
            self.get_num_waste[category] = 0
            self.filled[category] = 0