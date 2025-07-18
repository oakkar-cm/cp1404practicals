"""
Hexadecimal colour lookup
"""


COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "cornflowerblue": "#6495ed",
                 "hotpink": "#ff69b4", "palevioletred": "#db7093",
                 "mediumorchid": "#ba55d3", "darkslategray": "#2f4f4f",
                 "seagreen": "#2e8b57", "goldenrod": "#daa520",
                 "mistyrose": "#ffe4e1", "slateblue": "#6a5acd"}

maximum_colour_length = max(len(colour_name) for colour_name in COLOUR_TO_HEX.keys())

for colour_name, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour_name:<{maximum_colour_length}} is {hex_code}")
print()

colour_name = input("Enter short state: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid short state")
    hex_code = input("Enter short state: ").lower()