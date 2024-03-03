import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess


def initialize_result_text():
    global result_text  # Declare result_text as global to ensure it's accessible throughout the script
    result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
    result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def show_worldometer_stats():
    clear_frame()
    setup_worldometer_gui()

def show_wikipedia_news():
    clear_frame()
    setup_wikipedia_gui()

def clear_frame():
    for widgets in main_frame.winfo_children():
        widgets.destroy()
    initialize_result_text()  # Re-initialize result text after clearing the frame

def exit_gui():
    root.destroy()

def setup_worldometer_gui():
    # Setup GUI for Worldometer Covid Statistics
    ttk.Label(main_frame, text="Worldometer Covid Statistics", font=('Arial', 16)).pack(pady=10)
    # Add more GUI components here as per your requirements


def execute_timeline(start_date, end_date):
    # Execute mapper.py
    mapper_command = ["python3", "mapper_news.py"]
    subprocess.run(mapper_command, check=True)

    # Modify the reducer_command to pass start and end dates as arguments to reducer.py
    reducer_command = ["python3", "reducer_news.py", start_date, end_date]
    subprocess.run(reducer_command, check=True)
    
    # Assuming reducer.py generates 'output.txt' based on provided dates
    # Read and display the output from reducer_output.txt
    try:
        with open('reducer_output.txt', 'r') as file:
            output_content = file.read()
            # Ensure the result_text widget is cleared before inserting new content
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, output_content)
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: reducer_output.txt not found.\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error reading reducer_output.txt: {str(e)}\n")

def execute_responses(start_date, end_date):
    # Execute mapper.py
    mapper_command = ["python3", "mapper_response.py"]
    subprocess.run(mapper_command, check=True)

    # Modify the reducer_command to pass start and end dates as arguments to reducer.py
    reducer_command = ["python3", "reducer_response.py", start_date, end_date]
    subprocess.run(reducer_command, check=True)
    
    # Assuming reducer.py generates 'output.txt' based on provided dates
    # Read and display the output from reducer_output.txt
    try:
        with open('reducer_output.txt', 'r') as file:
            output_content = file.read()
            # Ensure the result_text widget is cleared before inserting new content
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, output_content)
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: reducer_output.txt not found.\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error reading reducer_output.txt: {str(e)}\n")

def execute_countrywise_news(country_name, start_date, end_date):
    # Placeholder for executing Countrywise News functionality
    print("Execute Countrywise News functionality here")

def show_main_menu():
    clear_frame()  # Clear the current GUI state
    # Re-initialize the main menu buttons
    initialize_main_buttons()

def setup_wikipedia_gui():
    clear_frame()

    # Top Label
    ttk.Label(main_frame, text="Wikipedia Covid News", font=('Arial', 16)).pack(pady=10)

    # Create a frame for the input fields and buttons
    input_frame = tk.Frame(main_frame)
    input_frame.pack(pady=20)

    # Input fields shared by Responses and Timeline
    ttk.Label(input_frame, text="Enter Start Date (dd-mm-yyyy):").grid(row=0, column=0, padx=5)
    start_date_entry = ttk.Entry(input_frame)
    start_date_entry.grid(row=1, column=0, padx=5)

    ttk.Label(input_frame, text="Enter End Date (dd-mm-yyyy):").grid(row=0, column=1, padx=5)
    end_date_entry = ttk.Entry(input_frame)
    end_date_entry.grid(row=1, column=1, padx=5)

    # Input field for Countrywise News
    ttk.Label(input_frame, text="Enter Country Name:").grid(row=0, column=2, padx=5)
    country_name_entry = ttk.Entry(input_frame)
    country_name_entry.grid(row=1, column=2, padx=5)

    # Buttons
    responses_button = ttk.Button(input_frame, text="Responses", command=lambda: execute_responses(start_date_entry.get(), end_date_entry.get()))
    responses_button.grid(row=2, column=0, padx=5, pady=10)

    timeline_button = ttk.Button(input_frame, text="Timeline", command=lambda: execute_timeline(start_date_entry.get(), end_date_entry.get()))
    timeline_button.grid(row=2, column=1, padx=5, pady=10)

    countrywise_button = ttk.Button(input_frame, text="Countrywise News", command=lambda: execute_countrywise_news(country_name_entry.get(), start_date_entry.get(), end_date_entry.get()))
    countrywise_button.grid(row=2, column=2, padx=5, pady=10)

    # Bottom Buttons Frame
    bottom_frame = tk.Frame(main_frame)
    bottom_frame.pack(fill=tk.X, pady=5)

    go_back_button = ttk.Button(bottom_frame, text="Go Back", command=show_main_menu)  # Define `show_main_menu`
    go_back_button.pack(side=tk.LEFT, padx=10)

    exit_button = ttk.Button(bottom_frame, text="Exit", command=exit_gui)
    exit_button.pack(side=tk.RIGHT, padx=10)
 
# Main window setup
root = tk.Tk()
root.title("COVID Data and News Query GUI")

# Main frame setup
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# initialize_result_text()

# Buttons for Worldometer Covid Statistics and Wikipedia Covid News
worldometer_button = ttk.Button(root, text="Worldometer Covid Statistics", command=show_worldometer_stats)
worldometer_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

wikipedia_button = ttk.Button(root, text="Wikipedia Covid News", command=show_wikipedia_news)
wikipedia_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

exit_button = ttk.Button(root, text="Exit", command=exit_gui)
exit_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Remember to add the result_text widget to display script outputs, if not already present
result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


root.mainloop()
