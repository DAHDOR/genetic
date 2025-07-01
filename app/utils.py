def ask_positive_integer(prompt: str, default: int = 1) -> int:
    while True:
        try:
            res = input(f"{prompt} (por defecto: {default}): ")
            if res == "":
                return default
            value = int(res)
            if value > 0:
                return value
            else:
                raise ValueError("El número debe ser positivo.")
        except ValueError as e:
            print(f"❌ Por favor, ingresa un número válido. {e}")

def ask_positive_float(prompt: str, default: float = 0.1) -> float:
    while True:
        try:
            res = input(f"{prompt} (por defecto: {default}): ")
            if res == "":
                return default
            value = float(res)
            if value > 0:
                return value
            else:
                raise ValueError("El número debe ser positivo.")
        except ValueError as e:
            print(f"❌ Por favor, ingresa un número válido. {e}")