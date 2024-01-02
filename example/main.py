# canoe.py
class Canoe:
    def __init__(self, number, color):
        self.number = number
        self.color = color


# Create a list of Canoe instances
canoe_list = [
    Canoe(number=1, color="red"),
    Canoe(number=2, color="blue"),
    Canoe(number=3, color="green"),
    # Add more instances as needed
]

# Print the first canoe (index 0) from the list
index_to_print = 0
if 0 <= index_to_print < len(canoe_list):
    selected_canoe = canoe_list[index_to_print]
    print(f"Canoe {selected_canoe.number} is {selected_canoe.color}.")
else:
    print(f"Index {index_to_print} is out of range.")