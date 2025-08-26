def modify_file_content(input_file, output_file):
    """
    Read content from input_file, modify it, and write to output_file.
    
    Parameters:
        input_file (str): Name of the input file
        output_file (str): Name of the output file
    """
    try:
        # The input file
        with open(input_file, "r") as file:
            content = file.read()  
        
        # Modify the content 
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_file, "w") as file:
            file.write(modified_content)
        
        print(f"Successfully read '{input_file}' and wrote modified content to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}'. Check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Prompt user for input filename
try:
    input_filename = input("Enter the name of the input file (e.g., example.txt): ")
    # Generate output 
    output_filename = "modified_" + input_filename
    
    # Call the function to read, modify, and write
    modify_file_content(input_filename, output_filename)

except ValueError:
    print("Error: Invalid input. Please enter a valid filename.")