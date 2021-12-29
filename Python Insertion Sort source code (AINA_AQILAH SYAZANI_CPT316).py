#AINA SYARAFINA BINTI ROSLAN (148450)
#AQILAH SYAZANI BINTI NOORAZIZ (146410)
f = open('sgb-words.txt', 'r+')
data = f.read().splitlines()

for i in range(1,len(data)):
    key = data[i]
    j=i-1
    while j >=0 and key < data[j]:
        data[j + 1] = data[j]
        j = j -1
    data[j+1] = key
print(data)

f.close()