"""Example of importing and using the milkrate module."""
import milkrate as mr

if __name__ == "__main__":
    print("Imported module rate:", mr.rate_per_litre(4.2, 8.7))
    print("Payout:", mr.payout(8.5, 4.2, 8.7))
