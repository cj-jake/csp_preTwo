"""
不会写
"""

# 红灯 r 秒，黄灯 y 秒，绿灯 g 秒
r, y, g = [int(i) for i in input().split()]

# n表示小明总共经过的道路段数和看到的红绿灯数目
n = int(input())


# 定义getTime(k,t,time)函数计算时间开销
# k为0，1，2，3时分别代表道路，红灯，黄灯，绿灯
# t代表通过道路需要的时间或信号灯剩余秒数
# time表示到达路口时，距开始已经经过多长时间
def getTime(k, t, time):
    if k == 0:  # 道路直接通行
        return t
    elif k == 1:#红灯
        if time <= t:  # t比较大(剩余秒数多)，到这个路口时，红灯还是红灯
            return t-time
        else:  # t比较小，到这个路口，红灯已变为绿灯，相当于把时间轴的原点向后移动t，假设小明出发时，该路口刚亮绿灯
            return getTime(3, g, time-t)
    elif k == 2:#黄灯
        if time <= t:
            return t-time+r#注意这里和红灯不一样了，等完黄灯还要等红灯
        else:  # 黄灯之后是红灯
            return getTime(1, r, time-t)
    else:#k == 3,绿灯
        if time <= t:
            return 0
        else:  # 绿灯之后是黄灯
            return getTime(2, y, time-t)


sum = 0
ryg = r+y+g  # 用于取余
for i in range(n):
    k, t = [int(i) for i in input().split()]
    sum += getTime(k, t, sum % ryg)

print(sum)
