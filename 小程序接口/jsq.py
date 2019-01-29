import time
def starttime(): #开始时间
    global a, b, c, d
    a = int(time.strftime('%d'))
    b = int(time.strftime('%H'))
    c = int(time.strftime('%M'))
    d = int(time.strftime('%S'))
    abcd = time.strftime('%Y-%m-%d %H:%M:%S')
def overtime(): #结束时间
    global e, f, g, h
    e = int(time.strftime('%d'))
    f = int(time.strftime('%H'))
    g = int(time.strftime('%M'))
    h = int(time.strftime('%S'))
    efgh = time.strftime('%Y-%m-%d %H:%M:%S')
def sumtime(): #总共耗时
    sum = ((e-a)*24*60*60+(f-b)*60*60+(g-c)*60+(h-d))
    print ('程序耗时:', sum, '秒')
