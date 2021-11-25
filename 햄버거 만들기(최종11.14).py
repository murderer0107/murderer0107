import turtle
import random
turtle.title("햄버거 완성!")


#변경 내용
#터틀로 햄버거 만들기 완성
#level_1 함수와 level_2 함수 만들어서 점수에 따라 레벨이 바뀌도록 해결
#point == 25 일때 일을 그만해도 된다는 엔딩 추가
#레벨2에서 남은 자리가 없는데 청소를 안할 시 point에서 -1되도록 변경

def make(color, x, end_x, y): #빵, 소스, 야채, 패티 그래픽
    turtle.speed(0)
    turtle.penup()
    turtle.shape("square")
    turtle.color(color)
    for i in range(x, end_x, 40):
        turtle.setpos(i, y)
        turtle.stamp()



Bulgogi_Burger = ["불고기 소스", "양상추", "불고기패티"]
Cheese_Burger = ["치즈딥 소스", "피클", "순쇠고기패티"]
Chicken_Burger = ["어니언 소스", "양상추", "치킨패티"]
shrimp_Burger = ["타르타르 소스", "양상추", "새우패티"]
point = 5

level = 1
clean = 20 #총 자리
dirty = 0 #더러운 자리


menu = ["불고기버거", "치즈버거", "치킨버거", "새우버거"]

def Level_Up():#레벨업 과정
    global level
    global point
    if 1 <= point <= 9:
        level = 1
    elif point >= 10:
        level = 2

def cleaning(): #청소 할껀지 말껀지
    global dirty
    global clean
    global point
    clean = 20
    if dirty >= 10:
        print("총 자리: %d, 남은 자리: %d" %(clean, clean - dirty))
        clean_up = input("청소하시겠습니까?(yes or no):")
        if dirty >= 20:
            print("매장에 자리가 없습니다. 청소를 해야합니다")
            if clean_up == "no":
                print("총 자리: %d, 남은 자리: %d\n" %(clean, clean - dirty))
                print("매장에 앉을 자리가 없으므로 점수에서 -1을 합니다.")
                point -= 1
        if clean_up == "yes":
            dirty = 0
            print("청소완료! 총 자리: %d, 남은 자리: %d" %(clean, clean - dirty))
        elif clean_up == "no":
            print("청소를 하지 않았습니다.")
        else:
            print("선택지에 없는 답입니다. 다시 입력해주세요.")
            cleaning()


def MakingBurger() :#햄버거 만들기
        global r_order
        r_order = random.randint(0,3)
        print()
        print("손님:", menu[r_order], "주세요.")
        global dirty
        dirty += 1
        sauce = 0
        vegetable = 0
        patty = 0
        global point
        print("--------------------------------------")
        print("소스는 무엇을 넣어야 할까?")
        print("1.치즈딥 소스 2.불고기 소스 3.어니언 소스 4.타르타르 소스 ")
        print("--------------------------------------")
        sauce = int(input("답: "))
        print("--------------------------------------")
        print("야채는 무엇을 넣어야 할까?")
        print("1.양상추 2. 피클")
        print("--------------------------------------")
        vegetable = int(input("답: "))
        print("--------------------------------------")
        print("패티는 무엇을 넣어야 할까?")
        print("1. 불고기패티 2. 순쇠소기패티 3. 치킨패티 4. 새우패티")
        print("--------------------------------------")
        patty = int(input("답: "))
        turtle.clear()
        print()
        

        if r_order == 0 :  #불고기 버거 만들기
            if sauce == 2 and vegetable == 1 and patty == 1 :
                
                point += 1
                print("완벽해요! 햄버거를 만드는 중 입니다.", "점수:",point)
                 #아래 빵
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, -50 - plus)
                    make("dark goldenrod", -180, 201, -50 - plus)
                    make("goldenrod", -150, 151, -90 - plus)
                    make("dark goldenrod", -130, 151, -90 - plus)
                    plus = 20
                #소스
                make("saddle brown", -150, 151, -30)
                make("maroon", -130, 151, -30)
                #야채
                make("pale green", -150, 151, -10)
                make("pale green", -130, 151, 10)
                #패티
                y = 0
                for i in range(2):
                    make("peru", -150, 151, 30 +  y)
                    make("burlywood", -130, 151, 30 + y)
                    y = 20
                #위 빵
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, 70 + plus)
                    make("dark goldenrod", -180, 201, 70 + plus)
                    make("goldenrod", -150, 151, 110 + plus)
                    make("dark goldenrod", -130, 151, 110 + plus)
                    plus = 20

            else :
                point -= 1
                print("무언가가 틀린 듯 하다.....", "점수:",point)

        if r_order == 1 :  #치즈 버거 만들기
            turtle.clear()
            if sauce == 1 and vegetable == 2 and patty == 2 :
                point += 1
                print("완벽해요! 햄버거를 만드는 중 입니다.", "점수:",point)
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, -50 - plus)
                    make("dark goldenrod", -180, 201, -50 - plus)
                    make("goldenrod", -150, 151, -90 - plus)
                    make("dark goldenrod", -130, 151, -90 - plus)
                    plus = 20
                #소스
                make("lemon chiffon", -150, 151, -30)
                make("yellow", -130, 151, -30)
                #야채
                make("yellow green", -150, 151, -10)
                make("yellow green", -130, 151, 10)
                #패티
                y = 0
                for i in range(2):
                    make("peru", -150, 151, 30 +  y)
                    make("burlywood", -130, 151, 30 + y)
                    y = 20
                #위 빵
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, 70 + plus)
                    make("dark goldenrod", -180, 201, 70 + plus)
                    make("goldenrod", -150, 151, 110 + plus)
                    make("dark goldenrod", -130, 151, 110 + plus)
                    plus = 20

               

            else :
                point -= 1
                print("무언가가 틀린 듯 하다.....", "점수:",point)

        if r_order == 2 :  #치킨 버거 만들기
            turtle.clear()
            if sauce == 3 and vegetable == 1 and patty == 3 :
                point += 1
                print("완벽해요! 햄버거를 만드는 중 입니다.", "점수:",point)
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, -50 - plus)
                    make("dark goldenrod", -180, 201, -50 - plus)
                    make("goldenrod", -150, 151, -90 - plus)
                    make("dark goldenrod", -130, 151, -90 - plus)
                    plus = 20
                #소스
                make("navajo white", -150, 151, -30)
                make("antique white", -130, 151, -30)
                #야채
                make("pale green", -150, 151, -10)
                make("pale green", -130, 151, 10)
                #패티
                y = 0
                for i in range(2):
                    make("sandy brown", -150, 151, 30 +  y)
                    make("gold", -130, 151, 30 + y)
                    y = 20
                #위 빵
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, 70 + plus)
                    make("dark goldenrod", -180, 201, 70 + plus)
                    make("goldenrod", -150, 151, 110 + plus)
                    make("dark goldenrod", -130, 151, 110 + plus)
                    plus = 20

                

            else :
                point -= 1
                print("무언가가 틀린 듯 하다.....", "점수:",point)

        if r_order == 3 :  #새우 버거 만들기
            turtle.clear()
            if sauce == 4 and vegetable == 1 and patty == 4 :
                point += 1
                print("완벽해요! 햄버거를 만드는 중 입니다.", "점수:",point)
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, -50 - plus)
                    make("dark goldenrod", -180, 201, -50 - plus)
                    make("goldenrod", -150, 151, -90 - plus)
                    make("dark goldenrod", -130, 151, -90 - plus)
                    plus = 20
                #소스
                make("moccasin", -150, 151, -30)
                make("floral white", -130, 151, -30)
                #야채
                make("pale green", -150, 151, -10)
                make("pale green", -130, 151, 10)
                #패티
                y = 0
                for i in range(2):
                    make("light salmon", -150, 151, 30 +  y)
                    make("peach puff", -130, 151, 30 + y)
                    y = 20
                #위 빵
                plus = 0
                for i in range (2):
                    make("goldenrod", -200, 201, 70 + plus)
                    make("dark goldenrod", -180, 201, 70 + plus)
                    make("goldenrod", -150, 151, 110 + plus)
                    make("dark goldenrod", -130, 151, 110 + plus)
                    plus = 20

               

            else :
                point -= 1
                print("무언가가 틀린 듯 하다.....", "점수:",point)


