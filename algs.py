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

def fibBaseConverter(other_base):
    new_string = "0"*len(other_base)
    double_zero_pointer = len(other_base) 
    prev_character = "0"
    print("Original String [", other_base, "]")
    for i in range(len(other_base)-1, -1, -1):
        c = other_base[len(other_base) -1 - i]
        print("new string [", new_string, "] i " ,i, "length: ", len(new_string)," double zero pointer [", double_zero_pointer, "]", "other_base[i] = [" , c, "]" )
        if (prev_character == "0" and c == "0"):
            print("in double 0")
            double_zero_pointer= i 
            prev_character = "0"
        elif (prev_character == "1" and c == "1"):
            print("in double one: ",i,  new_string[:i], "0"*(double_zero_pointer - i), "1", new_string[double_zero_pointer +1:])
            new_string = new_string[:i] + "0"*(double_zero_pointer - i) + "1" + new_string[double_zero_pointer +1:] 
            double_zero_pointer= i
            prev_character = "0"
        else:
            print("in regular case: other_base[i] = ["+c+"]", new_string[:i], c, new_string[i+1:])
            print("len: ", len(new_string))
            new_string = new_string[:i] +  c + new_string[i+1:]
            prev_character = c 
            print("len: ", len(new_string))
    return new_string[::-1]

if __name__ == "__main__":
    # u = 138 
    # min_weight_fib_base = getFibBase(u)
    other_base = "111111"#"101010101010100"#"1101100"
    ours = fibBaseConverter(other_base)
    print("Original: [", other_base, "]")
    print("After: [", ours, "]")
    # print(f"u: {u}\n Min-Weight Fibonacci Base: {min_weight_fib_base}")
