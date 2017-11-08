import sys
import random

#创建文件名
def creatname():
    b = random.randint(0,99999)
    b = ("%05d" %b)
    str1 = '四连环Log-'+ b +'.txt'
    return str1

#把文件设为全局变量
f = open(creatname(), 'w')

#同时输出到屏幕和文件的函数
def _print(*args, sep=' ', end='\n',flush = False):
    line = []
    for value in args:
        line.append(format(value))

    sys.stdout.write(sep.join(line))
    sys.stdout.write(end)
    
    f.write(sep.join(line))
    f.write(end)

    if flush:
        file.flush()
    
#打印棋盘
def print_QP(lista):

    listb = ['1','2','3','4','5','6','7','8']
    _print(' '+' '.join(map(str,listb)))

    for i in range(6):
        line_i = lista[5-i]
        line_i ='|'+ '|'.join(map(str,line_i)) + '|'
        _print(line_i)

    _print('-'*17)
    _print()

def whether_to_stop(lista,x):
    flag = 0
    for i in range(6):                  #i行
        for j in range(8):              #j列
            if lista[i][j] != x :
                continue

            else:

                for k in range(1,5):      #判断行，range设到5是为了完整判断三次，k=1,2,3；当k=4时，因为是接下来一定是‘ ’，直接跳出不会影响判断               
                    if j+k>7 or lista[i][j+k]!=x:
                        break
                if k == 4:
                    flag = 1
                    break

                for k in range(1,5):        #判断列，range同上
                    if  i+k > 5 or lista[i+k][j]!=x:
                        break
                if k == 4:
                    flag = 1
                    break

                for k in range(1,5):        #判断右上对角线
                    if i+k >5 or j+k >7 or lista[i+k][j+k]!=x:
                        break
                if k == 4:
                    flag = 1
                    break

                for k in range(1,5):        #判断左上对角线
                    if i+k >5 or j-k <0 or lista[i+k][j-k]!=x:
                        break
                if k == 4:
                    flag = 1
                    break                

        if flag == 1:
            break
    if flag == 1:
        return 1
    else:
        return 0


def main():

#--------打印规则，初始化棋盘------------------------------------

    _print('''Hi,我是劳拉，我们来玩一局四连环。我用O型棋子，你用X型棋子。
游戏规则：双方轮流选择棋盘的列号放进自己的棋子，
          若棋盘上有四颗相同型号的棋子在一行、一列或一条斜线上连接起来，
          则使用该型号棋子的玩家就赢了!''')
    _print()
    myList = [([' '] * 8) for i in range(6)]

    _print('''开始了！这是棋盘的初始状态：''')
    print_QP(myList)

#----------初始化结束---------------------------------------------

#----------游戏主循环---------------------------------------------
#while条件
    n = 0
    Flag = 0

    while n<=24:
        n+=1

        #电脑放子
        while True:
            a = random.randint(0,7)
            if myList[5][a] == ' ':       #如果该列满了就换一列，直到换到没满的列为止
                break;
            
        _print(">>>轮到我了,我把O棋子放在第%d列..." %(a+1))
        for i in range(6):
            if myList[i][a] == ' ':
                myList[i][a] = 'O'
                break
        print_QP(myList)

        #判断游戏是否结束
        if whether_to_stop(myList,'O') == 1:
            Flag = 1
            break
                    
        #用户放子
        while True:
            b = int(input(">>>轮到你了,你放X棋子,请选择列号(1-8): "))
            f.write(">>>轮到你了,你放X棋子,请选择列号(1-8): %d" %b)
            if b>8 or b<1:
                f.write('\n')
                _print("错误：列号输入超出范围！")
            elif myList[5][b-1] != ' ':
                f.write('\n')
                _print("这列满了，请另选一列...")
            else:
                f.write('\n')
                break

        for i in range(6):
            if myList[i][b-1] == ' ':
                myList[i][b-1] = 'X'
                break
        print_QP(myList)

        #判断游戏是否结束
        if whether_to_stop(myList,'X') == 1:
            Flag = 2
            break

#----------游戏主循环结束----------------------------------------
    if Flag == 1:
        _print("******* 耶，我赢了！^_^")
    elif Flag == 2:
        _print("******* 好吧，你赢了！^_*")
    else:
        _print("******* 难分胜负！@_@")

        
#----------文件关闭----------------------------------------------

    f.close()
   

if __name__=='__main__':
    main()
