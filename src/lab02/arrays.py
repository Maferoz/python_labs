def min_max(x):
    if not x: # Пустой список = False
        raise ValueError()
    min = x[0]
    max = x[0]
    print(max,min)
    for i in x:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

x1 = [3, -1, 5, 5, 0]
x2 = [42]
x3 = [-5, -2, -9]
x4 = []
x5 = [1.5,2,2.0,-3.1]
#print(min_max(x5))
def unique_sorted(x):
    unique_x = []
    for i in x:
        if i not in unique_x:
            unique_x.append(i)
    for i in range(len(unique_x)):
        for u in range(len(unique_x)-i-1):
            if unique_x[u] > unique_x[u+1]:
                unique_x[u], unique_x[u+1] = unique_x[u+1], unique_x[u]
    return unique_x
x1 = [3,1,2,1,3]
x2 = []
x3 = [-1,-1,0,2,2]
x4 = [1.0,1,2.5,2.5,0]
#print(unique_sorted(x4))

def flatten(x):
    res = []
    for i in x:
        if type(i) != tuple and type(i) != list:
            raise ValueError()
        res.extend(i)
    return res
x1 = [[1,2],[3,4]]
x2 = [[1,2],(3,4,5)]
x3 = [[1],[],[2,3]]
x4 = [[1,2],"ab"]
print(flatten(x4))
                       


    


