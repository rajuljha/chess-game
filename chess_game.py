import tkinter as tk
import random
from pprint import pprint

# Create a chessboard class
class Chessboard(tk.Frame):
    def __init__(self, master, rows=8, columns=8, size=64):
        super().__init__(master)
        self.rows = rows
        self.columns = columns
        self.size = size
        self.cells = {}

        self.canvas = tk.Canvas(self, width=self.columns * self.size, height=self.rows * self.size)
        self.canvas.pack()

        self.cell_values = [[random.choice(["Heads", "Tails"]) for _ in range(self.columns)] for _ in range(self.rows)]

        # Create the chessboard grid
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = col * self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size

                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFFF", tags="cell")
                text = self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=self.cell_values[row][col], fill="black", tags="text")
                self.cells[(row, col)] = (cell, text)
                # self.canvas.tag_bind(cell, "<Button-1>", lambda event, r=row, c=col: self.toggle_cell(r, c))
                self.canvas.tag_bind(cell, "<Button-1>", lambda event, r=row, c=col: self.display_binary_number(r, c))

    def display_binary_number(self, row, col):
        binary_number = self.calculate_binary_number(row, col)
        binary_digit = self.calculate_binary_digit()
        xor_result = self.perform_xor(binary_digit, binary_number)
        
        print("Binary Number for Cell ({}, {}): {}".format(row + 1, col + 1, binary_number))
        print("Result of XOR operation on current cell and required key cell is: {}".format(xor_result))
        cell_number = self.find_cell_number(xor_result)
        print("Cell Number that needs to be flipped: {}".format(cell_number))
        print('##############################################')


    def calculate_binary_number(self, row, col):
        cell_number = row * self.columns + col
        binary_number = format(cell_number, '06b')
        return binary_number

    def perform_xor(self, binary_digit, binary_number):
        result = ""
        for d, n in zip(binary_digit, binary_number):
            if d == n:
                result += "0"
            else:
                result += "1"
        return result

    def find_cell_number(self, xor_result):
        parts = [int(d) for d in xor_result]
        cell_number = 0
        for i, part in enumerate(parts):
            if part == 1:
                cell_number += 2 ** (5 - i)
        return cell_number

    def toggle_cell(self, row, col):
        current_value = self.cell_values[row][col]
        new_value = "Tails" if current_value == "Heads" else "Heads"
        self.cell_values[row][col] = new_value
        self.canvas.itemconfig(self.cells[(row, col)][1], text=new_value)

    def highlight_part(self, part):
        for row in range(self.rows):
            for col in range(self.columns):
                cell_color = "#FFFFFF"  # Default color is white

                if part == 0:
                    if col % 2 == 1:
                        cell_color = "#E8E8E8"  # Part 1: Even number columns
                elif part == 1:
                    if col in (2, 3, 6, 7):
                        cell_color = "#FFFFCC"  # Part 2: 3rd and 4th, 7th and 8th columns
                elif part == 2:
                    if col >= 4:
                        cell_color = "#CCFFCC"  # Part 3: Last 4 columns
                elif part == 3:
                    if row % 2 == 1:
                        cell_color = "#C0C0C0"  # Part 4: Even number rows
                elif part == 4:
                    if row in (2, 3, 6, 7):
                        cell_color = "#FFFF66"  # Part 5: 3rd and 4th, 7th and 8th rows
                elif part == 5:
                    if row >= 4:
                        cell_color = "#66FF66"  # Part 6: Bottom 4 rows

                self.canvas.itemconfig(self.cells[(row, col)][0], fill=cell_color)

    def count_heads_in_part(self, part):
        count = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if part == 0:
                    if col % 2 == 1:
                        if self.cell_values[row][col] == "Heads":
                            count += 1
                elif part == 1:
                    if col in (2, 3, 6, 7):
                        if self.cell_values[row][col] == "Heads":
                            count += 1
                elif part == 2:
                    if col >= 4:
                        if self.cell_values[row][col] == "Heads":
                            count += 1
                elif part == 3:
                    if row % 2 == 1:
                        if self.cell_values[row][col] == "Heads":
                            count += 1
                elif part == 4:
                    if row in (2, 3, 6, 7):
                        if self.cell_values[row][col] == "Heads":
                            count += 1
                elif part == 5:
                    if row >= 4:
                        if self.cell_values[row][col] == "Heads":
                            count += 1
        return count

# NEW
    def calculate_binary_digit(self):
        binary_digit = ""
        for part in range(5, -1, -1):  # Reverse order from part 6 to part 1
            count = self.count_heads_in_part(part)
            if count % 2 == 0:
                binary_digit += "0"
            else:
                binary_digit += "1"
        return binary_digit

# Create the main window
root = tk.Tk()
root.title("Chessboard")

# Create the chessboard widget
chessboard = Chessboard(root)
chessboard.pack()

# Create buttons to highlight each part of the board
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_labels = ["Part 1", "Part 2", "Part 3", "Part 4", "Part 5", "Part 6"]
buttons = []
for i, label in enumerate(button_labels):
    button = tk.Button(button_frame, text=label, width=10)
    button.configure(command=lambda part=i: highlight_and_count(part))
    button.pack(side=tk.LEFT, padx=5)
    buttons.append(button)

# Function to highlight a part and display the count of "Heads" in that part
def highlight_and_count(part):
    chessboard.highlight_part(part)
    count = chessboard.count_heads_in_part(part)
    print("Number of Heads in Part {}: {}".format(part + 1, count))

    binary_digit = chessboard.calculate_binary_digit()
    print("Binary Digit corresponding to board parity is:", binary_digit)

# Start the main event loop
root.mainloop()
