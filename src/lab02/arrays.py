def min_max(x):
    if not x:
        raise ValueError()
    min = x[0]
    max = x[0]
    for i in x:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

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

def flatten(x):
    res = []
    for i in x:
        if type(i) != tuple and type(i) != list:
            raise ValueError()
        res.extend(i)
    return res

                       


    



