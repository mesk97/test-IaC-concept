

def main(str):
    d = ['(', '{', '[']
    pare = {
            ')': '(',
            '}': '{',
            ']': '[' 
    }

    stack = []
    for s in str:
        if s in d:
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            p = stack.pop()
            if pare[s] != p:
                return False
    if len(stack) != 0:
        return False
    return True

if __name__ == "__main__":
    str = "({}())[]()"
    print (bool(main(str)))
