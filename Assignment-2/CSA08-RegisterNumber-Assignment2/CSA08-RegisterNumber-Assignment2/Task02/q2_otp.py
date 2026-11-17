"""Q2: OTP verification demonstrating while, for, break, continue, pass and loop-else."""

def verify_with_while(correct_otp="246810", extra_attempts=0):
    max_attempts = 3 + extra_attempts
    wrong_attempts = 0
    while wrong_attempts < max_attempts:
        entered = input("Enter OTP (blank to skip): ").strip()
        if entered == "":
            print("Blank entry ignored; attempt not counted.")
            continue
        if entered == correct_otp:
            print("OTP verified successfully.")
            break
        wrong_attempts += 1
        print(f"Incorrect OTP. Attempts used: {wrong_attempts}/{max_attempts}")
    else:
        print("Account locked for 30 minutes.")

def verify_with_for(correct_otp="246810", extra_attempts=0):
    """for range design; blank entries are re-prompted within the same attempt."""
    max_attempts = 3 + extra_attempts
    for attempt in range(1, max_attempts + 1):
        while True:
            entered = input(f"Attempt {attempt}/{max_attempts} - Enter OTP: ").strip()
            if entered == "":
                print("Blank entry ignored; please enter an OTP.")
                continue
            break
        if entered == correct_otp:
            print("OTP verified successfully.")
            break
        print("Incorrect OTP.")
    else:
        print("Account locked for 30 minutes.")

def control_statement_demo():
    print("\nControl statement demonstration:")
    for value in ["", "skip", "work"]:
        if value == "":
            continue                 # skip this iteration
        if value == "skip":
            pass                     # placeholder: intentionally do nothing
        print("Processed:", value)
        if value == "work":
            break                    # terminate loop

if __name__ == "__main__":
    print("Choose 1 for while, 2 for for-loop demo, 3 for control statements")
    choice = input("Choice: ").strip()
    if choice == "1":
        verify_with_while()
    elif choice == "2":
        verify_with_for()
    else:
        control_statement_demo()
