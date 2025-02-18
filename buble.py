def bubble(ll):
    n=len(ll)
    for i in range(n-1):
        for j in range(n-i-1):
            if ll[j+1]<ll[j]:
                ll[j],ll[j+1]=ll[j+1],ll[j]
    return ll

def main():
    ll=[8,5,9,6,3,7,1,3]
    print bubble(ll)
main()
        
