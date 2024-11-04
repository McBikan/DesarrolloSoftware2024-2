Feature: Sistema de cache con políticas de reemplazo
  Para mejorar el rendimiento del sistema
  Como desarrollador de sistemas de alto rendimiento
  Necesito un sistema de cache que almacene datos más utilizados bajo distintas políticas de reemplazo.

  Scenario: Almacenar y acceder datos frecuentemente usados con LRU
    Given un cache con capacidad de 3 elementos y política de reemplazo LRU
    When almaceno los datos "A", "B", y "C" en el cache
    And accedo al dato "A"
    And almaceno el dato "D"
    Then el cache debe contener los datos "A", "C", y "D"
    And el dato "B" debe haber sido reemplazado

  Scenario: Almacenar y acceder datos frecuentemente usados con FIFO
    Given un cache con capacidad de 3 elementos y política de reemplazo FIFO
    When almaceno los datos "A", "B", y "C" en el cache
    And almaceno el dato "D"
    Then el cache debe contener los datos "B", "C", y "D"
    And el dato "A" debe haber sido reemplazado

  Scenario: Cambiar la política de reemplazo sin perder datos
    Given un cache con capacidad de 3 elementos y política de reemplazo FIFO
    When almaceno los datos "A", "B", y "C" en el cache
    And cambio la política de reemplazo a LRU
    Then el cache debe seguir conteniendo los datos "A", "B", y "C"
