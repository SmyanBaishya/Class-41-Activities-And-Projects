# Import necessary libraries
from tkinter import *

# Function to convert inches to centimeters
def convert():
  # Get the value from the input field
  inches = float(entry.get())

  # Calculate the length in centimeters
  cm = inches * 2.54

  # Display the result in the output label
  result_label.config(text=str(inches) + " inches is equal to " + str(cm) + " centimeters")

# Create the main window
root = Tk()
root.title("Length Converter")

# Create the input label
input_label = Label(root, text="Enter length in inches:")
input_label.pack()

# Create the input field
entry = Entry(root)
entry.pack()

# Create the conversion button
convert_button = Button(root, text="Convert", command=convert)
convert_button.pack()

# Create the output label
result_label = Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()

# CODE DOES NOT WORK ON VSC, GO TO REPLIT > TKINTER.