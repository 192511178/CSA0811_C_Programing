def read_percentage(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Enter a valid number, for example 8.5.")
            continue
        return value

def main():
    fat = read_percentage("Enter fat percentage: ")
    snf = read_percentage("Enter SNF percentage: ")
    print(f"Fat: {fat:5.2f}% | SNF: {snf:5.2f}%")

if __name__ == "__main__":
    main()
