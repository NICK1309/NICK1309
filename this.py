# oop=>
# object
# class
# attributes
# methods
class Mobile:
    # Static / class attrs
    __shape = "Cuboid"
    # constructor
    def __init__(self):
        # instance attributes
        self.__ram = None          # public
        self.__processor = None# protected
        self.__price = None          # private
    
    def __data(self):
        return f'Ram: {self.__ram}\nProcessor: {self.__processor}\nPrice: {self.__price}'

    def __str__(self):
        return self.__data()
    # instance methods 
    # getter or accessor
    def get_ram(self):
        return self.__ram
    def get_processor(self):
        return self.__processor
    def get_price(self):
        return self.__price

    # setters for setting up the values 
    def set_ram(self, ram):
        self.__ram = ram
    def set_processor(self, processor):
        self.__processor = processor
    def set_price(self, price):
        self.__price = price
  #class methods
    @classmethod  #decorators to decorate our functions 
    def get_shape(cls):
        return cls.__shape
    @classmethod
    def set_shape(cls, shape):
        cls.__shape = shape
        @staticmethod()
        def extra():
            return 'Hello user!'    

m1 = Mobile()
m2 = Mobile()
m3 = Mobile()

print(m1)
print(m2)
print(m3)
print(m1.extra())
# print(m1.ram)
# print(m2.data())
# print( Mobile.data(m1) )

# print(m1.__price)
# m1.__price= 1
# print(m1.__price)

# print(m1._Mobile__price)

# obj1 = "nikita"
# print(obj1)
# print("Success")

print( m1.get_price() )
m1.set_price(90000)
print( m1.get_price() )
print(m1)

#decorators =>
# def be_positive(func):
#     def func(n1,n2):
#         if n1<n2:
#             n1,n2 = n2,n1
#         return n1-n2   
#     return func    

# @be_positive   
# def sub(n1,n2):
#     return n1-n2
# print(sub(10,50))    









