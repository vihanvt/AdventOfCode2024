#solution for problem 1- day 1
def main():
    with open(r"C:\Users\VIHAN\Desktop\2024d1p1.txt")as fob:
        a=[line.strip()for line in fob.readlines()]
        l1=[]
        l2=[]
        for i in a:
            parts=i.split()
            l1.append(int(parts[0]))
            l2.append(int(parts[1]))
        # print(l1)
        # print("_________________________________________________________________________________________________________________________")
        # print(l2)
        #finding smallest in l1 and l2
        l1.sort()#arranged in ascending order
        l2.sort()
        pairs=[]
        for i in range(len(l1)):
            pairs.append((l1[i], l2[i]))
        print("Mapped pairs:")
        diff=0
        sum=0
        for pair in pairs:
            diff=abs(pair[0]-pair[1])
            print(f"Difference for pair {pair}: {diff}")
            sum+=diff
        print("_________________________________________________________________________________________________________")
        print("The answer for problem 1 is : ",sum)



main()