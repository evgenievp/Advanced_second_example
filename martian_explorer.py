matrix = []
you_r, you_c = 0, 0

for i in range(6):
    row = input().split()
    matrix.append(row)
    for c in range(len(row)):
        if row[c] == "E":
            you_r, you_c = i, c

commands = input().split(", ")

def is_valid(r, c):
    return 0 <= r < 6 and 0 <= c < 6


metal, concrete, water = 0, 0, 0
end = False


def do(metal, concrete, water, end, matrix, you_r, you_c):
    if matrix[you_r][you_c] == "W":
        water += 1
        print(f"Water deposit found at ({you_r}, {you_c})")
    elif matrix[you_r][you_c] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({you_r}, {you_c})")
    elif matrix[you_r][you_c] == "M":
        metal += 1
        print(f"Metal deposit found at ({you_r}, {you_c})")
    elif matrix[you_r][you_c] == "R":
        end = True
        print(f"Rover got broken at ({you_r}, {you_c})")
    return metal, concrete, water, end

for dir in commands:
    if dir == "down":
        if is_valid(you_r + 1, you_c):
            you_r += 1
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
        else:
            you_r = 0
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
    elif dir == "up":
        if is_valid(you_r - 1, you_c):
            you_r -= 1
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
        else:
            you_r = 5
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
    elif dir == "left":
        if is_valid(you_r, you_c - 1):
            you_c -= 1
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
        else:
            you_c = 5
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
    elif dir == "right":
        if is_valid(you_r, you_c + 1):
            you_c += 1
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
        else:
            you_c = 0
            metal, concrete, water, end = do(metal, concrete, water, end, matrix, you_r, you_c)
    if end:
        break

if metal >= 1 and concrete >= 1 and water >= 1:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")