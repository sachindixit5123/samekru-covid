import tkinter as tk
from tkinter import ttk, messagebox

def show_worldometer_stats():
    clear_frame()
    # Label
    ttk.Label(main_frame, text="Enter Country Name:").grid(row=0, column=0, padx=10, pady=10)
    country_entry = ttk.Entry(main_frame)
    country_entry.grid(row=0, column=1, padx=10, pady=10)

    # Date range
    ttk.Label(main_frame, text="Start Date (dd-mm-yyyy):").grid(row=1, column=0, padx=10, pady=10)
    start_date_entry = ttk.Entry(main_frame)
    start_date_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(main_frame, text="End Date (dd-mm-yyyy):").grid(row=2, column=0, padx=10, pady=10)
    end_date_entry = ttk.Entry(main_frame)
    end_date_entry.grid(row=2, column=1, padx=10, pady=10)

    # Button to execute query
    execute_button = ttk.Button(main_frame, text="Execute Query", command=lambda: execute_query(country_entry.get(), start_date_entry.get(), end_date_entry.get()))
    execute_button.grid(row=3, column=0, columnspan=2, pady=10)

def show_wikipedia_news():
    clear_frame()
    # Label for country name input
    ttk.Label(main_frame, text="Enter Country Name:").grid(row=0, column=0, padx=10, pady=10)
    country_entry = ttk.Entry(main_frame)
    country_entry.grid(row=0, column=1, padx=10, pady=10)

    # Date range input
    ttk.Label(main_frame, text="Start Date (dd-mm-yyyy):").grid(row=1, column=0, padx=10, pady=10)
    start_date_entry = ttk.Entry(main_frame)
    start_date_entry.grid(row=1, column=1, padx=10, pady=10)
    
    ttk.Label(main_frame, text="End Date (dd-mm-yyyy):").grid(row=2, column=0, padx=10, pady=10)
    end_date_entry = ttk.Entry(main_frame)
    end_date_entry.grid(row=2, column=1, padx=10, pady=10)

    # Button to execute query
    execute_button = ttk.Button(main_frame, text="Execute News Query", command=lambda: execute_news_query(country_entry.get(), start_date_entry.get(), end_date_entry.get()))
    execute_button.grid(row=3, column=0, columnspan=2, pady=10)

def clear_frame():
    for widgets in main_frame.winfo_children():
        widgets.destroy()

def execute_news_query(country, start_date, end_date):
    # Placeholder for news query execution logic
    messagebox.showinfo("News Query Executed", f"News query executed for {country} from {start_date} to {end_date}")

def execute_query(country, start_date, end_date):
    # Placeholder for query execution logic
    messagebox.showinfo("Query Executed", f"Query executed for {country} from {start_date} to {end_date}")

# Create the main window
root = tk.Tk()
root.title("COVID Data and News Query GUI")

# Create a frame to contain the module components
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Buttons to select modules
worldometer_button = ttk.Button(root, text="Worldometer Covid Statistics", command=show_worldometer_stats)
worldometer_button.pack(side=tk.TOP, pady=(0, 10))

wikipedia_button = ttk.Button(root, text="Wikipedia Covid News", command=show_wikipedia_news)
wikipedia_button.pack(side=tk.TOP, pady=(0, 20))

# Run the application
root.mainloop()





   
# def execute_script(script_path, args):
#     # script_path: Path to the Python script
#     # args: List of arguments to pass to the script
#     command = ["python", script_path] + args
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     output, error = process.communicate()
    
#     if process.returncode == 0:
#         result_text.insert(tk.END, output)
#     else:
#         result_text.insert(tk.END, f"Error: {error}")
