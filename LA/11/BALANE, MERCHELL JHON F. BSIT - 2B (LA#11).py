class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

       
    def describePhone(self):
        return f'''
Brand: {self.brand}
Model: {self.model}  
'''

class Android(Phone):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
Samsung = Android("Samsung","s23+")


print(Samsung.describePhone())