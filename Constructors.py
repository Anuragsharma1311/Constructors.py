class Phone:
    def __init__ (self,color,cost):
       self.color=color
       self.cost=cost

    def details(self):
        print('color of my phone is' , self.color)
        print('cost of my phone is' , self.cost)

apple= Phone('Bule', '₹10,999')
apple.details()