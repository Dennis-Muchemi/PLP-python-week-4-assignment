#WEEK 4 ASSIGNMENT
#Function to modify the content of the file. In this case, we'll convert it to uppercase
def modify_content(content):
    return content.upper()

def main():
    # Ask the user for the filename to read
    input_file = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
            print("File read successfully.")
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Define the output filename
        output_file = f"modified_{input_file}"
        
        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            print(f"Modified content written to {output_file}.")
    
    # Handling errors
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_file}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
