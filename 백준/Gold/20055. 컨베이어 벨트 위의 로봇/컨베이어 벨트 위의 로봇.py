import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v):
        self.v = v
        self.is_load = False
        self.bf = None
        self.at = None

    def can_load(self):
        return self.v > 0 and not self.is_load

    def unload(self):
        self.is_load = False
    
    def fine_load(self):
        self.v -= 1
        self.is_load = True
        if self.v == 0:
            return False
        else:
            return True


class Link:
    def __init__(self, lst, n):
        nodes = [Node(v) for v in lst]
        self.head = nodes[0]
        self.mid = nodes[n-1]
        self.tail = nodes[-1]
        nodes[0].bf = nodes[-1]
        nodes[-1].af = nodes[0]
        for i in range(len(lst) - 1):
            nodes[i].af = nodes[i+1]
            nodes[i+1].bf = nodes[i]

    def rotate(self):
        self.head = self.tail
        self.mid = self.mid.bf
        self.tail = self.tail.bf


n, remain = map(int, input().split())
nums = list(map(int, input().split()))
belt = Link(nums, n)
rst = 0
robots = []
while remain > 0:
    rst += 1

    belt.rotate()

    new_robots = []
    for robot in robots:
        if belt.mid == robot:
            belt.mid.unload()
            continue
        if robot.af.can_load():
            robot.unload()
            robot = robot.af
            if not robot.fine_load():
                remain -= 1
        if belt.mid == robot:
            belt.mid.unload()
            continue
        new_robots.append(robot)

    if belt.head.can_load():
        if not belt.head.fine_load():
            remain -= 1
        new_robots.append(belt.head)
    robots = new_robots

print(rst)
