import math
from tqdm import tqdm

with open('dataset.txt') as f:
    data = f.readlines()
# print(raw)

monkeys = []
# Starting items: worry level for each item money is holding
# Operation: How worry level changes
# Test: What value decision tree
# what happens of test
# On inspect, /3 rounded down
# Monkey taking a turn is called a round
# A round is inspection, test and throw
# When receiving an item, item goes to end of list
# Read file
# If no items, turn ends
# for line in data:
#     pass
# GOAL:
# Find level of monkey business after 20 rounds. 
# Done by: two active monkeys multiplied

def str_math(old, equation):
    # Going to avoid eval here and do it manually
    pass

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
        ## Step 1, remove string: 
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
        print(f'\tOperation: new = old {self.items}')
        print(f'\tTest: divisible by {self.test}')
        print(f'\t\tIf true: throw to monkey {self.test_pass}')
        print(f'\t\tIf false: throw to monkey {self.test_fail}')
    
    def append_item(self, item):
        self.items.append(item)

    def monkey_business(self):
        # print(f'Monkey {self.number}:')
        if self.items == []:
            return None

        for n in range(len(self.items)):
            current = int(self.items[n])
            # print(f'\tMonkey inspects an item with a worry level of {current}.')
            self.inspections += 1
            # worry_level = int(item)
            op = self.operation[0]
            next_val = 0
            if self.operation[1] == "old":
                next_val = current
            else:
                next_val = int(self.operation[1])
            if op == "+":
                current += next_val
                # self.items[n] = current
                # print(f'\t\tWorry level increases by {next_val} to {current}.')
            elif op == "*":
                current *= next_val
                # self.items[n] = current
                # print(f'\t\tWorry level is multiplied by {next_val} to {current}.')
            current = math.floor((current / 3))
            # self.items[n] = current
            # print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {current}.')
            did_test_pass = (current % int(self.test) == 0)
            if did_test_pass:
                # print(f'\t\tCurrent worry level is not divisible by {self.test}')
                monkeys[int(self.test_pass)].append_item(current)
                # print(f'\t\tItem with worry level {current} is thrown to monkey {self.test_pass}.')
            else:
                # print(f'\t\tCurrent worry level is divisible by {self.test}')
                monkeys[int(self.test_fail)].append_item(current)
                # print(f'\t\tItem with worry level {current} is thrown to monkey {self.test_fail}.')
        self.items = []

def solve():
    counter = 0
    # Create monkey objects
    for line in data:
        # No spaces at start, assume its a new monkey
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
    for monkey in monkeys:
        monkey.print_state()
    print("********************************")
    for i in tqdm(range(20)):
        for monkey in monkeys:
            monkey.monkey_business()

solve()

# print(monkeys)

tmp = []
for monkey in monkeys:
    print(f'Monkey: {monkey.number}: {monkey.inspections}')
    tmp.append(monkey.inspections)
tmp.sort(reverse=True)
print(tmp)
print(tmp[0]*tmp[1])