from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Casos de prueba para la Pila"""
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.stack = Stack()
    
    def tearDown(self):
        """Limpieza después de cada prueba"""
        self.stack = None
    
    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)  
        # El valor recién agregado debe estar en la parte superior
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)  
        # Después de otro push, el valor superior debe ser el último agregado
    
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)  
        # El valor superior (2) debe eliminarse y devolverse
        self.assertEqual(self.stack.peek(), 1)  
        # Después de pop(), el valor superior debe ser 1
    
    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)  
        # El valor superior debe ser el último agregado (2)
        self.assertEqual(self.stack.peek(), 2)  
        # La pila no debe cambiar después de peek()
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())  
        # La pila recién creada debe estar vacía
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())  
        # Después de agregar un elemento, la pila no debe estar vacía
