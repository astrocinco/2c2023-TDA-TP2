
e = [5, 80, 12, 7, 16]
#   e1  e2  e3  e4 e5
s = [80, 16, 14, 8, 3]
#   s1  s2  s3  s4 s5

def get_best_training(e, s):
    
    cant_e = len(e)
    
    first_train = min(e[0], s[0])
    second_train = max(first_train + min(e[1], s[1]), min(e[1], s[0])) 
    opt = [first_train, second_train]
    
    for i in range(2, cant_e):
        a = min(e[i], s[i]) + opt[i-1]
        b = min(e[i], s[0]) + opt[i-2]
        opt.append(max(a, b))
        
    return opt[cant_e - 1]

print(get_best_training(e, s))        