cycles = 0
registry_val = 1
checkpoints = []

def check_cycle():
    if cycles == 20 or (cycles-20) % 40 == 0:
        checkpoints.append(registry_val * cycles)

with open('dataset.txt') as f:
    raw = f.readlines()
for line in raw:
    line = line.strip()
    if line == "noop":
        cycles += 1
        check_cycle()
    else:
        cycles += 1
        check_cycle()
        cycles += 1
        check_cycle()
        inst, val = line.split(" ")
        registry_val += int(val)

print(checkpoints)
total = 0
for item in checkpoints:
    total += item
print(total)