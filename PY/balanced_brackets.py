def balancedBrackets(string):
    stack = []
    pipes = 0
    brackets = {'[': ']', '(': ')', '{': "}", '|': '|'}
    for s in string:
        if s in brackets:
            if s == '|':
                pipes += 1
                if pipes % 2 == 0 and brackets[stack[-1]] == s:
                    stack.pop()
                    continue
            stack.append(s)
            continue
        if s not in brackets.values():
            continue
        print(f"s = {s}, stack = {stack}")
        if brackets[stack[-1]] == s:
            stack.pop()
        else:
            return 0
    return 1


print(balancedBrackets('Hel{lo}'))
print(balancedBrackets('{{||[]||}}'))
print(balancedBrackets('i (wa)n {t to buy a on}esie[...]'))
print(balancedBrackets('()[]{}{'))
