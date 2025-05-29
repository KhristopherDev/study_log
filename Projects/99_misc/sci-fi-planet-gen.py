import random

prefixes = ["Zor", "Xan", "Vel", "Tra", "Or", "Yel", "Drak", "Mor", "Ael", "Lun"]
suffixes = ["thar", "ion", "aris", "os", "mir", "ul", "ex", "ium", "ae", "ox"]
themes = ["Prime", "Minor", "Nova", "Secundus", "Ultima", "V", "VII", "Zeta", "X", "Delta"]

def generate_planet_name():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    theme = random.choice(themes)
    return f"{prefix}{suffix} {theme}"

def main():
    print("Random Sci-Fi Planet Name Generator\n")
    for _ in range(10):
        print(f"- {generate_planet_name()}")

if __name__ == "__main__":
    main()