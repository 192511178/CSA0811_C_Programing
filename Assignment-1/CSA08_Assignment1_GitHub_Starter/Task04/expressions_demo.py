import math

fat_values = [4.2, 3.1]
for fat in fat_values:
    raw_steps = (fat - 3.5) / 0.1
    print(f"fat={fat}: raw={raw_steps}, round={round(raw_steps)}, int={int(raw_steps)}, floor={math.floor(raw_steps)}")

print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("round(2.675, 2) =", round(2.675, 2))
print("Chained validation:", 2.0 <= 4.2 <= 7.0)
