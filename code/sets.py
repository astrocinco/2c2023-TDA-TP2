
def get_data_set_from_file(file):
    e = []
    s = []
    with open(file,'r') as o_file:
        size = int(o_file.readline(1))
        i=1
        o_file.readline()
        for line in o_file:
            if(i <= size):
                e.append(int(line))
            else:
                s.append(int(line))
            i+=1
            
    return (e, s)

def get_solution_from_file(file, set):
    set_founded = False
    with open(file,'r') as o_file:
        while(not set_founded):
            info = (next(o_file).strip())
            parse = (info.split('\n'))
            set_founded = (parse[0] == set)

        str_optimal = (next(o_file).strip()).split(': ')[1]
        plan = (next(o_file).strip()).split(': ')[1]
            
        optimal = int(str_optimal)
        secuence = []
        for status in plan.split(', '):
            if(status=='Entreno'): 
                secuence.append('E')
            else:  
                secuence.append('D')
            
    return (optimal, secuence)

'''
print(get_data_set_from_file('data/catedra/3.txt'))
print(get_solution_from_file('data/catedra/Resultados Esperados.txt', '10.txt'))
'''