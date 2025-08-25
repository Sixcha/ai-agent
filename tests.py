from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def runTests():
    results = []

    tests = [
        ["calculator", "main.py"],
        # ["calculator", "main.py", ["3 + 5"]],
        # ["calculator", "tests.py"],
        # ["calculator", "../main.py"]
        # ["calculator", "nonexistent.py"]
    ]

    for t in tests:
        results = run_python_file(t[0], t[1])
        print((results))




if __name__ == "__main__":
    runTests()