buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

# Nomor 1
print("Nomor 1: ", buah[2:5])

# Nomor 2
x = list(buah)
x.pop(3)
buah = tuple(x)
print("Nomor 2: ", buah)

# Nomor 3
y = list(buah)
y.insert(2,"manggis")
buah = tuple(y)
print("Nomor 3: ", buah)
