## 1. 교과목 정보 출력 ##
#### coding here ####
# 학수번호 = input('학수번호를 입력하세요 : ')

# if 학수번호 == '데사B0001' :
#     print('입력하신 과목은 데이터사이언스를위한수학 이며, 강의실은 숭인관 1호 입니다.')
# elif 학수번호 == '문화A0019' :
#     print('입력하신 과목은 파이썬프로그래밍 이며, 강의실은 인문관 15호 입니다.')
# elif 학수번호 == '문화A0007' :
#     print('입력하신 과목은 데이터사이언스입문 이며, 강의실은 대학원 4호 입니다.')
# else :
#     print('입력하신 과목은 정보에 없습니다.')

## 2. 숫자 맞추기 게임 ##]=
#answer = 25
#### coding here ####
# num = 0
# while True:
#     num = int(input('숫자를 입력하세요 : ')) 
#     if num < 25 :
#         print('UP !')
#     elif num > 25 :
#         print('DOWN !')
#     elif num == 25 :
#         print('정답!') 
#         break



## 3. 물건 값 계산하기 ##
#### coding here ####

# item_A = int(input('물품A를 몇 개 구매 하시겠습니까? '))
# item_B = int(input('물품B를 몇 개 구매 하시겠습니까? '))
# item_C = int(input('물품C를 몇 개 구매 하시겠습니까? '))
# item_D = int(input('물품D를 몇 개 구매 하시겠습니까? '))
# item_E = int(input('물품E를 몇 개 구매 하시겠습니까? '))
# print('총 구매하신 항목은 A %d개 B %d2개 C %d개 D %d개 E %d개 입니다.' %(item_A, item_B, item_C, item_D, item_E))

# price = item_A * 3000 + item_B * 25000 + item_C * 1600 + item_D * 18000 + item_E * 2600

# coupon = input('할인 쿠폰을 입력해 주세요 : ')

# if coupon == 'A37B2QD' :
#     print('주문하신 총 금액은 %d원 입니다.' %(price * 0.9))
# elif coupon == 'D8TY41M' :
#     print('주문하신 총 금액은 %d원 입니다.' %(price * 0.95))
# elif coupon == '9PBX8UY' :
#     print('주문하신 총 금액은 %d원 입니다.' %(price * 0.85))
# else :
#     print('주문하신 총 금액은 %d원 입니다.' %(price))






## 4. 소수 여부 판단하기 ##
#### coding here ####




# num1 = 0
# num2 = 0

# while True :
#     num1 = int(input('숫자를 입력하세요 : '))
#     for i in range (2,num1) :
#         if num1 >0 and num1 % i == 0 :
#            print('소수가 아닙니다') 
#            continue
#         elif  num1 < 0 :
#             print('자연수를 입력하세요.')
#         else : 
#             print('소수입니다.')
#             print('종료합니다.')
#             break






## 5. 리스트 데이터 확인 ##
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

#### coding here ####
# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']
# list = input('리스트를 입력하세요 : ')
# if list == answer :
#     print('O')
# else :
#     print('X')