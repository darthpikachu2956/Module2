import random

n = random.choice(range(3, 21))
result = []
print(n)

for i in range(1, 21):
    for j in range(i, 21):
        if i != j:
            if n % (i + j) == 0:
                pair = f'{i}{j}'
                result.append(pair)

print('Password: ', *result, sep='')
