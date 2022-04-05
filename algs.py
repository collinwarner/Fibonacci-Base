lookup = {}
def F(u):
    # get the largest fibonacci number < u. At least O(n) on u length, possibly O(log n) with memoization
    #if (u in lookup):
    #    return lookup[u]
    a_0 = 0
    if (u == a_0):
        return a_0, 0
    a_1 = 1
    #if (u == a_1):
    #    return a_1, 2 #any one will be in index 2 spot 

    index = 2
    while (a_1 + a_0  <= u):
        temp = a_1
        a_1 = a_0 + a_1
        a_0 = temp
        #print(a_1)
        index+= 1
    #need an optimal way of storing/looking up ranges
    return a_1, index
def getFibBase(u):
    # Convert a number to a fibonacci base representation
    S = ""
    F_i, i = F(u)
    m = u - F_i
    #print(f"F_i = {F_i}, i = {i}, m = {m}")
    if (m == 0):
        if (i == 0):
            return "0" 
        S = S + "1" 
        for j in range(i, 1, -1):
            S = S + "0"
            i -= 1
        return S
    S = S + "1"
    F_i, n_i = F(m)
    for j in range(i, n_i+1, -1):
        S = S + "0"
        i -= 1
    return S + getFibBase(m)
if __name__ == "__main__":
    u = 138 
    min_weight_fib_base = getFibBase(u)
    print(f"u: {u}\n Min-Weight Fibonacci Base: {min_weight_fib_base}")
