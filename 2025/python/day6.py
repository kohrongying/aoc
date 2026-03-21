def solve1(filename):
    problems = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            tmp = []
            if line == '':
                continue
            for num in line.split(' '):
                if num == '':
                    continue
                try:
                    tmp.append(int(num))
                except Exception:
                    tmp.append(num)
            problems.append(tmp)
    operators = problems[-1]
    problems = problems[:-1]
    grand_total = 0
    for i, operator in enumerate(operators):
        summ = problems[0][i]
        if operator == '+':
            for j in range(1, len(problems)):
                summ += problems[j][i]
        else:
            for j in range(1, len(problems)):
                summ = summ * problems[j][i]
                
        grand_total += summ
    print(grand_total)
    return grand_total


def solve2(filename):
    problems = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            problems.append(line)
    
    operators = problems[-1]
    problems = problems[:-1]
    grand_total = 0
    start_idx = 0
    end_idx = 0
    for i in range(1, len(operators)):
        if operators[i] in ['+', '*']:
            end_idx = i-1
            operator_str = operators[start_idx:end_idx]
            probs = [p[start_idx:end_idx] for p in problems]
            tmp = compute(probs, operator_str)
            start_idx = i
            grand_total += tmp
            
    # Last one
    operator_str = operators[start_idx:]
    probs = [p[start_idx:] for p in problems]
    tmp = compute(probs, operator_str)
    grand_total += tmp
    print(grand_total)
    return grand_total


"""
problems = ["5432", "543 ", "54 "] // equi length
operator = "*   " len=4 (1+3 space)
"""
def compute(problems: list[str], operator: str)-> int:
    def get_number_at(idx, problems):
        res = ''
        for problem in problems:
            if problem[idx] != ' ':
                res += problem[idx]
        return int(res)
   
    length = len(operator)
    operator = operator[0]
    numbers = [get_number_at(i, problems) for i in range(length-1, -1, -1)]
    summ = numbers[0]
    for n in numbers[1:]:
        if operator == '+':
            summ += n
        else:
            summ *= n
    return summ

