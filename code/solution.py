def get_matrix_of_training(e, s):
    M = [[0 for j in range(len(e))] for i in range(len(s))] # fil: entrenamientos, col: energia
    for i in range(len(e)):
        for j in range(len(s)):
            if(j > i): continue
            if(j == 0):
                if(i == 0 or i == 1):
                    M[i][j] = min(e[i], s[j])
                else:
                    M[i][j] = min(e[i], s[j]) + max(M[i-2]) 
            else:
                M[i][j] = min(e[i], s[j]) + (M[i-1][j-1])
    return M

def get_best_secuence_of_trainings(e, s):
    M = get_matrix_of_training(e, s)
    i = len(e)-1
    optimal_value = max(M[i])
    j = M[i].index(optimal_value)
    secuence = []
    while(not (i == 0 and j == 0)):
        if(j == 0):
            secuence.append('E')
            secuence.append('D')
            i -= 2
            continue
        else:
            secuence.append('E')
            i -=1
        j -= 1
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

print(get_alternative_training(e, s))        
print(get_best_training(e, s))        
print(get_best_secuence_of_trainings(e, s))        
'''