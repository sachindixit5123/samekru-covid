import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
from datetime import datetime
import time


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

def execute_all_statistics(country_name, statistic):
    # Placeholder for function logic
    print(f"Executing All Statistics for {country_name} - {statistic}")

def execute_countrylist_stats(country_name, start_date, end_date, query):
    # Execute mapper.py
        # Convert start_date and end_date from string to datetime objects
    # start_date_obj = datetime.strptime(start_date, '%d-%m-%Y')
    # end_date_obj = datetime.strptime(end_date, '%d-%m-%Y')
    
    
    command = "python3 /home/sachin/Desktop/Project/mod2/mapper.py {} {} {} {} | sort -n | python3 /home/sachin/Desktop/Project/mod2/combiner.py | sort -n | python3 /home/sachin/Desktop/Project/mod2/reducer.py > /home/sachin/Desktop/Project/mod2/result.txt".format(country_name, start_date, end_date, query)
    subprocess.run(command, check=True) 

    time.sleep(5)
       
    # Assuming reducer.py generates 'output.txt' based on provided dates
    # Read and display the output from reducer_output.txt
    try:
        with open('/home/sachin/Desktop/Project/mod2/result.txt', 'r') as file:
            output_content = file.read()
            # Ensure the result_text widget is cleared before inserting new content
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, output_content)
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: result.txt not found.\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error reading reducer_output.txt: {str(e)}\n")








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

def execute_countrywise_news(country_name):
    # Execute mapper.py
    mapper_command = ["python3", "country_range.py", country_name]
    subprocess.run(mapper_command, check=True)

    try:
        with open('newsrange.txt', 'r') as file:
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


def execute_more(country_name, start_date, end_date ):
    # Execute mapper.py
    mapper_command = ["python3", "country_news.py", country_name, start_date, end_date]
    subprocess.run(mapper_command, check=True)

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

def execute_jaccard(country_name, start_date, end_date ):
    # Execute mapper.py
    mapper_command = ["python3", "jaccard.py", country_name, start_date, end_date]
    subprocess.run(mapper_command, check=True)

    try:
        with open('jaccardoutput.txt', 'r') as file:
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


def show_main_menu():
    clear_frame()  # Clear the current GUI state
    # Re-initialize the main menu buttons
    initialize_main_buttons()

def initialize_main_buttons():
    # Buttons for Worldometer Covid Statistics and Wikipedia Covid News
    worldometer_button = ttk.Button(main_frame, text="Worldometer Covid Statistics", command=show_worldometer_stats)
    worldometer_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    wikipedia_button = ttk.Button(main_frame, text="Wikipedia Covid News", command=show_wikipedia_news)
    wikipedia_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    exit_button = ttk.Button(main_frame, text="Exit", command=exit_gui)
    exit_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)


