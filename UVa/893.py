def g(y,m,d):
    m = (m+9)%12
    y = y - m//10
    return 365*y + y//4 -y//100 +y//400 + (m*306+5)//10 + (d-1)

def d(g):
    y = (10000*g + 14780)//3652425
    ddd = g - (365*y + y//4 - y//100 + y//400)
    if (ddd <0):
        y = y - 1
        ddd = g - (365*y + y//4 - y//100 + y//400)
    mi = (100*ddd + 52)//3060
    mm = (mi + 2)%12 + 1
    y = y + (mi+2)//12
    dd = ddd - (mi*306+5)//10 + 1
    return str(int(dd)) + " " + str(int(mm)) + " " + str(int(y))
while True:
    n = input().split(" ")
    days, day, months, year = n
    days = int(days)
    day = int(day)
    months = int(months)
    year = int(year)
    if day == 0 and months == 0 and year == 0:
        break
    print(d(g(year,months,day)+days))
