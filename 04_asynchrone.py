import asyncio

async def dire_bonjour_apres_delai(nom, delai):
    await asyncio.sleep(delai)  # Simule une attente non bloquante
    print(f"Bonjour, {nom}!")

async def main():
    # Planifie l'exécution des tâches de manière asynchrone
    await asyncio.gather(
        dire_bonjour_apres_delai("Alice", 2),
        dire_bonjour_apres_delai("Bob", 1),
        dire_bonjour_apres_delai("Charlie", 3)
    )

# Exécute la boucle d'événements asynchrone
asyncio.run(main())