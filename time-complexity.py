import datetime

#新建一个表，包含从0至10000*n-1，四种不同函数的时间复杂度

def test1(n):
    lst=[]
    for i in range(n*10000):
        lst = lst + [i]
    return  lst

def test2(n):
    lst=[]
    for i in range(n*10000):
        lst.append(i)
    return  lst

def test3(n):
    return  [i for i in range(n*10000)]

def test4(n):
    return  list(range(n*10000))


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    n = 2 #20
    test1(n) #00.684597 04:36.805679
    test2(n) #00.001999  00.027983
    test3(n) #0.000999 00.014982
    test4(n) #0.000000 00.007993
    endtime = datetime.datetime.now()
    print(endtime - starttime)
