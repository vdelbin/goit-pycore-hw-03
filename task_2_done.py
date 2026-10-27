from random import randint

def get_numbers_ticket(min, max, quantity):

    if  quantity < 1 or max > 1000 or min < 1 or quantity > max:
        return []

    unique_numbers = set()

    while len(unique_numbers) < quantity:
        random_generated_number = randint(min, max)
        unique_numbers.add(random_generated_number)

    return sorted(list(unique_numbers))

print(get_numbers_ticket(1,99,12))