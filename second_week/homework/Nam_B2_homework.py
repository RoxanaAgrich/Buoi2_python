def dschanle():
    list1 = [1,2,3,4,5]
    list2 = [11,12,13,14,15]
    list3 =[]
    for i in list1:
        if(i % 2 != 0):
            list3.insert(1,i)
    for j in list2:
        if(j % 2 == 0):
            list3.insert(1,j)
    print(list3)
dschanle()

