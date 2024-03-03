
def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. Statistics")
        print("2. News")
        print("3. Exit")
        main_choice = input("Enter choice: ")

        if main_choice == '1':
            statistics_menu()
        elif main_choice == '2':
            news_menu()
        elif main_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-3.")

def statistics_menu():
    while True:
        print("\nSTATISTICS MENU")
        print("1a. All Statistics")
        print("1b. Country List Stats")
        print("1c. Go Back to previous Menu")
        stats_choice = input("Enter choice: ")

        if stats_choice == '1a':
            all_statistics()
        elif stats_choice == '1b':
            country_list_stats()
        elif stats_choice == '1c':
            break
        else:
            print("Invalid choice. Please enter a valid option (1a, 1b, 1c).")

def all_statistics():
    country_name = input("Enter Country Name: ")
    print("Options for", country_name)
    print("a. Total cases")
    print("b. Active cases")
    # Continue for other options as defined
    # Implement the functionality for each option

def country_list_stats():
    country_name = input("Enter Country Name: ")
    print("Options for", country_name)
    print("a. Active cases")
    # Continue for other options as defined
    # Implement the functionality for each option

def news_menu():
    while True:
        print("\nNEWS MENU")
        print("2a. Responses")
        print("2b. Timeline")
        print("2c. Countrywise News")
        print("2d. Go back to previous Menu")
        news_choice = input("Enter choice: ")

        if news_choice == '2a':
            responses()
        elif news_choice == '2b':
            timeline()
        elif news_choice == '2c':
            countrywise_news()
        elif news_choice == '2d':
            break
        else:
            print("Invalid choice. Please enter a valid option (2a, 2b, 2c, 2d).")

def responses():
    # Implement functionality here
    time_range = input("Enter Time range: ")
    print("Responses for", time_range)

def timeline():
    # Implement functionality here
    time_range = input("Enter Time range: ")
    print("Timeline for", time_range)

def countrywise_news():
    # Implement functionality here
    country_name = input("Enter Country Name: ")
    time_range = input("Enter Time Range: ")
    print(f"Countrywise News for {country_name} from {time_range}")

if __name__ == "__main__":
    main_menu()
