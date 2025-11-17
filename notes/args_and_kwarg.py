# MH 2nd *args and **kwargs notes

"""def hello(name = "Owie", age = "13"):
    return f"Hello {name} you are {age}"

print(hello(name = "Mirai", age = 15))"""

def hello(*names, **last):
    for name in names:
        if name == "Vivi" or "Irene":
            print(f"Hello {name} {last['blast']}")
        else:
            print(f"Hello {name} {last['hlast']}")

hello("Mirai", "Owie", "Irene", "Vivi", blast = "Bradbury", hlast = "Hsiao")
