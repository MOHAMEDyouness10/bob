#File:CS112_A1_T2_Game1_20230352
#Year:2024r
#Purpose: 100 game. Two players start from 0 and alternatively add a number from 1 to 10 to the sum. the first who reach 100 wins
#Author: Mohamed Magdy Youness Hamza
#ID:202030352
while True:
    sum = 0
    while sum < 100 :
        print("sum=",sum)
        num1 = int(input('player1 , please choose number from 1 to 10:'))
        if num1  <1 or num1 > 10:
            print('invaild number , please choose another number from 1 to 10')

            continue
        sum += num1
        if sum == 100:
            print("player1 win wRith sum = 100")
            break
        elif sum > 100:
            print("enter another number because sum is more than 100")
            sum -=num1
            continue
        print("sum=",sum)

        num2 = int(input('player 2 , please choose number from 1 to 10:'))
        while  num2 <1 or num2 > 10:
            print('invaild number , please choose another number from 1 to 10')
            break
        sum += num2
        if sum == 100:
            print("player2 win with sum = 100")
            break
        while sum > 100:
            print("enter another number because sum is more than 100")
            sum -= num2
            print("the score is", sum)
            num2 = int(input("player 2,please choose another number"))
            sum +=num2
            if sum == 100:
                print("player 2 is the winner with sum = 100")




