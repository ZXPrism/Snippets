import os

testNum = 1000
ok = 0

for i in range(testNum):
    os.system("python gen.py > data.txt")
    os.system("python bf.py < data.txt > bf.txt")
    os.system("sol < data.txt > sol.txt")

    bf = open("bf.txt")
    sol = open("sol.txt")

    bf_ans = bf.readline()
    sol_ans = sol.readline()

    bf.close()
    sol.close()

    print(f"Test #{i}: ", end="")
    if bf_ans == sol_ans:
        print("PASS")
        ok += 1
    else:
        print("FAIL")
        print(bf_ans, sol_ans)

print(f"** {ok} tests PASSED, {testNum - ok} tests FAILED **")

os.system("rm data.txt")
os.system("rm bf.txt")
os.system("rm sol.txt")
