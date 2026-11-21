"""Revised calculator for seasonal rates and ten-day volume bonus."""
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
REFERENCE_FAT = Decimal("3.5")
REFERENCE_SNF = Decimal("8.5")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

RATE_CARDS = {
    "regular": {"base": Decimal("30.00"), "fat_step": Decimal("0.40")},
    "april_june": {"base": Decimal("32.00"), "fat_step": Decimal("0.45")},
}

def money(value):
    """Round money to two decimal places."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)

def select_rate_card(month):
    """Select seasonal card; month is an integer from 1 to 12."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be from 1 to 12.")
    return RATE_CARDS["april_june"] if month in (4, 5, 6) else RATE_CARDS["regular"]

def rate_per_litre(fat, snf, month):
    """Calculate per-litre rate using the applicable seasonal card."""
    card = select_rate_card(month)
    fat_steps = ((Decimal(str(fat)) - REFERENCE_FAT) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((Decimal(str(snf)) - REFERENCE_SNF) / Decimal("0.1")).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    rate = card["base"] + fat_steps * card["fat_step"] + snf_steps * SNF_STEP_VALUE
    return money(rate)

def entry_payment(litres, fat, snf, month):
    """Calculate one entry's payment under the selected season."""
    litres = Decimal(str(litres))
    if litres < 0:
        raise ValueError("Litres cannot be negative.")
    if not Decimal("2.0") <= Decimal(str(fat)) <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0% and 7.0%.")
    if not Decimal("0.0") <= Decimal(str(snf)) <= Decimal("12.0"):
        raise ValueError("SNF must be between 0.0% and 12.0%.")
    return money(litres * rate_per_litre(fat, snf, month))

def ten_day_payment(entries, month):
    """Return ten-day total, adding the bonus when total litres exceed 500."""
    total_litres = sum((Decimal(str(row[0])) for row in entries), Decimal("0"))
    total_pay = sum((entry_payment(*row, month) for row in entries), Decimal("0.00"))
    if total_litres > BONUS_THRESHOLD:
        total_pay += total_litres * BONUS_PER_LITRE
    return money(total_pay)

if __name__ == "__main__":
    sample = [("300", "4.25", "8.63"), ("220", "3.50", "8.50")]
    for month in (3, 4):
        print(f"Month {month}: ten-day total Rs {ten_day_payment(sample, month):.2f}")
    print("Exactly 500 L (no bonus):", ten_day_payment([("500", "3.5", "8.5")], 4))
    print("More than 500 L (bonus applies):", ten_day_payment(sample, 4))
