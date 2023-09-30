import solution
import sets

def analysis_data_sets_catedra(files):
    for file in files:
        (e, s) = sets.get_data_set_from_file('data/catedra/' + file)
        (sol, sec) = sets.get_solution_from_file('data/catedra/Resultados Esperados.txt', file)
        
        local_sol = solution.get_best_training(e, s)
        #local_sec = solution.get_best_secuence_of_trainings(e, s)
        
        print(f" Solution compare: {local_sol}/{sol} - Secuence compare: ")


files = ['3.txt', '10.txt', '50.txt', '100.txt', '500.txt', '1000.txt', '5000.txt']

analysis_data_sets_catedra(files)