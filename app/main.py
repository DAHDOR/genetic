from app.utils import ask_positive_integer, ask_positive_float
from app.core import genetic_algorithm_a, genetic_algorithm_b
from app.functions import a, b

class App:
    def __init__(self):
        self.population_size = 10
        self.difference_threshold = 0.05
        self.max_iterations = 500
        self.mutation_variability = 1

    def _ask_configuration(self):
        print("\n🔧 Configuración del Algoritmo Genético")
        print("═" * 70)
        
        self.population_size = ask_positive_integer("👥 Tamaño de la población", self.population_size)
        self.difference_threshold = ask_positive_float("📊 Umbral de diferencia", self.difference_threshold)
        self.max_iterations = ask_positive_integer("🔁 Número máximo de iteraciones", self.max_iterations)
        self.mutation_variability = ask_positive_float("🧬 Variabilidad de mutación", self.mutation_variability)
        
        print("\n✅ ¡Configuración completada!")
        print(f"    👥 Población: {self.population_size}")
        print(f"    📊 Umbral: {self.difference_threshold}")
        print(f"    🔁 Iteraciones máximas: {self.max_iterations}")
        print(f"    🧬 Variabilidad: {self.mutation_variability}")
        print("═" * 70)

    def run(self):
        print("🧬 ¡Bienvenido al Algoritmo Genético! 🧬")
        print("=" * 70)
        self._ask_configuration()
        print("🚀 ¡Listo para comenzar el algoritmo genético!")
        print("═" * 70)
        print("\n" + "═" * 70)
        print("================ ALGORITMO GENÉTICO PARA LA FUNCIÓN A ================")
        print("═" * 70)
        mejor_individuo_a = genetic_algorithm_a(
            population_size=self.population_size,
            generations=self.max_iterations,
            mutation_rate=self.mutation_variability,
        )
        print("\n" + "═" * 70)
        print("Mejor individuo (Función A):")
        print(f"    x: {mejor_individuo_a}")
        print(f"    Fitness: {a(mejor_individuo_a)}")
        print("═" * 70)
        print("\n" + "═" * 70)
        print("================ ALGORITMO GENÉTICO PARA LA FUNCIÓN B ================")
        print("═" * 70)
        mejor_individuo_b = genetic_algorithm_b(
            population_size=self.population_size,
            generations=self.max_iterations,
            mutation_rate=self.mutation_variability,
        )
        print("\n" + "═" * 70)
        print("Mejor individuo (Función B):")
        print(f"    x: {mejor_individuo_b[0]}")
        print(f"    y: {mejor_individuo_b[1]}")
        print(f"    Fitness: {b(mejor_individuo_b)}")
        print("═" * 70)
        print('\n📂 Resultados guardados en la carpeta "output".')
        print("\n" + "═" * 70)
        print("\n👋 Gracias por usar el Algoritmo Genético. ¡Hasta la próxima!\n")
        print("═" * 70 + "\n")
