class knapsack_obj:

#this is to define a knapsack, that has a capacity and can be filled with objects, that are couples [value of the obj, weight of the obj]

    #to initialize capacity and the objects to put inside
    def __init__(self, capacity, values, weights):  
        self.capacity = capacity
        self.objects = []
        if len(values)==len(weights):
            for i in range(0, len(weights)):
                if self.weight()+weights[i] > self.capacity or weights[i]<=0:
                    print('Invalid object at index ', i)
                else:
                    self.objects.append([values[i],weights[i]])
        elif len(values)>len(weights):
            print("Invalid input lenght: more values then weights")
        elif len(values)<len(weights):
            print("Invalid input lenght: more weights then values")

    
    #to empty the knapsack
    def empty(self):  
        self.objects.clear()

    #to modify the capacity
    def new_cap(self,new):   
        if self.weight()>new:
            print('Invalid capacity')
        else:
            self.capacity = new

    #to add elements as a list of [[new values], [new weights]]
    def add_elts(self,elts):
        if len(elts[0])==len(elts[1]):
            l=len(elts[0])
            for i in range(0,l):
                if elts[1][i] <= self.rem_cap() and elts[1][i]>0:
                    self.objects.append([elts[0][i],elts[1][i]])
                else:
                    print('Invalid object at index ', i)
        elif len(elts[0])>len(elts[1]):  
            print("Invalid input lenght: more values then weights")
        elif len(elts[0])<len(elts[1]):
            print("Invalid input lenght: more weights then values")

    #to have the list of the weights
    def obj_weights (self):
        weights = []
        for i in range(0,len(self.objects)):
            weights.append(self.objects[i][1])
        return weights

    #to have the list of the values
    def obj_values (self):
        values = []
        for i in range(0,len(self.objects)):
            values.append(self.objects[i][0])
        return values
    
    #to have the element with the greates weight
    def greatest(self):
        i = self.obj_weights().index(max(self.obj_weights()))
        return self.objects[i]
    
    #to have the element with the lowest weight
    def lowest(self):
        i = self.obj_weights().index(min(self.obj_weights()))
        return self.objects[i]
    
    #to have the element with the greatest value
    def greatest_value(self):
        i = self.obj_values().index(max(self.obj_values()))
        return self.objects[i]
    
    #to have the element with the lowest value
    def lowest_value(self):
        i = self.obj_values().index(min(self.obj_values()))
        return self.objects[i]
    
    #to return the remaining capacity
    def rem_cap(self):
        return self.capacity - self.weight()
    
    #to have the weight of the knapsack
    def weight(self):
        w = 0
        if self.isempty() == False:
            for i in range(0,len(self.objects)):
                w += self.objects[i][1]
        return w
    
    def isempty(self):
        if len(self.objects)>0:
            return False
        else:
            return True
        
    def isfull(self):
        if self.rem_cap() == 0:
            return True
        else:
            return False


