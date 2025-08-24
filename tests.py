from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def runTests():
    results = []

    tests = [
        ["calculator", "lorem.txt", "wait, this isn't lorem ipsum"],
        ["calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"],
        ["calculator", "/tmp/temp.txt", "this should not be allowed"]
    ]

    for t in tests:
        results = write_file(t[0],t[1],t[2])
        print((results))




if __name__ == "__main__":
    runTests()