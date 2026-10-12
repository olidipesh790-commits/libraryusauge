from colorama import Fore, Style, init

init(autoreset=True)

name = input("Enter student name: ").strip()

while True:
    try:
        marks = float(input("Enter marks: "))
        break
    except ValueError:
        print(Fore.YELLOW + "Please enter a number.")

print(Fore.CYAN + f"Student: {name}")
print(f"Marks: {marks}")

if marks >= 40:
    print(Fore.GREEN + "Result: PASS")
else:
    print(Fore.RED + "Result: FAIL")