import os

def write_file(working_directory, file_path, content):
    targetFile = os.path.join(working_directory, file_path)
    targetAbsPath = os.path.abspath(targetFile)
    print(targetFile)

    # Handle Errors
    errors = []
    
    if not targetAbsPath.startswith(os.path.abspath(working_directory)):
        errors.append(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')  

    if errors:
        # print("\n".join(errors))
        return errors
    
    # Create file if necessary
    if not os.path.exists(targetFile):
        os.makedirs(os.path.dirname(targetFile),exist_ok=True)

    
    with open(targetFile, "w") as f:
        f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

