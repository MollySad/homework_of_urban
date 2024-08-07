import random


def generate_password(key):
    result = list()
    limit = (key + 1) // 2
    for i in range(1, limit):
        for j in range(i + 1, key):
            if key % (i + j) == 0:
                result.extend([i, j])
    return ''.join(map(str, result))


number = random.randint(3, 20)
print(f'Ключ: {number}\nПароль: {generate_password(number)}')
