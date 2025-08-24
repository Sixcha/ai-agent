import os

def get_files_info(working_directory, directory="."):
    # Set directory to check and its absolute path
    targetDirectory = os.path.join(working_directory, directory)
    targetAbsPath = os.path.abspath(targetDirectory)

    # Handle Errors
    errors = []
    if not os.path.isdir(targetDirectory):
        errors.append(f'Error: "{directory}" is not a directory')
        print("\n".join(errors))
        return errors
    
    if not targetAbsPath.startswith(os.path.abspath(working_directory)):
        errors.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        print("\n".join(errors))
        return errors

    items = os.listdir(targetDirectory)
    try:
        filesInfo = []
        for i in items:
            filePath = os.path.join(targetDirectory,i)
            fileSize = os.path.getsize(filePath)
            isDir = os.path.isdir(filePath)
            filesInfo.append(
                f"- {i}: file_size={fileSize} bytes, is_dir={isDir}"
            )
        return "\n".join(filesInfo)
    except Exception as e:
        return f"Error listing files:{e}"