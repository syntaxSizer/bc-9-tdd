#/usr/bin/python
def super_sum(*args):
    '''
    it takes in elements 
    in a list and returns
    total  sum
    '''

    total = 0 #initialize the total for elements in a list
    float_ = 0.0
#loop through each element 
    for ele in args: 
        if isinstance(ele,list): #test if the element is a list
            for i in ele:
                if isinstance(i, int):
                    total = i + total # adds the elements in an individual list
                elif isinstance(i, float):
                    float_num = i + float_num
                else:
                    return ' You have entered a non integer'
        else:
            if type(ele) is int: #test if the element passed is an integer
                total += ele
            else:
                return 'you entered a non integer item'

    super_sum = float_ + total
    return super_sum

print super_sum([5,6], 7)