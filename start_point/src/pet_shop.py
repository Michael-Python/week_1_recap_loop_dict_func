# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(self):
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

def increase_pets_sold(self, sold):
    self["admin"]["pets_sold"] += sold
    return self

def get_stock_count(self):
    return len(self["pets"])

def get_pets_by_breed(pets, breed_type):
    breed_list = []
    for pet in pets["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
            pets["pets"].remove(pet)

def add_pet_to_stock(pets, new_pet):
    pets["pets"].append(new_pet)
    
def get_customer_cash(cash):
    return cash["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return customer["cash"]


##### Calls this one to check the count of pets #####
def get_customer_pet_count(counts):
    counts = len(counts["pets"])
    return counts

# def get_customer_pet_count(customer):
#     return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pets):
    if pets["price"] > customer["cash"]:
        return False
    else:
        return True

