import re

def main():
    with open(r"C:\Users\VIHAN\Documents\AOC\2024d13p1.txt") as fob:
        a = fob.read()
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
        claws = re.findall(pattern, a)
        total_cost = 0
        
        for claw in claws:
            xa, ya, xb, yb, px, py = map(int, claw)
            cost = solve(xa, ya, xb, yb, px, py)
            if cost != -1:
                total_cost += cost
        
        print(f"Total cost to win all possible prizes: {total_cost} tokens")

def solve(xa, ya, xb, yb, px, py):
    #make equations for 1)a*xa+b*yb=px 2) a*ya+ b*yb=py solve these simultaneously
    b = (px * ya - py * xa) / (xb * ya - xa * yb)
    a = (px - b * xb) / xa
    if int(a) != a or int(b) != b:
        return -1
    if a > 100 or b > 100 or b < 0:
        return -1
    return 3 * int(a) + int(b)

main()
