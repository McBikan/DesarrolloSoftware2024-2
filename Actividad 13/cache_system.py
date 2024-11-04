class Cache:
    def __init__(self, capacity, policy):
        self.capacity = capacity
        self.policy = policy
        self.cache = {}
        self.access_order = []  # Lista que mantiene el orden de acceso para LRU
        self.hits = 0
        self.misses = 0
        self.data = []

    def store(self, item):
        if item in self.cache:
            # Si el item ya está en el cache, lo actualizamos
            self.access_order.remove(item)  # Elimina el item de la lista de acceso
        elif len(self.cache) >= self.capacity:
            self.evict()  # Evita el cache si se alcanza la capacidad
        self.cache[item] = True  # Agrega el item al cache
        self.access_order.append(item)  # Actualiza el orden de acceso

    def access(self, item):
        if item in self.cache:
            self.hits += 1
            # Actualiza la posición del item
            self.access_order.remove(item)  # Lo eliminamos de la lista de acceso
            self.access_order.append(item)  # Lo movemos a la parte más reciente
        else:
            self.misses += 1  # Incrementa los fallos

    def evict(self):
        if self.policy == "LRU":
            # Elimina el menos recientemente usado
            oldest = self.access_order.pop(0)  # Remueve el primer elemento
        elif self.policy == "FIFO":
            # Elimina el primero que se insertó
            oldest = self.access_order.pop(0)  # Remueve el primer elemento
        del self.cache[oldest]  # Elimina el item del cache

    def get_contents(self):
        return list(self.cache.keys())  # Asegúrate de que esto retorne solo las claves


    def set_policy(self, new_policy):
        # Cambia la política de reemplazo
        self.policy = new_policy

    def get_hit_rate(self):
        total_accesses = self.hits + self.misses
        return self.hits / total_accesses if total_accesses > 0 else 0
