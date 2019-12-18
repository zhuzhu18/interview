'''
有一个人用一张1024元的纸币购买价值n元的商品，
卖家用四种硬币找零，分别是1、4、16、64，
问卖家找零最少需要多少个硬币
'''

CHANGE = [64, 16, 4, 1]

def solution(all_money, value):
    rest_money = all_money - value
    time = list()
    for i in range(len(CHANGE)):
        if rest_money < CHANGE[i]:
            time.append(0)
            continue
        remainer = rest_money % CHANGE[i]
        time.append(int((rest_money - remainer) / CHANGE[i]))
        rest_money = rest_money - time[i] * CHANGE[i]
    return time, sum(time)