def setup_worldometer_gui():
    clear_frame()
    ttk.Label(main_frame, text="Worldometer Covid Statistics", font=('Arial', 16)).pack(pady=10)

    # Frame for Country Name and Statistics selection
    country_stat_frame = tk.Frame(main_frame)
    country_stat_frame.pack(pady=10, fill=tk.X)

    ttk.Label(country_stat_frame, text="Enter Country Name:").pack(side=tk.LEFT, padx=5)
    country_name_entry = ttk.Entry(country_stat_frame)
    country_name_entry.pack(side=tk.LEFT, padx=5)

    statistics_options = {
        "Total cases": "a", "Active cases": "b", "Total deaths": "c",
        "Total recovered": "d", "Total tests": "e", "Death/million": "f",
        "Tests/million": "g", "New case": "h", "New death": "i", "New recovered": "j"
    }
    # For the statistics dropdown
    

    statistic_var = tk.StringVar()
    statistics_dropdown = ttk.Combobox(country_stat_frame, textvariable=statistic_var, values=list(statistics_options.keys()))
    statistics_dropdown.pack(side=tk.LEFT, padx=(2, 10))
    tk.Label(country_stat_frame, text="Choose Query:").pack(side=tk.LEFT, padx=(10, 2))  # Adjust padding as needed
    statistics_dropdown.pack(side=tk.LEFT, padx=(2, 10))  # Adjust padding as needed
    all_stats_button = ttk.Button(country_stat_frame, text="All Statistics",
                                  command=lambda: execute_all_statistics(country_name_entry.get(), query_to_letter[statistic_var.get()]))
    all_stats_button.pack(side=tk.LEFT, padx=5)

    # Frame for Dates and Country List Statistics selection
    date_query_frame = tk.Frame(main_frame)
    date_query_frame.pack(pady=10, fill=tk.X)

    ttk.Label(date_query_frame, text="Enter Start Date (dd-mm-yyyy):").pack(side=tk.LEFT, padx=5)
    start_date_entry = ttk.Entry(date_query_frame)
    start_date_entry.pack(side=tk.LEFT, padx=5)

    ttk.Label(date_query_frame, text="Enter End Date (dd-mm-yyyy):").pack(side=tk.LEFT, padx=5)
    end_date_entry = ttk.Entry(date_query_frame)
    end_date_entry.pack(side=tk.LEFT, padx=5)

    country_list_options = {"% Change-active cases": "a", "% Change-daily death" : "b",
                            "% Change-new recovered" : "c", "% Change-new cases" : "d",
                            "Closest country" : "e"}
    query_var = tk.StringVar()
    query_dropdown = ttk.Combobox(date_query_frame, textvariable=query_var, values=list(country_list_options.keys()))
    query_dropdown.pack(side=tk.LEFT, padx=(2, 10))  # Adjust padding as needed
    tk.Label(date_query_frame, text="Choose Query:").pack(side=tk.LEFT, padx=(10, 2))  # Adjust padding as needed
    # query_dropdown.pack(side=tk.LEFT, padx=(2, 10))  # Adjust padding as needed
    country_list_stats_button = ttk.Button(date_query_frame, text="Country List Statistics",
                                       command=lambda: execute_countrylist_stats(country_name_entry.get(), start_date_entry.get(), end_date_entry.get(), country_list_options[query_var.get()]))
    country_list_stats_button.pack(side=tk.LEFT, padx=5)

    # Go Back Button
    go_back_button = ttk.Button(main_frame, text="Go Back", command=show_main_menu)
    go_back_button.pack(side=tk.BOTTOM, pady=5)

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

    countrywise_button = ttk.Button(input_frame, text="Countrywise News Range", command=lambda: execute_countrywise_news(country_name_entry.get())) #, start_date_entry.get(), end_date_entry.get()))
    countrywise_button.grid(row=2, column=2, padx=5, pady=10)

   
   # Adding the More Country News button
   

    bottom_frame = tk.Frame(main_frame)
    bottom_frame.pack(fill=tk.X, pady=5)

    more_country_news_button = ttk.Button(bottom_frame, text="More Country News", command=lambda: execute_more(country_name_entry.get(), start_date_entry.get(), end_date_entry.get()))
    more_country_news_button.pack(side=tk.LEFT, padx=10)

    jaccard_button = ttk.Button(bottom_frame, text="Jaccard Similarity", command=lambda: execute_jaccard(country_name_entry.get(), start_date_entry.get(), end_date_entry.get()))
    jaccard_button.pack(side=tk.LEFT, padx=10)  # Changed side to tk.LEFT for consistency

    go_back_button = ttk.Button(bottom_frame, text="Go Back", command=show_main_menu)
    go_back_button.pack(side=tk.LEFT, padx=10)

    exit_button = ttk.Button(bottom_frame, text="Exit", command=exit_gui)
    exit_button.pack(side=tk.RIGHT, padx=10)
 

if __name__ == "__main__":
    # Main window setup
    root = tk.Tk()
    root.title("COVID Data and News Query GUI")

    # Main frame setup
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    initialize_result_text()  # Initialize the result text area
    initialize_main_buttons()  # Initialize the main menu buttons
    
    root.mainloop()
