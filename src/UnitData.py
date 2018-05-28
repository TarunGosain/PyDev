'''
Created on 28-May-2018

@author: tarun1991
'''

class UnitData(object): 
    name = 'default'
    capacity = 100
    productionData = []

    def __init__ (self, name1, capacity1, prodData1):
        self.name = name1
        self.capacity = capacity1
        self.productionData = prodData1