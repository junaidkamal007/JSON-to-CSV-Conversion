# JSON-to-CSV-Conversion

Problem Statement

Many data workflows involve exchanging information between different formats, especially JSON and CSV. These formats are widely used for APIs, spreadsheets, and data analysis tools. However, converting between JSON and CSV can be repetitive and error-prone if done manually, especially when the datasets are large.

This project solves that problem by providing a simple command-line tool that automatically converts JSON files (containing a list of objects) into CSV, and vice-versa, with minimal user input.

Features

Convert JSON → CSV

Convert CSV → JSON

Easy user interface in the command line

Validates file paths and reports errors gracefully

How to Run
Prerequisites

Make sure you have:

Python 3.6 or higher installed

The standard json, csv, and os modules (included with Python)

Running the Script

Clone or download this repository.

Open a terminal or command prompt.

Navigate to the project directory.

Run the script:

python your_script_name.py


Follow the on-screen menu:

Press 1 to convert a JSON file to CSV.

Press 2 to convert a CSV file to JSON.

Press 3 to exit.

You will be prompted for input and output file paths.

Example Usage

Convert JSON to CSV

Enter the JSON file path: students.json
Enter the CSV file path: employees.csv
Successfully converted JSON into CSV


Convert CSV to JSON

Enter the CSV file path: employees.csv
Enter the JSON file path: students.json
Successfully converted CSV into JSON

Design Decisions

User-friendly CLI Menu

A simple menu allows users to choose between the two conversion options or exit. This eliminates the need to remember command-line arguments.

Robust File Path Handling

The script checks if input files exist before processing them to avoid runtime errors. If the file does not exist, the user is notified.

Standard Library Only

No external dependencies are required. Using Python’s built-in json and csv modules keeps the project lightweight and portable.

JSON Structure Assumption

The JSON-to-CSV conversion assumes the JSON file contains a list of objects (dictionaries). Each object’s keys become column headers in the CSV. This simplifies the conversion logic while covering the most common use cases.

Readable Output

JSON output is formatted with indentation for readability when converting from CSV.

Limitations & Notes

The JSON-to-CSV converter expects a JSON array at the top level. Nested objects or inconsistent keys may result in unexpected output.

The CSV-to-JSON converter treats each row as a dictionary with headers as keys.

Future Improvements

Support for nested JSON structures

GUI version

Additional flags for batch processing
