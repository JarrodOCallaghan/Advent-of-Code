import math
from tqdm import tqdm
import numpy as np
from functools import reduce
import operator

with open('dataset.txt') as f:
    data = f.readlines()
monkeys = []

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

class Monkey:
    def __init__(self, number: int):
        print(f'\n{number}')
        self.number = number
        self.items = None
        self.operation = None
        self.test = None
        self.test_pass = None
        self.test_fail = None
        self.inspections = 0

    def set_items(self, items_str: str):
        items_str = items_str.replace("  Starting items: ","")
        items = items_str.strip().split(", ")
        self.items = [int(i) for i in items]
    
    def set_operation(self, op_string: str):
        op_string = op_string.replace("  Operation: new = old ","")
        self.operation = op_string.strip().split(" ")
    
    def set_test(self, test_str: str):
        test_str = test_str.replace("  Test: divisible by ","")
        self.test = test_str.strip()

    def set_test_pass(self, pass_str: str):
        pass_str = pass_str.replace("    If true: throw to monkey ","").strip()
        self.test_pass = int(pass_str)

    def set_test_fail(self, fail_str: str):
        fail_str = fail_str.replace("    If false: throw to monkey ","").strip()
        self.test_fail = int(fail_str)

    def print_state(self):
        print(f'Monkey: {self.number}')
        print(f'\tStarting items: {self.items}')
        print(f'\tOperation: new = old {self.operation}')
        print(f'\tTest: divisible by {self.test}')
        print(f'\t\tIf true: throw to monkey {self.test_pass}')
        print(f'\t\tIf false: throw to monkey {self.test_fail}')
    
    def append_item(self, item):
        self.items.append(item)

    def monkey_business(self, mod_prod):
        if self.items == []:
            return None

        for n in range(len(self.items)):
            current = int(self.items[n])
            self.inspections += 1
            op = self.operation[0]
            mod = int(self.test)
            next_val = current if self.operation[1] == "old" else int(self.operation[1])

            if op == "+":
                current = current + next_val
            elif op == "*":
                current = current * next_val
            current = current % mod_prod

            if current % int(self.test) == 0:
                monkeys[int(self.test_pass)].append_item(current)
            else:
                monkeys[int(self.test_fail)].append_item(current)
        self.items = []

def solve():
    counter = 0
    for line in data:
        if line[0] != " " and line[0] != "\n":
            monkey = Monkey(counter)
            monkeys.append(monkey)
            counter += 1
        if "Starting" in line:
            monkeys[counter-1].set_items(line)
        if "Operation" in line:
            monkeys[counter-1].set_operation(line)
        if "Test" in line:
            monkeys[counter-1].set_test(line)
        if "true" in line:
            monkeys[counter-1].set_test_pass(line)
        if "false" in line:
            monkeys[counter-1].set_test_fail(line)
    mod_prod = 1
    for monkey in monkeys:
        print(f'Monkey Divisor {monkey.test}')
        mod_prod *= int(monkey.test)
    print("********************************")
    for i in tqdm(range(10000)):
        for monkey in monkeys:
            monkey.monkey_business(mod_prod)

solve()

tmp = []
for monkey in monkeys:
    print(f'Monkey: {monkey.number}: {monkey.inspections}')
    tmp.append(monkey.inspections)
tmp.sort(reverse=True)
print(tmp)
print(tmp[0]*tmp[1])