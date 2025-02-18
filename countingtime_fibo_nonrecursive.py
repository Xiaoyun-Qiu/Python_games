def fibo(num):
    ll=[0,1]
    if num>=2:
        for i in range(num-1):
            ss=ll[i]+ll[i+1]
            ll.append(ss)
        return ll[-1]
    elif num<=1:
        return num

def main():
    import time
    num=input('Enter an integer: ')
    t1=time.clock()
    ss=fibo(num)
    t2=time.clock()
    print 'The %dth fibo-number is %d.'% (num,ss)
    print 'It takes %f seconds.'% t2

main()
        
