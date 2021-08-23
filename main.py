

import tabula
import pyinputplus as pyip

def get_input_file():
    input_file = pyip.inputFilepath("Enter input pdf file root directory:\n>")
    ##For other menu choices
    global global_input_file
    global_input_file = input_file

    return input_file

def get_page_number():
    page_number = pyip.inputNum("Enter page number of the table within the pdf:\n>")
    return page_number

def get_area_coordinates():
    coordinates_split_string = pyip.inputRegex(r'(^(\d+(\.\d+|\d*),){3}(\d+(\.\d+|\d*))$)',
                            prompt="Input top,left,height,width (no spaces & with commas)\n>").split(",")
    top, left, height, width = [float(x) for x in coordinates_split_string]
    ##For other menu choices
    global global_area_coordinates
    global_area_coordinates = [top,left,top+height,left+width]

    return top, left, top+height, left+width

def get_output_file():
    output_file = pyip.inputFilepath("Enter output file path root directory:\n>")  # make sure its legit directory
    ##For other menu choices
    global global_output_file
    global_output_file = output_file
    return output_file

def find_file_name(file_path):
    output = 0
    for i in range(len(file_path)-1,-1,-1):
        if file_path[i] == '/' or file_path[i] == '\\':
            output = file_path[i+1:len(file_path)]
            break
    return output

def main_program(*args):
    if len(args) == 0:
        df = tabula.read_pdf(get_input_file(), stream=True, pages = get_page_number(), area = get_area_coordinates())
        df[0].to_excel(get_output_file(), index = False, header=True)
    elif len(args) == 2:
        df = tabula.read_pdf(args[0], stream=True, pages=get_page_number(), area=(args[1][0], args[1][1], args[1][2], args[1][3]))
        df[0].to_excel(get_output_file(), index=False, header=True)
    elif len(args) == 1:
        df = tabula.read_pdf(args[0], stream=True, pages=get_page_number(), area=get_area_coordinates())
        df[0].to_excel(get_output_file(), index=False, header=True)
    print(f'{find_file_name(global_output_file)} has been successfully produced!')



choice = 3
while choice != 4:
    if choice == 1:
        main_program(global_input_file, global_area_coordinates)
    elif choice == 2:
        main_program(global_input_file)
    elif choice == 3:
        main_program()

    choice = pyip.inputNum("Please choose following options:\n" ##can only be in a range
                           "1. Same input file & same coordinates\n"
                           "2. Same input file\n"
                           "3. Different input file.\n"
                           "4. Exit Program\n>"
                           , min = 1, max = 4) #make them choose between 1 - 4

print("Program has ended")


'''
USER FLOW
- Enter output path to be the same (e.g. /Users/Documents/) But not file name 
1. Work on Same pdf file, just enter different page number, different coordinates.
2. work on different pdf file
3. End program 
'''



