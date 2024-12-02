def main():
    with open(r"C:\Users\VIHAN\Documents\AOC\2024d2p1.txt") as fob:
        a = [line.strip() for line in fob.readlines()]
        l2 = []
        for i in a:
            num = i.split()
            l2.append([int(j) for j in num])
    ctr = 0
    for i in l2:
        inc = True
        dec = True
        for j in range(len(i) - 1):
            if abs(i[j] - i[j + 1]) not in [1, 2, 3]:
                inc = False
                dec = False
                break
            if i[j] < i[j + 1]:
                inc = True
            if i[j] > i[j + 1]:
                dec = True

        if inc or dec:
            ctr += 1
            

    print(ctr)

main()
