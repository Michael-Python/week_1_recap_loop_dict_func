# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(self):
    # to check what is returned
    # print(self["name"])
    # self["name"] returns the shop name because it is the only 'name' on this layer of the program.because
    return self["name"]
    
def get_total_cash(self):
    
    return self["admin"]["total_cash"]

def add_or_remove_cash(self, cash):
    # print(cash)
    # print(self["admin"]["total_cash"])
    self["admin"]["total_cash"] += cash
    return self

def get_pets_sold(self):
    return self["admin"]["pets_sold"]