"""
FORMATTING STRINGS
"""

# It is a very basic and improper way to do it, but you can concatenate strings in a similar way to Excel using =CONCAT("X"&" "&"Y")
name = "Eduardo"
last_name = "Salcedo"
full_name = name + " " + last_name
print(full_name)

# However, the proper standard way to do it in Python is by using the string formatting operator: f"{x} {y}"
nombre_completo = f"{name} {last_name}"
print(nombre_completo)

# Keep in mind that, as long as the curly brackets remain inside a formatting operator like f"{}", you can manipulate its internal values quite freely.
nombre_completo2 = f"{name[0:2]} {last_name[:3]} {3+5+6+12-9-2}"
print(nombre_completo2)
