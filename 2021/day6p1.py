"""Day 6: Lanternfish"""
from collections import Counter

def simulate_shoal(mycnt, days):
    """Simulating lanterfish shoal growth"""
    for _ in range(days):
        tmpcnt = mycnt.copy()
        mycnt[0] = tmpcnt[1]
        mycnt[1] = tmpcnt[2]
        mycnt[2] = tmpcnt[3]
        mycnt[3] = tmpcnt[4]
        mycnt[4] = tmpcnt[5]
        mycnt[5] = tmpcnt[6]
        mycnt[6] = tmpcnt[7] + tmpcnt[0]
        mycnt[7] = tmpcnt[8]
        mycnt[8] = tmpcnt[0]
    return mycnt

def main():
    """Calculating amount of lanternfishes"""
    with open("2021/day6.txt", 'r', encoding='utf-8') as file:
        lanternfishes = (file.readline()).split(",")
        lanternfishes = list(map(int, lanternfishes))
        cnt = Counter(lanternfishes)
        mycnt = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for key in mycnt:
            mycnt[key] += cnt[key]
    simulated = simulate_shoal(mycnt, 256)
    lantern_count = 0
    for key in simulated:
        lantern_count += simulated[key]
    print(lantern_count)
if __name__ == "__main__":
    main()
