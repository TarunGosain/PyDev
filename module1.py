'''
Created on 28-May-2018

@author: tarun1991
'''

from UnitData import UnitData


class MyClass():
    
    def calculateConsistency(self):

        def calculate(self, capacity, productionData):
            avg = sum(productionData) / len(productionData)
            extraProduction = avg - capacity
            
            if(extraProduction < 0):
                print("Unit " + self +" is producing " + str(extraProduction) + " units LESS daily")
            if(extraProduction > 0):
                print("Unit " + self +" is producing " + str(extraProduction) + " units MORE daily")
            if(extraProduction == 0):
                print("Unit " + self +" is producing exactly " + str(capacity) + " units daily which is equal to its capacity")
        
        print("Unit with higher value is more consistent than unit with lower value")
        print("================")
          
        for i in range(0, len(self)):
            calculate(self[i].name, self[i].capacity, self[i].productionData) 
        
    if __name__ == '__main__':
        print("Calling calculateConsistency")

#         =======preparing test Data==========
        u1 = UnitData('unit1', 100, [100, 110, 120, 60, 70])
        u2 = UnitData('unit2', 100, [40, 50, 60, 70, 80])
        u3 = UnitData('unit3', 100, [100, 100, 100, 100, 100])
        u4 = UnitData('unit4', 100, [100, 105, 110, 115])
        
        calculateConsistency([u1, u2, u3, u4])
        
      
