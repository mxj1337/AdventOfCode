"""Using thee-measurments counts how many times does the depth increased"""
def main():
    """three-measurement sliding window"""
    with open("2021/day1.txt", 'r', encoding='utf-8') as file:
        adv = []
        while True:
            line = file.readline()
            adv.append(line)
            if not line:
                break

    sumadv = []
    for i in range(len(adv)-3):
        sum3 = int(adv[i])+int(adv[i+1])+int(adv[i+2])
        sumadv.append(sum3)

    count = 0
    for i in range(1, len(sumadv)):
        if sumadv[i] > sumadv[i-1]:
            count = count+1

    print(count)
if __name__ == "__main__":
    main()
    