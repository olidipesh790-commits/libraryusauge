import pyjokes
 
# Part 1: display three different jokes
print("Here are three programming jokes:\n")
for number in range(1, 4):
    print(f"{number}. {pyjokes.get_joke()}")
 
# Part 2: keep showing jokes while the user answers "yes"
while True:
    answer = input("\nDo you want another joke? (yes/no): ").strip().lower()
    if answer == "yes":
        print(pyjokes.get_joke())
    else:
        print("Okay, goodbye!")
        break