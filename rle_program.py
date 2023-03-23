from console_gfx import ConsoleGfx

# Hex <-> decimal dictionaries
from_hex = {"0": 0, "1":1, "2":2, "3":3, "4":4, "5": 5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e": 14, "f":15}
to_hex = {0: "0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

def print_menu(): # Prints menu in a single line for conciseness. Potential to make it multi-line if necessary for readibility
    print("\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")


def to_hex_string(data): # Turns a list into a hexadecimal string, works with both raw data and RLE
    output = ""

    for i in data:
        output += to_hex[i]

    return output


def count_runs(flat_data): # Returns the number of runs in a data list. Works with decimal and hex, but not together
    runs = 0
    current = flat_data[0]
    count = 1
    for i in range(1, len(flat_data)):
        if count == 15:
            count = 1
            runs += 1
        elif current != flat_data[i]:
            current = flat_data[i]
            count = 1
            runs += 1
        else:
            count += 1
    return runs + 1


def encode_rle(flat_data): # Turns a raw data list into a RLE list (no hex)
    rle_output = []
    current = flat_data[0]
    count = 1
    for i in range(1, len(flat_data)):
        if count == 15:
            rle_output.extend([count, current])
            current = flat_data[i]
            count = 1
        elif current != flat_data[i]:
            rle_output.extend([count, current])
            current = flat_data[i]
            count = 1
        else:
            count += 1
    rle_output.extend([count, current])
    return rle_output


def get_decoded_length(rle_data): # Returns the number of raw data values from a RLE list input
    length = 0
    for i in rle_data[::2]:
        length += i
    return length


def decode_rle(rle_data): # Turns a RLE list into a raw/decompressed list (no hex)
    rle_output = []
    for i in range(0, len(rle_data), 2):
        for j in range(0, rle_data[i]):
            rle_output.append(int(rle_data[i + 1]))
    return rle_output


def string_to_data(data_string): # Turns a plain hex string into a decimal list, can take raw or RLE data
    output = []
    for i in data_string:
        output.append(from_hex[i])
    return output


def to_rle_string(rle_data): # Turns a RLE decimal list into a RLE hex string, values are separated by ":"
    output = ""
    for i in range(len(rle_data) // 2):
        output += f"{rle_data[i * 2]}{to_hex[rle_data[i * 2 + 1]]}"
        if i < len(rle_data) // 2 - 1:
            output += ":"
    return output


def string_to_rle(rle_string): # Turns a RLE hex string with ":" into a RLE decimal list
    output = []
    global from_hex
    rle_list = rle_string.split(":")
    for i in range(len(rle_list)):
        try:
            output.append(int(rle_list[i][:-1]))
        except:
            output.append(from_hex[rle_list[i][:-1]])
        try:
            output.append(int(rle_list[i][-1]))
        except:
            output.append(from_hex[rle_list[i][-1]])
    return output


def main(): # Main function
    print("Welcome to the RLE image encoder!\n\nDisplaying Spectrum Image:") # Displays welcome message
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow) # Displays spectrum message

    while True: # Overarching True loop
        print_menu() # prompt the user for menu option

        string_input = input("\nSelect a Menu Option: ") # User inputs are saved as strings for data sanitization

        if string_input == "0": # Ends program
            exit()
        elif string_input == "1": # Prompts user for name of file then imports said file
            file_name = input("Enter name of file to load: ")
            file = ConsoleGfx.load_file(file_name)
        elif string_input == "2": # Loads test image then alerts user that it has been loaded
            print("Test image data loaded.")
            file = ConsoleGfx.test_image
        elif string_input == "3": # Allows user to input a hex RLE string with ":", converts input to a RLE list and saves it as "file"
            file = string_to_rle(input("Enter an RLE string to be decoded: "))
        elif string_input == "4": # Allows user to input a hex RLE string without ":", converts input to a RLE list and saves it as "file"
            file = string_to_data(input("Enter the hex string holding RLE data: "))
        elif string_input == "5": # Allows user to input a raw hex string, converts input to a RLE list and saves it as "file"
            file = encode_rle(string_to_data(input("Enter the hex string holding flat data: ")))
        elif string_input == "6": # Displays currently loaded file
            print("Displaying image...")
            ConsoleGfx.display_image(file)
        elif string_input == "7": # Outputs current file as a RLE hex string with ":"
            print(f"RLE representation: {to_rle_string(file)}")
        elif string_input == "8": # Outputs current file as a RLE hex string without ":"
            print(f"RLE hex values: {to_hex_string(file)}")
        elif string_input == "9": # Outputs current file as a raw hex string without ":"
            print(f"Flat hex values: {to_hex_string(decode_rle(file))}")
        else: # Error checking, invalid inputs return an error and reprint menu and prompt
            print("Error! Invalid input.")


if __name__ == "__main__":
    main() # Runs through a dedicated "main" function for simplicity