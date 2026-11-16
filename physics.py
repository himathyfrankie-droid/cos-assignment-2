# PHYSICS CALCULATOR

# 1. PRESSURE
def pressure():
    print("\n--- PRESSURE ---")

    force = float(input("Enter force: "))
    area = float(input("Enter area: "))

    if area == 0:
        print("Area cannot be zero.")
    else:
        P = force / area
        print("Pressure =", P, "Pa")


# 2. POWER
def power():
    print("\n--- POWER ---")

    work = float(input("Enter work done: "))
    time = float(input("Enter time: "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        P = work / time
        print("Power =", P, "Watts")


# 3. POTENTIAL ENERGY
def potential_energy():
    print("\n--- POTENTIAL ENERGY ---")

    mass = float(input("Enter mass: "))
    gravity = float(input("Enter gravitational acceleration: "))
    height = float(input("Enter height: "))

    PE = mass * gravity * height
    print("Potential Energy =", PE, "Joules")


# 4. OHM'S LAW
def ohms_law():
    print("\n--- OHM'S LAW ---")

    current = float(input("Enter current: "))
    resistance = float(input("Enter resistance: "))

    V = current * resistance
    print("Voltage =", V, "Volts")


# 5. HEAT ENERGY
def heat_energy():
    print("\n--- HEAT ENERGY ---")

    mass = float(input("Enter mass: "))
    specific_heat = float(input("Enter specific heat capacity: "))
    temperature_change = float(input("Enter temperature change: "))

    Q = mass * specific_heat * temperature_change
    print("Heat Energy =", Q, "Joules")


# MAIN PROGRAM

while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Pressure")
    print("2. Power")
    print("3. Potential Energy")
    print("4. Ohm's Law")
    print("5. Heat Energy")

    choice = input("\nChoose an operation (1-5): ")

    if choice == "1":
        pressure()

    elif choice == "2":
        power()

    elif choice == "3":
        potential_energy()

    elif choice == "4":
        ohms_law()

    elif choice == "5":
        heat_energy()

    else:
        print("Invalid choice!")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Physics Calculator!")
        break