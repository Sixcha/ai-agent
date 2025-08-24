import os

def get_file_content(working_directory, file_path):
    maxFileSize = 10000
    # Set file to check and its absolute path
    targetFile = os.path.join(working_directory, file_path)
    targetAbsPath = os.path.abspath(targetFile)

    # Handle Errors
    errors = []
    if not os.path.isfile(targetFile):
        errors.append(f'Error: File not found or is not a regular file: "{targetFile}"')
        print("\n".join(errors))
        return errors
    
    if not targetAbsPath.startswith(os.path.abspath(working_directory)):
        errors.append(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        print("\n".join(errors))
        return errors
    
    try:
        with open(targetFile, "r") as f:
            fileContents = f.read(maxFileSize)
            if os.path.getsize(targetFile) > maxFileSize:
                fileContents = f"{fileContents} ...File {file_path} truncated at 10000 characters"
            print(fileContents)
            return fileContents
    except Exception as e:
        return f"Error listing file contents: {e}"