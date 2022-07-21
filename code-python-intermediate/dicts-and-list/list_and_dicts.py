def superlistandsuperdict():
    my_list = [25, 'Garcia',5.5]
    my_dict = {"firstname":"Alejandro", "lastname":"Zamora"}

    superlist = [
        {"firstname":"Alejandro", "lastname":"Zamora"},
        {"firstname":"Carlos", "lastname":"Zelaya"},
        {"firstname":"Miguel", "lastname":"Torres"},
        {"firstname":"Melvin", "lastname":"Doo"},
        {"firstname":"Scrapy", "lastname":"Doo"},
    ]

    superdict = {
        "naturalNums":[1,2,3,4,5],
        "intNums":[-1,-2,-3,0,4,5,6],
        "floatNums":[1.2,4.3,5.6,7.7]
    }

    for key,value in superdict.items(): #easy method for superdictionary
        print(key,"-",value)
    
    for i in range(len(superlist)):
        print(superlist[i])

if __name__== '__main__':
    superlistandsuperdict()