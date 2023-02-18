# https://leetcode.com/problems/generate-parentheses/?envType=study-plan&id=algorithm-ii

# 22. Generate Parentheses
# Medium
# 16.2K
# 630
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


def main(n):
    variants = (n+1)*[None]
    variants[0] = [""]
    variants[1] = ["()"]
    #variants[2] = ["()()", "(())"]
    for i in range(2, n+1):
        #print (i, len(variants[i-1]))
        options = []
        for j in range(0, len(variants[i-1])):
            v = variants[i-1][j]
            options.append("()%s" % (v))
            options.append("(%s)" % (v))
            if j > 0:
                options.append("%s()" % (v))
        variants[i] = options
    return variants[n]

if __name__ == "__main__":
    n = 4
    print(main(n))

["()()()()","(()()())","()(()())","((()()))","(()())()","()()(())","(()(()))","()(())()","()((()))","(((())))","((()))()","()(())()","((())())","(())()()"]
["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]


["()(()())","((()()))","(()())()","()()(())","(()(()))","()(())()","()((()))","((()))()","()(())()","((())())","(())()()"]
["((()()))","((())())","((()))()","(()(()))","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())"]