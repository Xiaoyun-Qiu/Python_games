def check_mat_1(mylist):
    ll=[]
    for i in mylist:
        if i in ll:
            return True
            break
        else:
            ll.append(i)
    return False


        
