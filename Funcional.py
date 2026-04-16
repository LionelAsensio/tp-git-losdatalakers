import yaml
from pathlib import Path

def create_problem_dict(title, prompt, hints, tags):
    """Función pura para crear la estructura de datos"""
    return {
        "title": title,
        "prompt": prompt,
        "hints": hints,
        "tags": tags
    }

def update_yaml_functional(file_path, new_problems):
    """Lógica funcional para actualizar el archivo [cite: 53]"""
    path = Path(file_path)
    
    # Lectura
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            current_content = yaml.safe_load(f) or []
    else:
        current_content = []

    # Combinación (Inmutabilidad: creamos una nueva lista)
    updated_content = current_content + new_problems

    # Escritura
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(updated_content, f, allow_unicode=True, sort_keys=False)

def cargar_preguntas():
    """Implementación requerida para el laboratorio [cite: 54]"""
    # Definición de datos crudos
    raw_data = [
        ("Lambda Suma", "Suma dos números usando lambda.", ["lambda x, y: x + y"], ["funcional"]),
        ("Filtrar Pares", "Filtra pares de una lista.", ["Usa filter()"], ["funcional"]),
        ("Mapear Cuadrados", "Eleva lista al cuadrado.", ["Usa map()"], ["funcional"]),
        ("Reducir Lista", "Obtén el producto de una lista.", ["Usa functools.reduce"], ["funcional"]),
        ("Ordenar Tuplas", "Ordena por el segundo elemento.", ["key=lambda x: x[1]"], ["listas"]),
        ("Comprensión Listas", "Genera pares del 1 al 20.", ["if x % 2 == 0"], ["sintaxis"]),
        ("Generador", "Crea un generador de Fibonacci.", ["yield"], ["avanzado"]),
        ("Any/All", "Verifica si todos son positivos.", ["Usa all()"], ["lógica"]),
        ("Zip Lists", "Combina dos listas en un dict.", ["Usa zip()"], ["estructuras"]),
        ("Enumerate", "Imprime índice y valor.", ["Usa enumerate()"], ["básico"])
    ]

    # Uso de Programación Funcional para transformar los datos [cite: 53]
    procesados = list(map(lambda x: create_problem_dict(*x), raw_data))
    
    update_yaml_functional("problems.yaml", procesados)
    print("Preguntas Funcionales agregadas exitosamente.")