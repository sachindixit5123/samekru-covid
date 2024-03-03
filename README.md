# Project Readme: COVID-19 Data Analysis and Information Retrieval

## Module 1: Crawling Worldometers Website

### Purpose
Module 1 focuses on crawling the Worldometer website to extract COVID-19 statistics worldwide, continent-wise, and country-wise.

### Instructions
1. Use the provided file `worldometers_countrylist.txt` with continent-wise country names.
2. Write a Python code to save HTML pages of the main URL and individual country pages.
3. Create a grammar to extract various COVID-19 statistics for any country/continent/world based on yesterday’s data and store them in text files.

## Module 2: Crawling Wikipedia COVID-19 Timeline

### Purpose
Module 2 involves crawling the Wikipedia COVID-19 timeline page to extract worldwide news and responses.

### Instructions
1. Extract worldwide news and responses for all times.
2. Store the results in suitable text files, organized by year and month.
3. For specific countries (India, Australia, Malaysia, England, Singapore), extract news information and store it with dates.

## Module 3.1: Addressing Queries of Worldometer COVID Statistics

### Purpose
Module 3.1 uses data from Module 1 to address user queries through a MapCombineReduce paradigm.

### Instructions
1. Integrate MapCombineReduce inside the Python code to retrieve query outputs.
2. Answer queries using yesterday’s data for each country, including percentages of total world cases.
3. Address specific queries with time ranges and provide change percentages and the closest country.

## Module 3.2: Addressing Queries of Wikipedia COVID News

### Purpose
Module 3.2 uses data from Module 2 to address user queries through a MapCombineReduce paradigm.

### Instructions
1. Retrieve query outputs using the MapCombineReduce paradigm for worldwide news and responses.
2. Provide information on available news dates for a specific country.
3. Extract news for a given country and date range.
4. Calculate Jaccard similarity for the closest country based on news content.

## Module 4: Combining Modules 3.1 and 3.2

### Purpose
Module 4 combines the functionalities of Modules 3.1 and 3.2 in a menu-driven method.

### Instructions
1. Design a user-friendly menu to access either module.
2. Print the date of the last data extraction in the menu.
3. Store information extraction results in text files based on design decisions.
4. Use the MapCombineReduce paradigm to display query results.

## General Instructions

1. **Dynamic Queries:** Note that queries are dynamic; implement a user-friendly design to handle varying queries.
2. **Data Storage:** Clearly document how information is stored in text files based on your design decisions.

Feel free to adapt and modify the instructions based on your specific design choices and preferences. Good luck with your project!
