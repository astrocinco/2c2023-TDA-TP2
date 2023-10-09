import sets
import sys

def get_matrix_of_training(effort_list, energy_list):
    matrix = [[0 for j in range(len(effort_list))] for i in range(len(energy_list))] # fil: entrenamientos, col: energia
    
    for ei in range(len(effort_list)):
        for sj in range(len(energy_list)):
            if(sj > ei): continue
            if(sj == 0):
                if(ei == 0 or ei == 1):
                    matrix[ei][sj] = min(effort_list[ei], energy_list[sj])
                else:
                    matrix[ei][sj] = min(effort_list[ei], energy_list[sj]) + max(matrix[ei-2]) 
            else:
                matrix[ei][sj] = min(effort_list[ei], energy_list[sj]) + (matrix[ei-1][sj-1])

    return matrix



def get_best_secuence_of_trainings(effort_list, energy_list):
    matrix = get_matrix_of_training(effort_list, energy_list)
    ei = len(effort_list)-1
    sj = matrix[ei].index(max(matrix[ei]))
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
            sj = matrix[ei].index(max(matrix[ei]))
        else:
            ei -=1
            sj -= 1
        if(ei == 0): secuence.insert(0, 'E')
                
    return secuence



def get_best_training(effort_list, energy_list):
    matrix = get_matrix_of_training(effort_list, energy_list)

    return max(matrix[len(effort_list)-1])



def get_alternative_training(effort_list, energy_list):
    cant_e = len(effort_list)
    
    first_train = min(effort_list[0], energy_list[0])
    second_train = max(first_train + min(effort_list[1], energy_list[1]), min(effort_list[1], energy_list[0])) 
    opt = [first_train, second_train]
    
    for i in range(2, cant_e):
        a = min(effort_list[i], energy_list[i]) + opt[i-1]
        b = min(effort_list[i], energy_list[0]) + opt[i-2]
        opt.append(max(a, b))
        
    return opt[cant_e - 1]

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("ERROR")
        print("Usage: <arg1> file with information of trainings")
        sys.exit(1)

    (effort_list, energy_list) = sets.get_data_set_from_file(file)
    secuence = get_best_secuence_of_trainings(effort_list, energy_list)
    
    print(f"Best effort: {get_best_training(effort_list, energy_list)}")
    print(f"Secuence of trainings: {secuence}")