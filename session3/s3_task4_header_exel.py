'''
Session 3:
    Write a Python program to parse .h header file and read all prototypes of functions and insert it into excel sheet with unique ID start with IDX0
'''
import re
from openpyxl import Workbook

def extract_function_prototypes(header_file):
    prototypes = []
    with open(header_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'^\s*([\w\s\*]+)\s+(\w+)\s*\((.*?)\)', line)
            if match:
                return_type, function_name, parameters = match.groups()
                prototypes.append((return_type.strip(), function_name.strip(), parameters.strip()))
    return prototypes

def create_excel_sheet(prototypes):
    wb = Workbook()
    ws = wb.active
    ws.append(['ID', 'Return Type', 'Function Name', 'Parameters'])

    for idx, (return_type, function_name, parameters) in enumerate(prototypes):
        unique_id = f'IDX{idx}'
        ws.append([unique_id, return_type, function_name, parameters])

    wb.save('function_prototypes.xlsx')

def main():
    header_file = 'your_header_file.h'  # Replace with your header file path
    prototypes = extract_function_prototypes(header_file)
    create_excel_sheet(prototypes)
    print("Function prototypes extracted and saved to 'function_prototypes.xlsx'.")

if __name__ == "__main__":
    main()
