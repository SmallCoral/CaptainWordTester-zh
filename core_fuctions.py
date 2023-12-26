#核心功能函数
import random , time

def askOriginalWords(finalList):
    '''
    根据译义写出原义的模式
    '''
    origins = 0             #原义
    translations = 1        #译义
    questionMEM = 1         #题号
    trueMEM = 0             #正确数
    falseMEM = 0            #错误数
    wrongWords = []         #错误问题的列表的格式：[[fianlList,Your answer],...]
    askedLog = open(".\Datas\log.txt", "a+",encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nDate and Time：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode: A(translation => Origins)\n---------------------------------------------')
    print('=============')
    while True:
        int = random.randint(0,len(finalList) - 1)
        print('问题 %d: %s' % (questionMEM , finalList[int][translations]))
        answer1 = input('你的答案:')
        if answer1 == finalList[int][origins]:
            askedLog.write('\n问题 %d: %s' % (questionMEM, finalList[int][origins]))
            askedLog.write('\n答案: %s  (True)' % answer1)
            askedLog.write('\n-------')
            print('Right''\n-------')
            trueMEM += 1
            questionMEM += 1
            continue
        elif answer1 == 'q':
            print('*************************')
            print('测试结束！以下是测试的结果概要：',\
                  '您可以在日志文件中看到测试的详细信息。')
            print('\tTotleMember: %d\n\tTrueMember: %d \n\tFalseMember: %d ' % (questionMEM - 1,trueMEM , falseMEM))           
            askedLog.write('\nSummarize:'\
                           '\nTotleMember: %d\nTrueMember: %d \nFalseMember: %d ' % (questionMEM - 1,trueMEM , falseMEM))
            if (questionMEM - 1) != 0:          #被除数为0会怎么样呢？
                print('\tCorrect rate: %.4f' % (trueMEM/(questionMEM - 1)))
                askedLog.write('\nCorrect rate: %.4f' % (trueMEM/(questionMEM - 1)))
            askedLog.write('\nWrong Words:')  #错误回答的问题写入到日志中
            for little in wrongWords:
                askedLog.write('\n\t%s %s (Your answer：%s %s)' %
                              (little[0][0] , little[0][1] , little[1][0] , little[1][1]) )
            askedLog.write('\n------The End Line-------\n\n')
            askedLog.close()
            print('=============')
            break
        else:
            print('回答错误!你还有一次机会。')
            answer2 = input()
            if answer2 == finalList[int][origins]:
                print('Right''\n-------')
                questionMEM += 1
                trueMEM += 1
                continue
            else:
                askedLog.write('\n问题 %d: %s' % (questionMEM, finalList[int][origins]))
                askedLog.write('\n答案1: %s (False)' % answer1)
                askedLog.write('\n答案2: %s (False)' % answer2)
                askedLog.write('\n正确答案 : %s' % finalList[int][origins])
                askedLog.write('\n-------')
                print('很遗憾!正确答案是:')
                print(finalList[int][origins])
                print('-------')
                wrongWords.append([finalList[int] , [answer1,answer2]])
                questionMEM += 1
                falseMEM += 1
                continue

def askTranslatedWords(finalList):
    '''
    根据原义写出译义的模式
    '''
    origins = 0
    translations = 1
    questionMEM = 1
    trueMEM = 0
    falseMEM = 0
    unknownMEM = 0          
    wrongQuestions = []
    unknownQuestions = []
    askedLog = open(".\Datas\log.txt", "a+", encoding='utf-8')
    askedLog.write('--------------The Start Line-----------------\nTime：')
    askedLog.write(time.asctime())
    askedLog.write('\nMode: B(Origins => translation)\n-------------------------------------')
    print('=============')
    print('警告:此模式提供的题目为主观题，请自己判断对错。')
    while True:
        int = random.randint(0,len(finalList) - 1)
        print('Question %d: %s ' % (questionMEM , finalList[int][origins]))
        answer1 = input('Your answer：')
        if answer1 == 'q':
            print('*************************')
            print('测试结束。以下是测试结果概要。',\
                  '您可以在日志文件中看到测试的详细信息。')
            print('\tTotleMember: %d\n\tTrueMember: %d\n\tFalseMember: %d\n\tUnknownMember: %d' \
                    % (questionMEM - 1,trueMEM , falseMEM , unknownMEM))
            askedLog.write( '\nSummarize:' \
                            '\nTotleMember: %d\nTrueMember: %d\nFalseMember: %d\nUnknownMember: %d' \
                                 % (questionMEM - 1, trueMEM, falseMEM, unknownMEM))
            if (questionMEM - 1) != 0:                  #被除数为0会怎么样呢？
                print('Correct rate: %.4f' % (trueMEM/(questionMEM - 1)))
                askedLog.write('\nCorrect rate: %.4f' % (trueMEM/(questionMEM - 1)))
            askedLog.write('\n错误回答:')      #错误回答的问题写入到日志中
            for little in wrongQuestions:
                askedLog.write('\n\t%s %s (你的答案是：%s )' % (little[0][0],little[0][1],little[1]))
            askedLog.write('\n未能判断对错的问题:')
            for little in unknownQuestions:             #未能判断对错的问题也应该写入到日志中
                askedLog.write('\n\t%s %s (你的答案是：%s )' % (little[0][0],little[0][1],little[1]))
            askedLog.write('\n------The End Line-------\n\n')
            askedLog.close()
            break
        print('--你的答案已被记录。下面是标准答案。')
        print('--标准答案是：%s' % finalList[int][translations])
        while True:
            answer2 = input('检查你的答案(正确(“y”)错误(“n”)跳过(“ENTER”)):')
            if answer2 == 'y':
                askedLog.write('\n问题 %d: %s' % (questionMEM, finalList[int][origins]))
                askedLog.write('\n答案: %s  (True)' % answer1)
                askedLog.write('\n-------')
                trueMEM += 1
                questionMEM += 1
                print('-------')
                break
            elif answer2 == 'n':
                askedLog.write('\n问题 %d: %s' % (questionMEM, finalList[int][origins]))
                askedLog.write('\n你的答案: %s (False)' % answer1)
                askedLog.write('\n标准答案: %s' % finalList[int][translations])
                askedLog.write('\n-------')
                wrongQuestions.append([finalList[int] , answer1])
                falseMEM += 1
                questionMEM += 1
                print('-------')
                break
            elif answer2 == '':
                askedLog.write('\n问题 %d: %s' % (questionMEM, finalList[int][origins]))
                askedLog.write('\n答案: %s  (未知)' % answer1)
                askedLog.write('\n-------')
                unknownQuestions.append([finalList[int] , answer1])
                unknownMEM += 1
                questionMEM += 1
                print('-------')
                break
            else:
                print('请输入合法的字符！')
                continue
 
def practiceMode(finalList):
    origin = 0
    translation = 1
    questionMEM = 1
    print('=============')
    while True:
        if questionMEM > len(finalList):
            break
        print('单词 %d : %s  %s' % (questionMEM , finalList[questionMEM-1][origin] , finalList[questionMEM-1][translation]))
        print('输入单词: ',end='')
        while True:
            answer = input()
            if answer == finalList[questionMEM - 1][origin]:
                questionMEM += 1
                break
            if answer == 'q':
                break
            else:
                print('输入不一致!请重新输入!')
                continue
        if answer == 'q':
            break
    print('练习结束')
    print('=============')    
