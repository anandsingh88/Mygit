st = 'my NAme is ANANd singh aND TOdaY is MONDAy'

def uprlorcase():
    lcount = 0
    ucount = 0
    """this function calculate the total number of upper and lower case letters by
    using their ASCII values"""

    for itm in st:
        if ord(itm)>=97 and ord(itm)<=122:
            lcount+=1
#            tlcount=lcount
        elif ord(itm)>=65 and ord(itm)<=90:
            ucount+=1
#           tucount=ucount
    print('total upper casr letter',ucount,'totol lower case letter',lcount)

print(uprlorcase())
