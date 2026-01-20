import os
import json
import csv
import sys

def display():
    print('welcome to the file converter')
    print('Press 1 to convert json into csv \n')
    print('Press 2 to convert csv into json \n')
    print('Press 3 to Exit \n')

    return input('Choose what you want to convert: ')

def json_to_csv():
    try:
        input_path = input("Enter the JSON file path: ").strip()

        if not os.path.exists(input_path):
           print('file does not exist....')
           return
        
        output_path = input('Enter the CSV file path').strip()

        with open(input_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        if isinstance(data, list) and len(data) > 0:
            headers = list(data[0].keys()) 

            with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)   
                writer.writeheader()
                writer.writerows(data)   

            print("Successfully converted JSON into CSV")

        else:
            print('ERROR JSON should be list of objects ')

    except Exception as e:
        print(f"Error during conversion: {str(e)}")

def csv_to_json():
    try:
        input_path = input("Enter the CSV file path: ").strip()

        if not os.path.exists(input_path):
           print('file does not exist....')
           return
        
        output_path = input('Enter the JSON file path: ').strip()

        data = []
        with open(input_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

            print("Successfully converted CSV into JSON")

    except Exception as e:
        print(f"ERROR in conversion {str(e)}")

def main():
    print("Welcome to JSON-CSV Converter!")    


    while True:

        choice = display()

        if choice == '1':
            json_to_csv()  

        elif choice == '2':
            csv_to_json()

        elif choice == '3':
            print("Thank you for using converter, Exiting")    
            break

        else:
            print("Invalid option choose 1, 2 or 3")   

        input("Press Enter to continue....")         

if __name__ == '__main__':
    main()                  





                    




    

