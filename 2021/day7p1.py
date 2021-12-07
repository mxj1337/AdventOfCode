"""Day 7: The Treachery of Whales"""
import statistics

def main():
    """In 1-dimensional case this example can be simplfied to the median of those points."""
    with open("2021/day7.txt", 'r', encoding='utf-8') as file:
        crabs = (file.readline()).split(",")
        crabs = list(map(int, crabs))
        median = statistics.median(crabs)
        fuel_needed = 0
        for i in crabs:
            fuel_needed += abs(i - median)

    print(median, fuel_needed)

if __name__ == "__main__":
    main()
    