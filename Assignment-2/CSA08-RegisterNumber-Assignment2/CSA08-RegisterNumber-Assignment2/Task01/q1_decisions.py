"""Q1: Electricity subsidy eligibility - separate if and if-elif-else."""
HOUSEHOLDS = [
    {"name": "H1", "units": 100, "ration": False, "senior": False},
    {"name": "H2", "units": 101, "ration": True,  "senior": False},
    {"name": "H3", "units": 200, "ration": True,  "senior": False},
    {"name": "H4", "units": 201, "ration": False, "senior": False},
    {"name": "H5", "units": 250, "ration": False, "senior": True},
    {"name": "H6", "units": 150, "ration": False, "senior": True},
    {"name": "H7", "units": 80,  "ration": True,  "senior": False},
    {"name": "H8", "units": 220, "ration": True,  "senior": False},
]

def separate_if(units, ration_card, senior_over_80):
    """Illustrates independent if statements; overlapping conditions can print multiple results."""
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if 101 <= units <= 200 and not ration_card:
        results.append("No subsidy")
    if units > 200 and senior_over_80:
        results.append("Senior-citizen exception: eligible (verify scheme rules)")
    if units > 200 and not senior_over_80:
        results.append("No subsidy")
    return results

def elif_decision(units, ration_card, senior_over_80):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if senior_over_80:
            return "Senior-citizen exception: eligible (verify scheme rules)"
        else:
            return "No subsidy"
    return "Invalid units"

def main():
    print("PREDICTIONS / TEST RESULTS")
    for h in HOUSEHOLDS:
        args = (h["units"], h["ration"], h["senior"])
        print(f'{h["name"]}: {h["units"]} units, ration={h["ration"]}, senior>80={h["senior"]}')
        print("  Separate if:", " | ".join(separate_if(*args)))
        print("  if-elif-else:", elif_decision(*args))
    print("\nBoundary checks: 100, 101, 200, 201")
    for units in (100, 101, 200, 201):
        print(units, "->", elif_decision(units, True, False))

if __name__ == "__main__":
    main()
