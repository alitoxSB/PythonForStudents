def squares_div3():
    # squares = []
    # for i in range(1,101): #for generates squares of first hundred natural numbers.
    #     if(i**2%3!=0):
    #         squares.append(i**2)
    #     else:
    #         pass
    
    squares = [i**2 for i in range(1,101) if i%3 != 0]
    print(squares)

def mult469():
    mult = [i*4 for i in range(1,2501) if i%6 or i%9]
    print(mult)

if __name__== '__main__':
    # run()
    mult469()