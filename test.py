import re

# Function to extract filenames and content from the input text
def extract_data_from_text(text):
    # Regular expression to match the pattern
    pattern = r'\[start\](.*?)\[/start\](.*?)\[end\]\1\[/end\]'
    
    # Find all matches in the input text
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Organize matches into a list of lists
    result = [[filename.strip(), content.strip()] for filename, content in matches]
    
    return result

# Read content from 'test.txt'
with open('test.txt', 'r') as file:
    file_content = file.read()

# Extract data from the file content
extracted_data = extract_data_from_text(file_content)


extracted_content = []
# Print the result
for item in extracted_data:
    # print(item)
    extracted_content.append(item)

print(extracted_content[2])




# import re

# # Your input string
# input_string = """
# [start]biodata1[/start]
# fullname: JohnDee
# age: 28
# [end]biodata1[/end]
# [start]biodata5[/start]
# This is a story of
# a flower
# [end]biodata5[/end]
# [start]biodata6[/start]
# document content for biodata6

# [end]biodata6[/end]

# """

# # Regular expression to match the pattern
# pattern = r'\[start\](.*?)\[/start\](.*?)\[end\]\1\[/end\]'

# # Find all matches in the input string
# matches = re.findall(pattern, input_string, re.DOTALL)

# # Organize matches into a list of lists
# result = [[filename.strip(), content.strip()] for filename, content in matches]

# # Print the result
# for item in result:
#     print(item)



# import os

# def read_file_and_print(file_path):
#     try:
#         # Construct the full file path
#         full_path = os.path.join(os.getcwd(), file_path)
#         print(f"Full path to the file: {full_path}")
        
#         # Check if file exists
#         if not os.path.isfile(full_path):
#             print(f"File not found: {full_path}")
#             return
        
#         # Open and read the file
#         with open(full_path, 'r') as file:
#             file_contents = file.read()
        
#         # Print file contents
#         print("File contents:")
#         print(file_contents)
        
#     except Exception as e:
#         # Print the error message
#         print(f"Error reading the file: {e}")

# # Example usage
# DOWNLOAD_OCR_FILE_PATH = 'uploads/Download OCR.txt'
# read_file_and_print(DOWNLOAD_OCR_FILE_PATH)




# from datetime import datetime

# def convert_date(date_str):
#     try:
#         # Try to parse the date using the expected format
#         date_obj = datetime.strptime(date_str, "%d/%m/%Y")
#         # Format the date object to the desired format
#         return date_obj.strftime("%d/%m/%y")
#     except ValueError:
#         # Return an error message or placeholder if the input is not a valid date
#         return "'"

# # Example usage
# input_date = "22/07/1976"
# converted_date = convert_date(input_date)
# print(converted_date)  # Output: 22/07/76

# # Example of invalid input
# invalid_date = "22/07/76"
# converted_invalid = convert_date(invalid_date)
# print(converted_invalid)  # Output: '
