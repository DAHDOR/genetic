from app.utils import ask_positive_integer, ask_positive_float

class App:
    def __init__(self):
        self.population_size = 10
        self.difference_threshold = 0.05
        self.max_iterations = 500
        self.mutation_variability = 1

    def _ask_configuration(self):
        print("\n🔧 Configuración del Algoritmo Genético")
        print("═" * 45)
        
        self.population_size = ask_positive_integer("👥 Tamaño de la población", self.population_size)
        self.difference_threshold = ask_positive_float("📊 Umbral de diferencia", self.difference_threshold)
        self.max_iterations = ask_positive_integer("🔁 Número máximo de iteraciones", self.max_iterations)
        self.mutation_variability = ask_positive_float("🧬 Variabilidad de mutación", self.mutation_variability)
        
        print("\n✅ ¡Configuración completada!")
        print(f"    👥 Población: {self.population_size}")
        print(f"    📊 Umbral: {self.difference_threshold}")
        print(f"    🔁 Iteraciones máximas: {self.max_iterations}")
        print(f"    🧬 Variabilidad: {self.mutation_variability}")
        print("═" * 45)

    def run(self):
        print("🧬 ¡Bienvenido al Algoritmo Genético! 🧬")
        print("=" * 50)
        self._ask_configuration()
        print("\n🚀 ¡Listo para comenzar el algoritmo genético!")
        