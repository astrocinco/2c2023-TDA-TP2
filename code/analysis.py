import solution
import sets

import timeit
import pandas as pd
from colorama import Fore

def get_execution_time(method, max, rep, size):
    df_time = pd.DataFrame()
    for n_days in range(2, max):
        time = 0
        for i in range(1, rep):
            aux_set = sets.create_random_data_set(n_days, 5*n_days, 8*n_days)
            time += timeit.timeit(lambda: method(aux_set[0], aux_set[1]), number=size)
        time = time / rep
        
        aux_df = pd.DataFrame({"time": time*1000}, index=[n_days])
        df_time = pd.concat([df_time, aux_df])
    return df_time

def secuence_analysis(solution, local):
    diff = []

    if(len(solution) != len(local)): return ['Error']

    for i in range(len(solution)):
        if(solution[i] != local[i]):
            diff.append(i)

    return diff

def results_data_sets_catedra(files, method, secuence_method):
    solution_expected = []
    solution_obtained = []
    
    for file in files:
        (e, s) = sets.get_data_set_from_file('../data/catedra/' + file)
        (sol, sec) = sets.get_solution_from_file('../data/catedra/Resultados Esperados.txt', file)
        
        local_sol = method(e, s)
        local_sec = secuence_method(e, s)
        
        solution_expected.append((sol, sec))
        solution_obtained.append((local_sol, local_sec))
    
    return {"files": files, "expected": solution_expected, "obtained": solution_obtained}

def results_analysis(solution_results):
    
    for i in range(len(solution_results["expected"])):
        
        if(solution_results["expected"][i][0] == solution_results["obtained"][i][0]): sol_analysis = Fore.GREEN + '✔' + Fore.WHITE 
        else: sol_analysis = Fore.RED + '✘' + Fore.WHITE 
        
        secuence = secuence_analysis(solution_results["expected"][i][1], solution_results["obtained"][i][1])
        if(not secuence): sec_analysis = Fore.GREEN + '✔' + Fore.WHITE
        elif(secuence == ['Error']): sec_analysis = Fore.RED + 'Len error ✘' + Fore.WHITE 
        else: sec_analysis = Fore.RED + '✘' + Fore.WHITE 
        
        file_name = solution_results["files"][i]
        print(f"{file_name}: {sol_analysis} - Secuence diff: {sec_analysis}")
