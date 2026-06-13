import datetime
from utils import add, subtract

def main():
    print("Name: Noor Mohammed Taief")
    print(f"Today's date: {datetime.date.today()}")

    print("\n--- Calculator Tests ---")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")

if __name__ == "__main__":
    main()