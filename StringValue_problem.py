a = input()
aList = list(a)
valueList = input().split(" ")
for i in range(len(valueList)):
            valueList[i] = int(valueList[i])     

dict1 = {}
dict2 = {}

for i in range(len(valueList)):
            if aList[i] not in dict1:
                dict1[aList[i]] = []
                dict1[aList[i]].append(valueList[i])
            else:
                dict1[aList[i]].append(valueList[i])
                
        
for i in range(len(dict1)):
    if len(dict1[aList[i]]) > 1:
        dict2[aList[i]] = dict1[aList[i]]
        
sum = 0

for i in dict2:
    sum += min(dict2[i])

print(dict2)
print(sum)