from collections import defaultdict
class InventoryAllocator:

    def __init__(self, order, warehouse):
        self.order = order
        self.warehouse = warehouse


    def calculate(self):
        distribution_list = []

        #Loop all warehouse
        for idx in range(len(self.warehouse)):

            name = self.warehouse[idx]['name']
            inventory = self.warehouse[idx]['inventory']
            warehouseDict = defaultdict(dict)

            #Loop all ordered fruit
            for fruit in self.order:

                orderNum = self.order[fruit]

                #If ordered fruits are already been distributed continue
                if orderNum == 0:
                    continue

                #If ordered fruit is in warehouse' inventory -> distribute -> reduce the ordered fruit number(orderNum)
                if fruit in inventory:
                    inventoryNum = inventory[fruit]

                    if inventoryNum >= orderNum:
                        warehouseDict[name][fruit] = orderNum
                        self.order[fruit] = 0

                    elif inventoryNum > 0:
                        warehouseDict[name][fruit] = inventoryNum
                        self.order[fruit] -= inventoryNum

            if len(warehouseDict) != 0:
                distribution_list.append(dict(warehouseDict))

        # print or return answer
        print(distribution_list)
        # return distribution_list




#Examples
ex1 = InventoryAllocator({'apple': 1},
                         [{'name': 'owd', 'inventory': {'apple': 1}}, 
                          ])
ex1.calculate()

ex2 = InventoryAllocator({'apple': 1},
                         [{'name': 'owd', 'inventory': {'apple': 0}}, 
                          ])
ex2.calculate()

ex3 = InventoryAllocator({'apple': 10},
                         [{'name': 'owd', 'inventory': {'apple': 5}},
                          {'name': 'dm', 'inventory': {'apple': 5}} 
                          ])
ex3.calculate()

#Test Case

#exact match 1
ia1 = InventoryAllocator({'apple': 5, 'banana': 5},
                         [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5}},
                          {'name': 'dm', 'inventory': {'apple': 4, 'banana':4}}])
ia1.calculate()

#exact match 2
ia2 = InventoryAllocator({'apple': 5, 'banana': 5},
                         [{'name': 'owd', 'inventory': {'apple': 1, 'banana': 1}},
                          {'name': 'dm', 'inventory': {'apple': 4, 'banana':4}}])
ia2.calculate()

#sum of inventory > order
ia3 = InventoryAllocator({'apple':5, 'banana': 5},
                         [{'name': 'owd', 'inventory': {'apple': 7}}, 
                          {'name': 'dm', 'inventory': {'apple':3}},
                          {'name': 'k', 'inventory': {'banana': 10}}])
ia3.calculate()

#sum of inventory < order
ia4 = InventoryAllocator({'apple': 5, 'banana': 5},
                         [{'name': 'owd', 'inventory': {'apple': 1, 'banana': 1}},
                          {'name': 'dm', 'inventory': {'apple': 3, 'banana':3}}])
ia4.calculate()

#not enough inventory1
ia5 = InventoryAllocator({'banana': 5,'apple':1},
                         [{'name': 'owd', 'inventory': {'banana': 0}}, 
                          {'name': 'dm', 'inventory': {'apple':0}},
                          {'name': 'ko', 'inventory': {'apple': 0}}])
ia5.calculate()

#not enough inventory2
ia6 = InventoryAllocator({'banana': 5,'apple':1},
                         [{'name': 'owd', 'inventory': {'banana': 0}}, 
                          {'name': 'dm', 'inventory': {'apple':0}},
                          {'name': 'ko', 'inventory': {'pineapple': 1}},
                          {'name': 'fr', 'inventory': {'banana': 3}}])
ia6.calculate()




