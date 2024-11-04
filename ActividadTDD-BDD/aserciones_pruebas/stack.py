from typing import Any

class Stack:
    """Implementa una estructura de datos de Pila"""
    
    def __init__(self):
        """Constructor"""
        self.items = []
    
    def push(self, data: Any) -> None:
        """Añade un elemento a la parte superior de la pila."""
        self.items.append(data)
    
    def pop(self) -> Any:
        """Elimina y devuelve el elemento en la parte superior de la pila."""
        return self.items.pop()
    
    def peek(self) -> Any:
        """Devuelve el elemento en la parte superior de la pila sin eliminarlo"""
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """Devuelve True si la pila está vacía, de lo contrario devuelve False"""
        return len(self.items) == 0
