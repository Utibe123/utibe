def velocity_calc():
    s = float(input("Enter displacement: "))
    t = float(input("Enter time: "))
    v = s / t
    print(f"Velocity = {v} m/s")


def acceleration_calc():
    v = float(input("Enter velocity: "))
    t = float(input("Enter time: "))
    a = v / t
    print(f"Acceleration = {a} m/s^2")


def work_calc():
    f = float(input("Enter force: "))
    d = float(input("Enter distance: "))
    w = f * d
    print(f"Work done = {w} J")


def force_calc():
    m = float(input("Enter mass: "))
    a = float(input("Enter acceleration: "))
    f = m * a
    print(f"Force = {f} N")


def impulse_calc():
    f = float(input("Enter force: "))
    t = float(input("Enter time: "))
    i = f * t
    print(f"Impulse = {i} Ns")


options = {
    "a": velocity_calc,
    "b": acceleration_calc,
    "c": work_calc,
    "d": force_calc,
    "e": impulse_calc
}

print("Choose a formula:")
print("a - Velocity")
print("b - Acceleration")
print("c - Work")
print("d - Force")
print("e - Impulse")

choice = input("Enter a, b, c, d, or e: ").lower()

if choice in options:
    options[choice]()
else:
    print("Invalid option selected.")
