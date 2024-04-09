from dataclasses import dataclass
from typing import List


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return isinstance(other, Elemento) and self.nombre == other.nombre


class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nuevo_nombre)
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ', '.join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"


# Ejemplo de uso
if __name__ == "__main__":
    elemento1 = Elemento("A")
    elemento2 = Elemento("B")
    elemento3 = Elemento("C")

    conjunto1 = Conjunto("Conjunto 1")
    conjunto1.agregar_elemento(elemento1)
    conjunto1.agregar_elemento(elemento2)

    conjunto2 = Conjunto("Conjunto 2")
    conjunto2.agregar_elemento(elemento2)
    conjunto2.agregar_elemento(elemento3)

    print(conjunto1)
    print(conjunto2)

    print("¿El conjunto 1 contiene el elemento B?", conjunto1.contiene(elemento2))

    conjunto3 = conjunto1 + conjunto2
    print(conjunto3)

    conjunto4 = Conjunto.intersectar(conjunto1, conjunto2)
    print(conjunto4)
