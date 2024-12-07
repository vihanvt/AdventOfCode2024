from itertools import product
def evaluate(nums, ops):
    result = str(nums[0])
    for i in range(len(ops)):
        if ops[i] == "+":
            result = str(int(result) + nums[i + 1])
        elif ops[i] == "*":
            result = str(int(result) * nums[i + 1])
        elif ops[i] == "||":
            result = result + str(nums[i + 1])
    return int(result) 
with open(r"C:\Users\VIHAN\Documents\AOC\2024d7p1.txt") as fob:
    total_result = 0
    for line in fob:
        line = line.strip()
        if ":" in line:
            parts = line.split(":")
            nums = [int(x) for x in parts[1].split()]
            finalnum = int(parts[0])       
        n = len(nums) - 1
        ctr = 0
        for ops in product(["+", "*", "||"], repeat=n):
            if evaluate(nums, ops) == finalnum:
                ctr += 1
        
        if ctr > 0:
            total_result += finalnum
    print("Total Calibration Result:", total_result)
