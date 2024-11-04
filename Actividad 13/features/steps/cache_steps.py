from behave import given, when, then
from cache_system import Cache

@given(u'un cache con capacidad de {capacity} elementos y política de reemplazo {policy}')
def step_impl(context, capacity, policy):
    context.cache = Cache(capacity=int(capacity), policy=policy)

@when(u'almaceno los datos "{data}" en el cache')
def step_impl(context, data):
    for item in data.split(","):
        context.cache.store(item.strip().strip('"'))

@when(u'accedo al dato "{data}"')
def step_impl(context, data):
    context.cache.access(data.strip().strip('"'))

@when(u'almaceno el dato "{data}"')
def step_impl(context, data):
    context.cache.store(data.strip().strip('"'))

@then('el cache debe contener los datos "{expected_items}"')
def step_impl(context, expected_items):
    expected_items_list = [item.strip().strip('"') for item in expected_items.split(",")]  # Normalizar los elementos
    actual_contents = [item.strip().strip('"') for item in context.cache.get_contents()]  # Normalizar los elementos
    
    # Convertir ambos a conjuntos para la comparación
    assert set(actual_contents) == set(expected_items_list), f'El cache debe contener {set(expected_items_list)}, pero tiene {set(actual_contents)}'


@then('el dato "{item}" debe haber sido reemplazado')
def step_impl(context, item):
    assert item.strip() not in context.cache.get_contents(), f'El dato {item.strip()} todavía está en el cache.'

@when(u'cambio la política de reemplazo a {policy}')
def step_impl(context, policy):
    context.cache.set_policy(policy.strip())

@then(u'el cache debe seguir conteniendo los datos "{data}"')
def step_impl(context, data):
    expected_contents = set(item.strip().strip('"') for item in data.split(","))
    actual_contents = set(context.cache.get_contents())
    assert actual_contents == expected_contents, f"El cache debe seguir conteniendo {expected_contents}, pero tiene {actual_contents}"

# Paso específico para un cache FIFO con capacidad de 3 elementos
@given(u'un cache FIFO con capacidad de 3 elementos')
def step_impl(context):
    context.cache = Cache(capacity=3, policy='FIFO')
