from knapsack_obj_class import knapsack_obj

def main_knapsack_obj():

    northface = knapsack_obj(4,[1,2,3,4],[1,1,5,1])

    print('The capacity is ', northface.capacity)
    print('The objects are ', northface.objects)
    print("Is it empty? ", northface.isempty())
    print("The weight is ", northface.weight())

    northface.new_cap(8)
    print("The remaining capacity is ", northface.rem_cap())
    northface.add_elts([[5,6,7],[3,8,1]])
    print("The remaining capacity is ", northface.rem_cap())
    print("The weight is ", northface.weight())
    print('The objects are ', northface.objects)
    print('The values are ',northface.obj_values())
    print('The weights are ',northface.obj_weights())

    print("The biggest object is ", northface.greatest())
    print("The smallest object is ", northface.lowest())

    print("Is it empty? ", northface.isempty())
    print("Is it full? ", northface.isfull())

    northface.new_cap(7)
    print("Is it full? ", northface.isfull())

    northface.empty()
    print("Is it empty? ", northface.isempty())

    print('The capacity is ', northface.capacity)
    print('The objects are ', northface.objects)


main_knapsack_obj()