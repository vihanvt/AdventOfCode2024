def main():
    with open(r"C:\Users\VIHAN\Documents\AOC\2024d14p1.txt") as fob:
        robots = []
        for line in fob:
            a, b = line.strip().split(" ")
            x, y = map(int, a[2:].split(","))  # taking out positions
            vx, vy = map(int, b[2:].split(","))  # taking out velocities
            robots.append({"p": [x, y], "v": [vx, vy]})
        def updater(robots, width, height):
            for robot in robots:
                x, y = robot["p"]
                vx, vy = robot["v"]
                x = (x + vx) % width
                y = (y + vy) % height
                robot["p"] = [x, y]
        width, height = 101, 103
        for _ in range(100):
            updater(robots, width, height)
        quads = [0, 0, 0, 0]
        for robot in robots:
            x, y = robot["p"]
            if x == width // 2 or y == height // 2:
                continue
            qid= (int(x > width // 2)) + (int(y > height // 2) * 2)#checks which part the robot is present
            quads[qid] += 1
        safety_factor = quads[0] * quads[1] * quads[2] * quads[3]
        print(f"Safety Factor: {safety_factor}")
main()
