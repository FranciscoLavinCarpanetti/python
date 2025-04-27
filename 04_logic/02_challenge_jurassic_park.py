def count_carnivore_dinosaur_eggs(egg_list: list) -> int:
    """Esta función cuenta la cantidad de huevos de dinosaurios carnívoros en una lista de huevos."""
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs

egg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_carnivore_dinosaur_eggs(egg_list))
