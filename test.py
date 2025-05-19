from timeit import timeit

# Fonction lambda
lambda_func = lambda x: x * 2

# Fonction classique
def def_func(x):
    return x * 2

print("test :")
# Mesure du temps
print("lambda:", timeit('lambda_func(5)', globals=globals(), number=10_000_000))
print("def   :", timeit('def_func(5)', globals=globals(), number=10_000_000))