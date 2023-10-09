MAX_EFFORT = 2000
MAX_ENERGY = 2000



def get_data_set_from_file(file):
    effort_list = []
    energy_list = []
    with open(file,'r') as o_file:
        i=1
        line = o_file.readline()
        size = int(line)
        for line in o_file:
            if(i <= size):
                effort_list.append(int(line))
            else:
                energy_list.append(int(line))
            i+=1
            
    return (effort_list, energy_list)



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



def create_random_data_set(days, max_effort = MAX_EFFORT, max_energy = MAX_ENERGY, min_effort = 0 , min_energy = 0):
    import random as r
    effort_list = []
    energy_list = []
    
    if max_energy < days:
        print("set invalido")
        return (effort_list,energy_list)
    for i in range(0, days):
        effort_list.append(r.randint(min_effort, max_effort))
        
        if i == 0:
            energy_list.append( r.randint(min_energy + days, max_energy))
        else:
            try:
                energy_list.append(r.randint(min_energy + days-i, energy_list[i-1]-1)) 
            except ValueError:
                print(f"VALUE ERROR: minimo = {min_energy + days-i}, maximo = {energy_list[i-1]-1}")
                print(f"min_energy = {min_energy}, dias menos i = {days-i}, i = {i}")

    return (effort_list, energy_list)



def data_set_to_txt(data_set : tuple, n, file_name):
    file_name = "2c2023-TDA-TP2\data\personalized_sets\_" + file_name 
    file = open(file_name,"w")
    file.write(str(n)+"\n")
    
    for data in data_set[0]:
        file.write(str(data)+"\n")
    for data in data_set[1]:
        file.write(str(data)+"\n")
   
    file.close()
    
    return 0
