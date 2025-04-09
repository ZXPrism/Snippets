# created: 15:25 2025/04/07 by ZXPrism
# https://tieba.baidu.com/p/9626722373

from rich import print


# 计算后缀表达式结果
def EvalRPN(rpn: str) -> int:
    operandStack = []
    for ch in rpn:
        if ch >= "0" and ch <= "9":
            operandStack.append(ch)
        else:
            op2 = float(operandStack[-1])
            operandStack.pop()
            op1 = float(operandStack[-1])
            operandStack.pop()

            if ch == "+":
                operandStack.append(op1 + op2)
            elif ch == "-":
                operandStack.append(op1 - op2)
            elif ch == "*":
                operandStack.append(op1 * op2)
            elif ch == "/":
                if op2 == 0:
                    return float("nan")
                operandStack.append(op1 / op2)
    return operandStack[0]


# 后缀表达式转中缀表达式
def RPN2InfixExpr(rpn: str) -> str:
    exprStack = []
    for ch in rpn:
        if ch >= "0" and ch <= "9":
            exprStack.append(ch)
        else:
            op2_str = exprStack[-1]
            exprStack.pop()

            op1_str = exprStack[-1]
            exprStack.pop()

            if ch == "+":
                exprStack.append(f"({op1_str} + {op2_str})")
            elif ch == "-":
                exprStack.append(f"({op1_str} - {op2_str})")
            elif ch == "*":
                exprStack.append(f"({op1_str} * {op2_str})")
            elif ch == "/":
                exprStack.append(f"({op1_str} / {op2_str})")
    return "".join(exprStack)


# 生成素数
N = 100
primes = []
spf = [i for i in range(N + 1)]
for i in range(2, N + 1):
    if spf[i] == i:
        primes.append(i)
    for p in primes:
        if i * p > N:
            break
        spf[i * p] = p
        if i % p == 0:
            break

# 存储概率分布
result = {}

# 遍历所有可能的 k
for k in range(2, 3):
    # 目标素数
    target = primes[3 * k - 2 : 3 * k + 1]

    # 设定投掷次数 j 的上下限
    lower, upper = 2, (2 * k if k < 9 else 20)

    # 遍历所有可能的骰子面数 i
    for face_num in [6]:
        for throw_time in [4]:
            curr_comb = [0] * throw_time
            tot, ok_cnt = 0, 0

            def dfs(k: int):
                global tot

                if k == throw_time:
                    tot += 1

                    expr = []

                    # 检查所有可能的表达式组合（为了提高效率，一旦找到合法表达式就结束搜索）
                    def CheckAllExprs(digit: int, sign: int) -> bool:
                        if sign == throw_time - 1:
                            if EvalRPN(expr) in target:
                                # print(f"{RPN2InfixExpr(expr)}")
                                return True
                        if digit < throw_time:
                            expr.append(str(curr_comb[digit - 1]))
                            if CheckAllExprs(digit + 1, sign):
                                return True
                            expr.pop()
                        if digit > sign + 1:
                            for op in ["+", "-", "*", "/"]:
                                expr.append(op)
                                if CheckAllExprs(digit, sign + 1):
                                    return True
                                expr.pop()
                        return False

                    if CheckAllExprs(0, 0):
                        print(curr_comb)
                        global ok_cnt
                        ok_cnt += 1

                    return
                for i in range(1, face_num + 1):
                    curr_comb[k] = i
                    dfs(k + 1)

            # 生成所有可能的投掷结果，并判断该结果是否合法（存在至少一种表达式，使其结果为目标素数）
            dfs(0)

            # 记录结果
            result[(k, face_num, throw_time)] = ok_cnt / tot

print(result)
