# created: 9:24 2024/8/16
# version 01
# only support numbers containing ONE digit
# does not support ^ (power operator)

opPriority = {"+": 0, "-": 0, "*": 1, "/": 1, "(": -1}

suffixExpr = ""
operatorStack = []
expr = input()  # example: ( 1+  2) *3+4/ 5- 6

for ch in expr:
    if ch >= "0" and ch <= "9":
        suffixExpr += ch
    elif ch == "(":
        operatorStack.append(ch)
    elif ch == ")":
        while operatorStack[-1] != "(":
            suffixExpr += operatorStack[-1]
            operatorStack.pop()
        operatorStack.pop()
    elif ch in opPriority:
        curOpPri = opPriority[ch]
        while len(operatorStack) != 0 and opPriority[operatorStack[-1]] >= curOpPri:
            suffixExpr += operatorStack[-1]
            operatorStack.pop()
        operatorStack.append(ch)

while len(operatorStack) != 0:
    suffixExpr += operatorStack[-1]
    operatorStack.pop()

print("suffix expr: " + suffixExpr)

res = 0
operandStack = []
for ch in suffixExpr:
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
            operandStack.append(op1 / op2)
res = operandStack[0]

print("result: {:.2f}".format(res))
