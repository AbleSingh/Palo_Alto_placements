def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    brandlist=[]
    brandlist = input().split(" ")
    dict1 = {}
    findCount(x,y,brandlist,dict1)

def maxD(dict):
        Keymax = max(dict, key= lambda x: dict[x])
        return Keymax

def findCount(a,b,brand,dict1): 
    count = 0
    if len(brand) > a:
        return 0
        
    else:
        for i in range(len(brand)):
            brand[i] = int(brand[i])
            
        unq = list(set(brand))
        
        for i in range(len(unq)):
            dict1[unq[i]] = brand.count(unq[i])

        while (b>0):
            n = maxD(dict1)
            count += 1
            b -= dict1[n]

        print(count)

main()