print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠶⠟⠋⠻⣿⡗⠀⠀⠀⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠋⠁⠀⢀⣀⣤⣄⡀⠀⠘⠃⠀⠀⠀⣠⡀⠈⠻⣦⡀⠀⠀⠀⠀
⠀⠀⠀⣰⠏⢠⡄⠀⣴⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠘⠻⠃⠀⠀⠈⠻⣄⠀⠀⠀
⠀⠀⣼⣇⡀⠈⠁⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢹⣆⠀⠀
⠀⣸⡟⠛⠃⠀⠀⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⢀⣿⣶⡆⠀⠀⢿⡄⠀
⠀⣿⠁⠀⠀⠀⠀⠀⠈⠻⠿⣿⠿⠞⠋⠀⠀⠀⠀⠀⠀⠀⠿⠉⠁⠀⠀⢸⣇⠀
⠀⣿⠀⠀⣴⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⢴⠀⠀⠀⠀⠀⠀⠰⠆⢈⣿⠀
⠀⣿⡀⣰⣿⣿⣷⡀⠀⢀⣤⡄⠀⠀⠀⢰⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀
⠀⢸⣧⣿⣿⣿⣿⣷⣄⣾⣿⣿⡄⠀⢀⣿⣿⣿⣿⣿⣶⣶⣶⣶⣷⣤⣀⣾⠃⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



''')

print("Welcome to 'A night on the road'!")
input("Press Enter to start the game.")
input(
    "It's a closed night.\nA lovely couple travels by car in a lonely road.\nThe copilot sleeps."
)
input("You're low on gas, but a petrol station is near.")
input("Suddenly, a truck approaches your car.")
dodge = input(
    "Do you try to dodge the truck?\n(Type 'Y' for yes or 'N' for no) ")
partner = "d"

if dodge == "Y" or dodge == "y":
    print("You evade the truck.\nHowever a wheel blows off.")
    input("The copilot is severely injured :(")
    partner = "the copilot"
elif dodge == "N" or dodge == "n":
    print("The truck collides with the car.")
    input("Your partner is severely injured :(")
    partner = "your partner"

input("The car is broken down.")
help = input("Would you like to help " + partner +
             "?\n(Type 'Y' for yes or 'N' for no) ")

if help == "Y" or help == "y":
    input("You pick up " + partner +
          ".\nTogether, you walk to the petrol station.")
    print("You ended up together!")
elif help == "N" or help == "n":
    input("You leave " + partner + ".\nAlone, you walk to the petrol station.")
    print("You ended up alone!")
    print("Screw You!")
