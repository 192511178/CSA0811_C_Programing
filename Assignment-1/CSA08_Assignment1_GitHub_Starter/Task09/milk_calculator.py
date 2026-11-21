"""Validated milk payment calculator using Decimal for money."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
REFERENCE_FAT = Decimal("3.5")
REFERENCE_SNF = Decimal("8.5")
CENT = Decimal("0.01")

def money(value):
    """Round a monetary value to the nearest paisa."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Calculate the rate per litre from fat and SNF percentages."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    fat_steps = ((fat - REFERENCE_FAT) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - REFERENCE_SNF) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return money(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    """Calculate the farmer's payment for one milk entry."""
    litres = Decimal(str(litres))
    if litres < 0:
        raise ValueError("Litres cannot be negative.")
    if not Decimal("2.0") <= Decimal(str(fat)) <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0% and 7.0%.")
    if not Decimal("0.0") <= Decimal(str(snf)) <= Decimal("12.0"):
        raise ValueError("SNF must be between 0.0% and 12.0%.")
    return money(litres * rate_per_litre(fat, snf))

def ten_day_total(entries):
    """Return the total payment for an iterable of (litres, fat, snf) entries."""
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return money(total)

def main():
    """Read entries until the clerk enters 'done', then show the total."""
    entries = []
    while True:
        farmer_id = input("Farmer ID (or done): ").strip()
        if farmer_id.lower() == "done":
            break
        try:
            litres = Decimal(input("Litres: ").strip())
            fat = Decimal(input("Fat %: ").strip())
            snf = Decimal(input("SNF %: ").strip())
            amount = payout(litres, fat, snf)
        except (ValueError, ArithmeticError) as exc:
            print("Invalid entry:", exc)
            continue
        entries.append((litres, fat, snf))
        print(f"Farmer {farmer_id}: payment Rs {amount:,.2f}")
    print(f"Ten-day total: Rs {ten_day_total(entries):,.2f}")

if __name__ == "__main__":
    main()
