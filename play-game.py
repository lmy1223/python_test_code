import random

def play_game(num):
    while True:
        a = int(raw_input("Please input a number: "))
        if a > num :
            print "太大了！"
        elif a < num :
            print "太小了！"
        else :
            print "正确！"
            break


def main():
    print "--------开始---------"
    num = random.randint(0,50)
    play_game(num)
    while True:
        yes_or_no = raw_input("Do you want to play this game again?")
        if yes_or_no == "yes":
            num = random.randint(0,50)
            play_game(num)
        elif yes_or_no == "no":
            print " -----再见----- "
            break
        else:
            print "请重新输入"


if __name__ == '__main__':
    main()
