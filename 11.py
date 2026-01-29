import random

savollar_soni = 5
togri_javoblar = 0

for i in range(savollar_soni):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    print(f"{i+1}-savol: {a} + {b} = ?")
    javob = int(input("Javobingiz: "))

    if javob == a + b:
        print("To‘g‘ri! ✅\n")
        togri_javoblar += 1
    else:
        print(f"Noto‘g‘ri ❌ To‘g‘ri javob: {a + b}\n")

print("Test tugadi!")
print(f"Siz {savollar_soni} ta savoldan {togri_javoblar} tasiga to‘g‘ri javob berdingiz.")
