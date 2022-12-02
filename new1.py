class Mobile:
    #static /class attributes
    shape = 'Cuboid'
    #constructor
    def __init__(self):
        # instance attributes
      self.__ram = None   #public
      self.__processor = None  #protected
      self.__price = None #private

    def __data(self):
         return f'Ram: {self.ram}\nProcessor: {self.processor}\nPrice {self.price}' 





     #setters


    #for class  attrs
    def get_shape(self):
       return  self.__shape
    def set_shape(self, shape):
        self.__shape = shape

m1 = Mobile('16 GB','8 GEN 1',90000) #m1 is a object or reference variable.
m2 = Mobile('12 GB','865+',55000)
m3 = Mobile('8 GB','855',35000)

        # print(m1)
        # print(m2)
        # print(m3)
        #print(m1.ram)
    # print(m2.data())
    # print(Mobile.data(m1))

m1 = Mobile()
m2 = Mobile()
m3 = Mobile()
print("Success")
print(m1.get_shape)