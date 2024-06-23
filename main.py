# main.py
import scenario1
import scenario2

def main():
    while True:
        print("Choose a scenario to run:")
        print("1. Scenario 1")
        print("2. Scenario 2")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            scenario1.py.run()
        elif choice == '2':
            scenario2.py.run()
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

