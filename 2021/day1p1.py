with open("day1.txt", 'r', encoding='utf-8') as f:
    prev = f.readline()
    count = 0
    while True:
        depth = f.readline()
        count = count+1 if depth > prev else count
        prev = depth
        if not depth:
            break

print(count)
