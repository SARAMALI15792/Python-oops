import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except Exception as e:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Initialize GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Global variable for expression
expression = ""

# Entry widget for displaying the input/output
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20 bold", justify='right')
entry.pack(fill="both", ipadx=8, padx=10, pady=10)

# Buttons layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15 bold", relief="ridge", height=2, width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main event loop
root.mainloop()
