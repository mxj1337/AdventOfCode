#three-measurement sliding window

with open("day1.txt", 'r', encoding='utf-8') as f:
    adv = []
    while True:
        line = f.readline()
        adv.append(line)
        if not line:
            break

sumadv = []
for a in range(len(adv)-3):
    sum3 = int(adv[a])+int(adv[a+1])+int(adv[a+2])
    sumadv.append(sum3)

count = 0
for a in range(1,len(sumadv)):
    if sumadv[a]>sumadv[a-1]:
        count=count+1

print(count)
