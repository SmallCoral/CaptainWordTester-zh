#choose_fuctions文件，用来存储选择功能的功能所需要的函数
import change_fuctions

def jsonOrTxt():
    while True :
        print('----------------------------------------------',\
              '选择阅读模式',\
              '按 "a"： Json 模式（程序将读取 Json 文件）',\
              '按 "b"： txt 模式（程序将读取 txt 文件）',\
              '按 "q"： 退出程序',\
              '如果已完成，则应按 "ENTER "键（每次都应在程序中完成）。',sep = '\n')
        judge = input('你的答案是:')
        if judge == 'a':                                    #Json Files
            return 1
        elif judge == 'b':                                  #Txt Files
            return 2
        elif judge == 'q':
            return 3
        else:
            print("您的答案未定义！\n请重新输入！")
            continue

def askDict(Dict):
    '''
    scanCycle函数的必要部分
    '''
    print('选择一个你想要选择的Grope:')
    print('按“q”键返回模式选择。')
    i = 1
    List = change_fuctions.dictToList(Dict)
    for little in List:
        print('%d : %s.' % (i , little[0]))
        i += 1
    while True:                     #判定输入的字符是否合法
        choose = input('输入其ID，然后按“ENTER”:')
        #这个地方使用try的原因：如果输入为非数字（比如按Q键是退出），就会报错。
        try:
            choose = int(choose)
            if choose > 0 and choose <= len(List):
                break
            else:
                print('请核对并输入真实答案!')
                continue
        except:
            if choose == 'q':
                return 'EXIT'
            else:
                print("你的答案没有定义!")
    return List[choose - 1][1]

def testModeChoose():
    while True:
        print('----------------------------------------------------------',\
              '让我们选择你的模式:',\
              '按“a”键:根据翻译猜单词!',\
              '按“b”:翻译单词!',\
              '按“c”:练习!',\
              '按“q”键:中断。',\
              '按“ENTER”确认。',sep = '\n')
        answer = input('你的答案是:')
        if answer == 'a':
            return 1
        elif answer == 'b':
            return 2
        elif answer == 'c':
            return 3
        elif answer == 'q':
            return 'EXIT'
        else:
            print("您的答案未定义！\n请重新输入！")
            continue
