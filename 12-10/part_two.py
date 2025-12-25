from collections import deque

TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'

def parse_line(line: str):
    line = line.split()
    joltage = list(map(int, tuple(line[-1][1:len(line[-1])-1].split(','))))
    buttons = line[1:len(line)-1]

    for i in range(len(buttons)):
        buttons[i] = tuple(map(int, buttons[i][1:len(buttons[i]) - 1].split(',')))
    return buttons, joltage

# def fewest_buttons(buttons, joltage):

#     def is_over(cur_joltage):
#         for i, j in enumerate(cur_joltage):
#             if joltage[i] < j:
#                 return True
#         return False
    
#     def add_joltage(b_ind, cur_j):
#         b = buttons[b_ind]
#         temp = cur_j.copy()
#         for i in b:
#             temp[i] += 1
#         return temp
    
#     fewest = float('inf')
#     memo = set()
#     def helper(cur_joltage, cur_button_ind, total_pressed):
#         nonlocal fewest

#         if cur_joltage == joltage:
#             fewest = min(fewest, total_pressed)
#             return

#         if cur_button_ind == len(buttons) or is_over(cur_joltage):
#             return
        
#         if total_pressed >= fewest:
#             return
        
#         state = (tuple(cur_joltage), cur_button_ind)
#         if state in memo:
#             return
#         memo.add(state)

#         # consider pressing button and staying on the button
#         helper(add_joltage(cur_button_ind, cur_joltage), cur_button_ind, total_pressed + 1)

#         # consider not pressing button and continuing
#         helper(cur_joltage, cur_button_ind + 1, total_pressed)

#     helper([0 for _ in range(len(joltage))], 0, 0)
#     return fewest

from z3 import Int, Optimize, Sum, sat

def fewest_buttons_z3(buttons, target):
    num_buttons = len(buttons)
    num_dims = len(target)

    x = [Int(f"x{j}") for j in range(num_buttons)]

    opt = Optimize()

    # adding constraints
    for xi in x:
        opt.add(xi >= 0)

    for i in range(num_dims):
        opt.add(
            Sum([
                x[j] for j in range(num_buttons)
                if i in buttons[j]
            ]) == target[i]
        )

    opt.minimize(Sum(x))

    opt.check()
    model = opt.model()
    return sum(model[xi].as_long() for xi in x)

sol = 0
with open(INPUT_FILE, 'r') as file:
    for line in file:
        buttons, joltage = parse_line(line.strip())
        print(buttons, joltage)
        sol += fewest_buttons_z3(buttons, joltage)
print(sol)