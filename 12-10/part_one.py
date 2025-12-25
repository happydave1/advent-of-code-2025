
TEST_FILE = './test.txt'
INPUT_FILE = './input.txt'


def parse_line(line):
    line = line.split()
    t = line[0][1:len(line[0]) - 1]
    b = line[1:len(line)-1]

    for i in range(len(b)):
        b[i] = tuple(map(int, b[i][1:len(b[i]) - 1].split(',')))
    return t, b

def fewest_buttons(target, buttons):
    '''
    given a target of form .##.
    where . indicates a light turned off while
    # indicates a light turned on
    and a buttons list of form [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]
    where each button toggles the lights at the index for each button
    return the fewest amt of times needed to get the target formation.
    lights all start off
    '''

    def toggle_lights(cur_lights, cur_button_ind):
        button = buttons[cur_button_ind]
        new_lights = cur_lights.copy()
        for i in button:
            new_lights[i] = not new_lights[i]
        return new_lights

    fewest = float('inf')
    temp = []
    for i in range(len(target)):
        if target[i] == '#':
            temp.append(True)
        else:
            temp.append(False)
    target = temp
    
    def helper(cur_lights, buttons_pressed, cur_button_ind):
        nonlocal fewest

        if cur_button_ind == len(buttons):
            if cur_lights == target:
                fewest = min(fewest, len(buttons_pressed))
            return
        
        if len(buttons_pressed) >= fewest:
            return
        
        # consider current button pressed
        helper(toggle_lights(cur_lights, cur_button_ind), buttons_pressed + [buttons[cur_button_ind]], cur_button_ind + 1)

        # consider current button not pressed
        helper(cur_lights, buttons_pressed, cur_button_ind + 1)
    
    helper([False for _ in range(len(target))], [], 0)
    return fewest
    

sol = 0
with open(INPUT_FILE, 'r') as file:

    for line in file:
        target, buttons = parse_line(line.strip())
        sol += fewest_buttons(target, buttons)
print(sol)