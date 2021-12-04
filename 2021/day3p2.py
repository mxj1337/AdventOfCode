"""Veryfing life support rating"""
def get_rating_value(lines, index, what):
    """"Calculating the most/least common bit of the list with the given index
    untill the rating value is found"""
    if len(lines) > 1:
        bit_we_are_looking_for = 0
        for line in lines:
            bit_we_are_looking_for += int(line[index])
        if what == "Oxygen":
            bit_we_are_looking_for = 1 if bit_we_are_looking_for >= (len(lines) / 2) else 0
        if what == "CO2":
            bit_we_are_looking_for = 0 if bit_we_are_looking_for >= (len(lines) / 2) else 1

        newlines = []
        for line in lines:
            if int(line[index]) == bit_we_are_looking_for:
                newlines.append(line)
        return get_rating_value(newlines, index + 1, what)
    else:
        return lines[0]

def main():
    """Calculating Life Support Rating for submarine"""
    with open("2021/day3.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    oxygen_generator_rating = int(get_rating_value(lines, 0, "Oxygen"), 2)
    co2_scrubber_rating = int(get_rating_value(lines, 0, "CO2"), 2)
    #get_rating_value returns string containing binary number, we need to change it to decimal
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(life_support_rating)

if __name__ == "__main__":
    main()
    