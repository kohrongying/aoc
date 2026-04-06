import re

def read_input(filename) -> list[tuple[int,int]]:
    input = []
    pattern = r"[\(\{\[](.*?)[\)\}\]]"
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            res = re.findall(pattern, line)
            input.append({
                'indicator': res[0],
                'buttons': [x.split(',') for x in res[1:-1]],
                'joltage': res[-1].split(',')
            })
    return input

def solve1(filename):
    input = read_input(filename)
    count = 0
    for inp in input:
        indicator = inp['indicator']
        buttons = inp['buttons']
        presses = get_min_button_presses(indicator, buttons)
        count += presses or 0
        print('presses', presses)
    print('ANSWER', count)
    
    
def get_min_button_presses(final_indicator, buttons):    
    min_press = 999999
    start = '.' * len(final_indicator)
    all_buttons = len(buttons)
    min_press_map = { start : 0 }
    queue = [(start, buttons)]
    while queue:
        curr_indicator_state, remaining = queue.pop(0)
        if len(remaining) > 0:
            for i, btn in enumerate(remaining):
                new_indicator = get_new_indicator(curr_indicator_state, btn)
                
                # if new indicator is same as final, then dont add to queue
                if new_indicator == final_indicator:
                    min_press = min(min_press, all_buttons - len(remaining) + 1)
                    continue
                
                # store in min press map. if current val is not better than what i have in
                # min press map then dont add to queue
                if new_indicator in min_press_map:
                    if all_buttons - len(remaining) + 1 >= min_press_map[new_indicator]:
                        continue
                    else:
                        min_press_map[new_indicator] = all_buttons - len(remaining) + 1 
                else:
                    min_press_map[new_indicator] = all_buttons - len(remaining) + 1
                
                # add to queue
                queue.append((new_indicator, remaining[:i] + remaining[i+1:]))
        
            
    return min_press
            
def get_new_indicator(old_indicator: str, btn: list[str]) -> str:
    newind = ''
    for i in range(len(old_indicator)):
        if str(i) in btn:
            newind += '.' if old_indicator[i] == '#' else '#'
        else:
            newind += old_indicator[i]
    return newind
      
assert get_new_indicator('....', ['3']) == '...#'
assert get_new_indicator('#...', ['0', '3']) == '...#'