#import random  #손님의 랜덤 주문

#def Order() :
#    global r_order
#    r_order = random.randint(0,3)
#    print()
#    print("손님:", menu[r_order], "주세요.") 
#    global dirty
#    dirty += 1
#    MakingBurger()
    
    
select = 0             #게임 시작전 메뉴안내
while True :
    print("======<메뉴설명>======")
    print("====1. 불고기버거=====")
    print("====2. 치즈버거=======")
    print("====3. 치킨버거=======")
    print("====4. 새우버거=======")
    print("====5. 게임시작=======")

    select = int(input("알고 싶은 메뉴의 번호를 입력하세요: "))

    if select == 5 :
        print("지금부터 게임을 시작합니다.")
        #Order()
        print("게임 시작시 레벨 1로 시작합니다. 레벨1은 햄버거 만들기만 가능합니다.")
        MakingBurger()
        break
    elif select == 1 :
        print("불고기버거는 \n", Bulgogi_Burger, "을 필요로 합니다.")
    elif select == 2 :
        print("치즈버거는 \n", Cheese_Burger, "을 필요로 합니다.")
    elif select == 3 :
        print("치킨버거는 \n", Chicken_Burger, "을 필요로 합니다.")
    elif select == 4 :
        print("새우버거는 \n", shrimp_Burger, "을 필요로 합니다.")

def level_1():
    if level == 1:  #레벨에 따라 바뀌는 업무
        while True :
            #Order()
            print("\n현재 레벨은 1입니다. 햄버거 만들기만 가능합니다.")
            MakingBurger()
            Level_Up()
            
            if level == 2:
                level_2()
                break
            elif point == 0:
                break
def level_2():
    if level == 2 :
        while True :
            print("\n현재 레벨은 2입니다. 햄버거 만들기와 매장관리가 가능합니다.")
            MakingBurger()
            cleaning()
            Level_Up()
            #Order()
            if level == 1:
                level_1()
            elif point == 25:
                print("당신은 점수 %d을 달성해서 더 이상 일을 하지 않아도 됩니다!" %point)
                quit()
                break

level_1()      


while True :
    if point == 0 : #해고와 다시 기회 주기
        print("당신은 너무 많은 실수로 인해 해고되었습니다.....")
        restart = str(input("다시 하시겠습니다? (yes or no): "))
        if restart == "yes":
            point = 5
            print("게임 시작 시 레벨 1로 시작합니다. 레벨1은 햄버거 만들기만 가능합니다.")
            level_1()
        elif restart == "no":
            quit()
        
        
    
turtle.done()
