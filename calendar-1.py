import calendar
import tkinter as tk
from tkinter import messagebox

def display_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        
        if month < 1 or month > 12:
            messagebox.showerror("Invalid Month", "Please enter a valid month (1-12).")
            return

        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.formatmonth(year, month)

        # Display the calendar in the text window
        calendar_text.delete(1.0, tk.END)
        calendar_text.insert(tk.END, month_calendar)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for year and month.")

# Creating the main window
root = tk.Tk()
root.title("Calendar Viewer")

# Label and entry for the year
tk.Label(root, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1)

# Label and entry for the month
tk.Label(root, text="Month (1-12):").grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

# Button to display the calendar
tk.Button(root, text="Show Calendar", command=display_calendar).grid(row=2, column=1)

# Text box to display the calendar
calendar_text = tk.Text(root, height=10, width=20)
calendar_text.grid(row=3, column=0, columnspan=2)

# tkinter main loop
root.mainloop()