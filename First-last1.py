def  numberslist():
    result_list = list(input("x:\n").split())
    first = result_list[0]
    last = result_list[-1]
    print(result_list)
    return first, last
a, c = numberslist()
print(a,c)