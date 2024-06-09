def ctoe(ct):
    return ct / 100

def etoc(EUR):
    return int("EUR" * 100)

def main():
    amount = float(input("Gib den Betrag ein: "))
    unit = input("Gib die Einheit ein (ct, EUR): ")

    if unit == "ct":
        result = ctoe(amount)
        print(amount, "ct entsprechen", result, "EUR")
    elif unit == "EUR":
        result = etoc(amount)
        print(amount, "EUR entsprechen", result, "ct")
    else:
        print("Ungültige Einheit.")

if __name__ == "__main__":
    main()