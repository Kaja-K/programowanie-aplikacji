def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


n = int(input("Podaj liczbę do obliczenia silni: "))
print(f"Silnia z {n} to {silnia(n)}")
