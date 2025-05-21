def ChkPrime(num):
    flag = True

    if num == 0 or num == 1: 
        flag = False
    elif num > 1:      
        for no in range(2,num):
            if(num % no) == 0:
                flag = False
                break

    return flag


