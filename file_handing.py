def read_and_modify_file():
    # Ask user for the input file name
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal file content successfully read.")
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
        return

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Define the output filename
    output_filename = f"modified_{input_filename}"

    try:
        # Attempt to write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"\nModified content written to '{output_filename}'.")
    except IOError:
        print(f"❌ Error: Could not write to the file '{output_filename}'.")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()
