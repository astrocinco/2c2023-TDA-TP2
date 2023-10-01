import solution
import sets
from colorama import Fore

def secuence_analysis(solution, local):
    diff = []

    if(len(solution) != len(local)): return ['Error']

    for i in range(len(solution)):
        if(solution[i] != local[i]):
            diff.append(i)

    return diff

def analysis_data_sets_catedra(files):
    for file in files:
        (e, s) = sets.get_data_set_from_file('data/catedra/' + file)
        (sol, sec) = sets.get_solution_from_file('data/catedra/Resultados Esperados.txt', file)
        
        local_sol = solution.get_best_training(e, s)
        local_sec = solution.get_best_secuence_of_trainings(e, s)
        
        if(local_sol==sol): sol_analysis = Fore.GREEN + '✔' 
        else: sol_analysis = Fore.RED + '✘' 
        
        secuence = secuence_analysis(sec, local_sec)
        if(not secuence): sec_analysis = Fore.GREEN + '✔' 
        elif(secuence == ['Error']): sec_analysis = Fore.RED + 'Len error ✘' 
        else: sec_analysis = Fore.RED + '✘' 
        
        print(f"{Fore.WHITE + file}: {sol_analysis} {Fore.WHITE} - Secuence diff: {sec_analysis}")


files = ['3.txt', '10.txt', '10_bis.txt', '10_todo_entreno.txt', '50.txt', '50_bis.txt', '100.txt', '500.txt', '1000.txt', '5000.txt']

analysis_data_sets_catedra(files)