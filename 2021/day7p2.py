"""Day 7: The Treachery of Whales"""
def get_fuel_cost(crabs):
    """Now the sum of fuel compsumption can be calculated as sum of arithmetic sequences
    where a1 = 1 and r = 1 and a_n exuals absolute of our crab position substracted from n point
    so we bruteforce every point from lowest crab position to highest as possible answer"""
    fuel_cost = []
    for i in range(min(crabs), max(crabs)):
        fuel_sum = 0
        for j in crabs:
            k = abs(j - i)
            fuel_sum += (1 + k) / 2 * k
        fuel_cost.append(fuel_sum)
    return min(fuel_cost)

def main():
    """Calculating minimal fuel consumption"""
    with open("2021/day7.txt", 'r', encoding='utf-8') as file:
        crabs = (file.readline()).split(",")
        crabs = list(map(int, crabs))
        fuel_needed = get_fuel_cost(crabs)
    print(fuel_needed)

if __name__ == "__main__":
    main()
