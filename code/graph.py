import solution
import sets
import analysis

import matplotlib.pyplot as plt
import pandas as pd

#Grafica el tiempo de ejecución dado un dataframe (acepta que tenga más de un método)
def make_execution_time_graph(time_execution, title="Gráfico de tiempo de ejecución"):
    plt.style.use('ggplot')
    time_execution.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()
    
def make_graph_for_different_method_durations(files, method='nuestra solucion'):

    best_results = analysis.results_data_sets_catedra(files, solution.get_best_training, solution.get_best_secuence_of_trainings)
    alternative_results = analysis.results_data_sets_catedra(files, solution.get_alternative_training, solution.get_best_secuence_of_trainings)
    
    results = ({
     'Expected': [result[0] for result in best_results["expected"]],
     'Obtained': [result[0] for result in best_results["obtained"]],
     'Alternative': [result[0] for result in alternative_results["obtained"]],
    })
    
    data = pd.DataFrame(results)

    
    plt.style.use('ggplot')
    data.plot.bar(stacked=False)
    plt.title("Diferencia de resultado con la respuesta óptima para " + method)
    plt.xlabel("Numero de set")
    plt.ylabel("Resultado del analisis")
    plt.yscale('log')
    plt.show()