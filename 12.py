import random

boshi = int(input("Boshlanishi : "))
oxiri = int(input("Tugashi : "))
# son = random.randint(int(input("Boshlanishi : ")), int(input("Tugashi : ")))

for i in random.sample(range(boshi, oxiri + 1), 2):
    print(i)