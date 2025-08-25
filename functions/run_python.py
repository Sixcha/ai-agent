import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    targetFile = os.path.join(working_directory, file_path)
    targetAbsPath = os.path.abspath(targetFile)

    # Handle Errors
    errors = []
    
    if not targetAbsPath.startswith(os.path.abspath(working_directory)):
        errors.append(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    if not targetFile.endswith(".py"):
        errors.append(f'Error: "{file_path}" is not a Python file.')

    if not os.path.exists(targetFile):
        errors.append(f'Error: File "{file_path}" not found.')

    if errors:
        print(errors)
        return errors
    
    subprocess.run(targetFile, args, timeout=30, capture_output=True)