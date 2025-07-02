import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from app.functions import a, b

def create_initial_population_a(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]

def create_initial_population_b(size, lower_bound, upper_bound):
    return [(random.uniform(lower_bound, upper_bound),
             random.uniform(lower_bound, upper_bound))
            for _ in range(size)]

def selection(population, fitnesses, tournament_size=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected

def crossover_a(parent1, parent2):
    alpha = random.random()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2

def crossover_b(parent1, parent2):
    alpha = random.random()
    child1 = tuple(alpha * p1 + (1 - alpha) * p2 for p1, p2 in zip(parent1, parent2))
    child2 = tuple(alpha * p2 + (1 - alpha) * p1 for p1, p2 in zip(parent1, parent2))
    return child1, child2

def mutation_a(individual, mutation_rate=0.1, lower_bound=-10, upper_bound=10):
    if random.random() < mutation_rate:
        mutation_amount = random.uniform(-1, 1)
        individual += mutation_amount
        individual = max(min(individual, upper_bound), lower_bound)
    return individual

def mutation_b(individual, mutation_rate=0.1, lower_bound=-10, upper_bound=10):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            mutation_amount = random.uniform(-1, 1)
            individual[i] += mutation_amount
            individual[i] = max(min(individual[i], upper_bound), lower_bound)
    return tuple(individual)

def genetic_algorithm_a(population_size, generations, mutation_rate, lower_bound=-10, upper_bound=10):
    population = create_initial_population_a(population_size, lower_bound, upper_bound)
    
    # Prepare for plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    best_performers = []
    all_populations = []

    # Prepare for table
    table = PrettyTable()
    table.field_names = ["Generación", "x", "Fitness"]
    table.float_format = ".4"
    table.align["x"] = "r"
    table.align["Fitness"] = "r"
    table.min_width["x"] = 8
    table.min_width["Fitness"] = 8

    for generation in range(generations):
        fitnesses = [a(ind) for ind in population]

        # Store the best performer of the current generation
        best_individual = max(population, key=a)
        best_fitness = a(best_individual)
        best_performers.append((best_individual, best_fitness))
        all_populations.append(population[:])
        table.add_row([generation + 1, best_individual, best_fitness])

        population = selection(population, fitnesses)

        next_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            child1, child2 = crossover_a(parent1, parent2)

            next_population.append(mutation_a(child1, mutation_rate, lower_bound, upper_bound))
            next_population.append(mutation_a(child2, mutation_rate, lower_bound, upper_bound))

        # Replace the old population with the new one, preserving the best individual
        next_population[0] = best_individual
        population = next_population

    # Print the table
    print("\nTabla de mejores individuos por generación:")
    # Mostrar tabla completa si <= 20 filas, si no, mostrar intervalos
    total_rows = len(table._rows)
    if total_rows <= 20:
        print(table)
    else:
        interval = max(1, total_rows // 10)
        # Obtener solo las filas seleccionadas
        selected_indices = [0] + [i for i in range(1, total_rows-1) if i % interval == 0] + [total_rows-1]
        # Imprimir encabezado una sola vez
        header = table.get_string(start=0, end=1).split('\n')[:3]  # Header y separadores
        print('\n'.join(header))
        for idx in selected_indices:
            row_str = table.get_string(start=idx, end=idx+1).split('\n')[3]  # Solo la fila
            print(row_str)
        print(header[-1])  # Línea final

    # Save table to CSV
    import csv, os
    os.makedirs('output', exist_ok=True)
    with open('output/tabla_generaciones_a.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(table.field_names)
        for row in table._rows:
            writer.writerow(row)

    # Plot the population of the last generation
    final_population = all_populations[-1]
    final_fitnesses = [a(ind) for ind in final_population]
    ax.scatter(range(len(final_population)), final_population, color='blue', label='Individuos')
    ax.scatter([final_population.index(best_individual)], [best_individual], color='red', s=100, label='Mejor Individuo')
    ax.set_xlabel('Índice de individuo')
    ax.set_ylabel('x')
    ax.set_title(f'Soluciones de la población en la generación final ({generations})')
    ax.legend()
    plt.savefig('output/poblacion_final_a.png')
    plt.close(fig)

    # Gráfica del valor de x a lo largo de las generaciones
    generations_list = range(1, len(best_performers) + 1)
    x_values = [ind[0] for ind in best_performers]
    fig, ax = plt.subplots()
    ax.plot(generations_list, x_values, label='x', color='blue')
    ax.set_xlabel('Generación')
    ax.set_ylabel('Valor de x')
    ax.set_title('Mejor valor de x a lo largo de las generaciones')
    ax.legend()
    plt.savefig('output/mejor_x_generaciones.png')
    plt.close(fig)

    # Gráfica de la fitness a lo largo de las generaciones
    best_fitness_values = [fit[1] for fit in best_performers]
    min_fitness_values = [min([a(ind) for ind in pop]) for pop in all_populations]
    max_fitness_values = [max([a(ind) for ind in pop]) for pop in all_populations]
    fig, ax = plt.subplots()
    ax.plot(generations_list, best_fitness_values, label='Mejor fitness', color='black')
    ax.fill_between(generations_list, min_fitness_values, max_fitness_values, color='gray', alpha=0.5, label='Rango de fitness')
    ax.set_xlabel('Generación')
    ax.set_ylabel('Fitness')
    ax.set_title('Fitness a lo largo de las generaciones')
    ax.legend()
    plt.savefig('output/fitness_generaciones_a.png')
    plt.close(fig)

    return max(population, key=a)

    

def genetic_algorithm_b(population_size, generations, mutation_rate, lower_bound=-10, upper_bound=10):
    population = create_initial_population_b(population_size, lower_bound, upper_bound)

    # Prepare for plotting
    fig, axs = plt.subplots(2, 1, figsize=(12, 12))  # 2 rows, 1 column for subplots
    best_performers = []
    all_populations = []

    # Prepare for table
    table = PrettyTable()
    table.field_names = ["Generación", "x", "y", "Fitness"]
    table.float_format = ".4"
    table.align["x"] = "r"
    table.align["y"] = "r"
    table.align["Fitness"] = "r"
    table.min_width["x"] = 8
    table.min_width["y"] = 8
    table.min_width["Fitness"] = 8

    for generation in range(generations):
        fitnesses = [b(ind) for ind in population]

        # Store the best performer of the current generation
        best_individual = max(population, key=b)
        best_fitness = b(best_individual)
        best_performers.append((best_individual, best_fitness))
        all_populations.append(population[:])
        table.add_row([generation + 1, best_individual[0], best_individual[1], best_fitness])

        population = selection(population, fitnesses)

        next_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            child1, child2 = crossover_b(parent1, parent2)

            next_population.append(mutation_b(child1, mutation_rate, lower_bound, upper_bound))
            next_population.append(mutation_b(child2, mutation_rate, lower_bound, upper_bound))

        # Replace the old population with the new one, preserving the best individual
        next_population[0] = best_individual
        population = next_population

    # Print the table
    print("\nTabla de mejores individuos por generación:")
    # Mostrar tabla completa si <= 20 filas, si no, mostrar intervalos
    total_rows = len(table._rows)
    if total_rows <= 20:
        print(table)
    else:
        interval = max(1, total_rows // 10)
        selected_indices = [0] + [i for i in range(1, total_rows-1) if i % interval == 0] + [total_rows-1]
        header = table.get_string(start=0, end=1).split('\n')[:3]
        print('\n'.join(header))
        for idx in selected_indices:
            row_str = table.get_string(start=idx, end=idx+1).split('\n')[3]
            print(row_str)
        print(header[-1])

    # Save table to CSV
    import csv, os
    os.makedirs('output', exist_ok=True)
    with open('output/tabla_generaciones_b.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(table.field_names)
        for row in table._rows:
            writer.writerow(row)

    # Plot the population of one generation (last generation)
    final_population = all_populations[-1]
    final_fitnesses = [b(ind) for ind in final_population]

    axs[0].scatter(range(len(final_population)), [ind[0] for ind in final_population], color='blue', label='x')
    axs[0].scatter([final_population.index(best_individual)], [best_individual[0]], color='cyan', s=100, label='Mejor individuo x')
    axs[0].set_ylabel('x', color='blue')
    axs[0].legend(loc='upper left')

    axs[1].scatter(range(len(final_population)), [ind[1] for ind in final_population], color='green', label='y')
    axs[1].scatter([final_population.index(best_individual)], [best_individual[1]], color='magenta', s=100, label='Mejor individuo y')
    axs[1].set_ylabel('y', color='green')
    axs[1].set_xlabel('Índice de individuo')
    axs[1].legend(loc='upper left')

    axs[0].set_title(f'Soluciones de la población en la generación final ({generations})')
    fig.savefig('output/poblacion_final_b.png')
    plt.close(fig)

    # Gráfica de los valores de x e y a lo largo de las generaciones
    generations_list = range(1, len(best_performers) + 1)
    x_values = [ind[0][0] for ind in best_performers]
    y_values = [ind[0][1] for ind in best_performers]
    fig, ax = plt.subplots()
    ax.plot(generations_list, x_values, label='x', color='blue')
    ax.plot(generations_list, y_values, label='y', color='green')
    ax.set_xlabel('Generación')
    ax.set_ylabel('Valores de parámetros')
    ax.set_title('Valores de x e y a lo largo de las generaciones')
    ax.legend()
    plt.savefig('output/valores_xy_generaciones.png')
    plt.close(fig)

    # Gráfica de la fitness a lo largo de las generaciones
    best_fitness_values = [fit[1] for fit in best_performers]
    min_fitness_values = [min([b(ind) for ind in pop]) for pop in all_populations]
    max_fitness_values = [max([b(ind) for ind in pop]) for pop in all_populations]
    fig, ax = plt.subplots()
    ax.plot(generations_list, best_fitness_values, label='Mejor fitness', color='black')
    ax.fill_between(generations_list, min_fitness_values, max_fitness_values, color='gray', alpha=0.5, label='Rango de fitness')
    ax.set_xlabel('Generación')
    ax.set_ylabel('Fitness')
    ax.set_title('Fitness a lo largo de las generaciones')
    ax.legend()
    plt.savefig('output/fitness_generaciones_b.png')
    plt.close(fig)

    return max(population, key=b)