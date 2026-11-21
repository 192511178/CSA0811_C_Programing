from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

def total_paise(items):
    total = 0
    for amount in items:
        rupees, paise = amount.split(".")
        total += int(rupees) * 100 + int((paise + "00")[:2])
    return total

if __name__ == "__main__":
    print("float :", total_float(payments))
    print("Decimal:", total_decimal(payments))
    print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
    print("Integer paise:", total_paise(payments), "paise")
    bad_total = sum(Decimal(float(x)) for x in payments)
    print("Decimal(float(amount)):", bad_total)
