# import time

# def faulty_calculator():
#     print("Welcome to the Faulty Calculator!")
#     input("Enter your calculation: ")
#     print("Processing...")
#     while True:
#         time.sleep(1)
#         print("Still processing...", end="\r")

# if __name__ == "__main__":
#     faulty_calculator()




import time

def faulty_calculator():
    print("Welcome to the Faulty Calculator!")
    print("Enter your mathematical expression (e.g., 2 + 2):")

    try:
        _ = input("> ")  # Takes input but does nothing with it
        print("Processing, please wait...")
        while True:
            time.sleep(1)  # Keeps the program running indefinitely
            print("Still calculating...")  
    except KeyboardInterrupt:
        print("\nOops! The calculator failed to respond. Try again later.")

faulty_calculator()
