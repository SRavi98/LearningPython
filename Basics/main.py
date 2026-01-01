name = input("what's your name? ").strip().title()

if " " in name:
    first, last = name.split(" ")
else:
    first = name
    last = ""

print(f"Hello {first} {last}")