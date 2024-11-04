import pytest
import time
from cache_system import Cache  # Importación del sistema de cache

# Arrange, Act, Assert for measuring cache performance

def test_cache_lru_efficiency():
    # Arrange: Configurar el caché con la política LRU
    cache = Cache(capacity=3, policy="LRU")
    data = ["A", "B", "C"]

    # Act: Almacenar los datos en el cache y acceder a ellos
    start_time = time.time()
    for item in data:
        cache.store(item)
    cache.access("A")  # Simular acceso frecuente a "A"
    cache.store("D")   # Forzar un reemplazo de "B"
    end_time = time.time()

    # Assert: Verificar el estado del cache y el tiempo transcurrido
    assert set(cache.get_contents()) == {"A", "C", "D"}, "El cache no tiene los datos correctos"
    assert "B" not in cache.get_contents(), "El dato B debería haber sido reemplazado"
    assert end_time - start_time < 1, "El almacenamiento y acceso no debe tardar más de 1 segundo"

def test_cache_fifo_performance():
    # Arrange: Configurar el cache con la política FIFO
    cache = Cache(capacity=3, policy="FIFO")
    data = ["A", "B", "C"]

    # Act: Almacenar los datos y agregar uno nuevo para forzar reemplazo
    start_time = time.time()
    for item in data:
        cache.store(item)
    cache.store("D")  # Forzar reemplazo de "A"
    end_time = time.time()

    # Assert: Verificar que se reemplazó correctamente y medir el tiempo
    assert set(cache.get_contents()) == {"B", "C", "D"}, "El cache no tiene los datos correctos"
    assert "A" not in cache.get_contents(), "El dato A debería haber sido reemplazado"
    assert end_time - start_time < 1, "El reemplazo no debe tardar más de 1 segundo"

def test_cache_hit_rate():
    # Arrange: Crear un cache con política LRU
    cache = Cache(capacity=3, policy="LRU")
    data = ["A", "B", "C"]

    # Act: Llenar el cache y verificar la tasa de aciertos
    for item in data:
        cache.store(item)
    cache.access("A")  # Simular acceso a un dato ya almacenado (acierto)
    cache.access("D")  # Acceso a un dato no almacenado (falla)
    hit_rate = cache.get_hit_rate()  # Método hipotético para obtener la tasa de aciertos

    # Assert: Verificar que la tasa de aciertos es la correcta
    assert hit_rate == 0.5, f"Tasa de aciertos incorrecta, esperada: 0.5, obtenida: {hit_rate}"
