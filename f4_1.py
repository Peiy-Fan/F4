from random import randint
from random import choice
ops = ['+','-','*','/']
bra = ['(', '', ')']
#com = input('>') #用户输入
cot = 0 #答对的题
x = 0
while x < 20 :
    s1 = randint(1,10)
    s2 = randint(1,10)
    s3 = randint(1,10)
    s4 = randint(1,10)
    op1 = choice(ops) #随机运算符
    op2 = choice(ops)
    op3 = choice(ops)
    """括号"""
    bra_1 = ['' , '' ,'']
    bra_2 = ['' , '' , '']
    i = ii =0
    while (i ==0 and ii ==2) or abs(i-ii)==1 \
        or ii < i  :
        i = randint(0,2)
        ii = randint(0,2)

    bra_1[i] = '(';   bra_2[ii]=')'

    while op1 == op2 == op3 :
        op1 = choice(ops) #随机运算符
        op2 = choice(ops)
        op3 = choice(ops)

    eq = bra_1[0] + str(s1) + op1 + bra_1[1] + str(s2) + \
    bra_2[0] + op2 + bra_1[2] + str(s3) + bra_2[1] + op3 \
    + str(s4) + bra_2[2]
    res = eval(eq) 
    if len(str(res) ) > 5:
        continue
    x += 1
    print(eq)
    print("?")
    in_res=eval(input())
   # in_res =eval( input('?'))
    if in_res == res:
        print('算对啦，你真是个天才！')
        cot += 1
    else:
        print('再想想吧，答案似乎是%s喔！'%res)

print('你一共答对%s道题，共20道题'%cot)