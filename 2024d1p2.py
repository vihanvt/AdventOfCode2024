#solution for problem 2-day 1
def main():
    with open(r"C:\Users\VIHAN\Desktop\2024d1p1.txt") as fob:
        a = [line.strip() for line in fob.readlines()]
        l1 = []
        l2 = []
        for i in a:
            parts = i.split()
            l1.append(int(parts[0]))#left list
            l2.append(int(parts[1]))#right list
        l1.sort()  # arranged in ascending order for left and right lists
        l2.sort()
        similscore = 0
        for i in l1:
            ctr = 0
            for j in l2:
                if i == j:
                    #checking for counting instances
                    ctr += 1
            if ctr > 0:
                print(f"Element {i} found {ctr} times in right list")
                similscore += i * ctr #calculating the similarity score
        print(f"Total similarity score: {similscore}")

main()
