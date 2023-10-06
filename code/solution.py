def get_matrix_of_training(e, s):
    M = [[0 for j in range(len(e))] for i in range(len(s))] # fil: entrenamientos, col: energia
    for ei in range(len(e)):
        for sj in range(len(s)):
            if(sj > ei): continue
            if(sj == 0):
                if(ei == 0 or ei == 1):
                    M[ei][sj] = min(e[ei], s[sj])
                else:
                    M[ei][sj] = min(e[ei], s[sj]) + max(M[ei-2]) 
            else:
                M[ei][sj] = min(e[ei], s[sj]) + (M[ei-1][sj-1])
    return M

def get_best_secuence_of_trainings(e, s):
    M = get_matrix_of_training(e, s)
    ei = len(e)-1
    sj = M[ei].index(max(M[ei]))
    secuence = []
    while(not (ei == 0 and sj == 0)):
        secuence.insert(0, 'E')
        if(sj == 0):
            secuence.insert(0, 'D')
            if(ei == 1): 
                ei -= 1
                continue 
            else:
                ei -= 2
            sj = M[ei].index(max(M[ei]))
        else:
            ei -=1
            sj -= 1
        if(ei == 0): secuence.insert(0, 'E')
                
    return secuence

def get_best_training(e, s):
    M = get_matrix_of_training(e, s)
    return max(M[len(e)-1])

def get_alternative_training(e, s):
    
    cant_e = len(e)
    
    first_train = min(e[0], s[0])
    second_train = max(first_train + min(e[1], s[1]), min(e[1], s[0])) 
    opt = [first_train, second_train]
    
    for i in range(2, cant_e):
        a = min(e[i], s[i]) + opt[i-1]
        b = min(e[i], s[0]) + opt[i-2]
        opt.append(max(a, b))
        
    return opt[cant_e - 1]

'''
e = [5, 80, 12, 7, 16]
#   e1  e2  e3  e4 e5

s = [80, 16, 14, 8, 3]
#   s1  s2  s3  s4 s5

## secuence: [D, E, E, D, E]

print(get_alternative_training(e, s))        

def print_matrix(M):
    for i in M:
        print(i)
    
print(get_best_training(e, s))        
print_matrix(get_matrix_of_training(e, s))        
print(get_best_secuence_of_trainings(e, s))        
'''