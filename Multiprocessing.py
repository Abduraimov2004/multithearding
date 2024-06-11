import time
import multiprocessing
from datetime import datetime


def write_to_file(file_path) -> None:
    time.sleep(3)
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data written to {file_path}: {data}")


def main() -> None:
    file_path1 = 'data/file1.txt'
    file_path2 = 'data/file2.txt'
    file_path3 = 'data/file3.txt'
    file_path4 = 'data/file4.txt'
    file_path5 = 'data/file5.txt'
    file_path6 = 'data/file6.txt'
    file_path7 = 'data/file7.txt'
    file_path8 = 'data/file8.txt'


    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1,))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2,))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3,))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4,))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path5,))
    process6 = multiprocessing.Process(target=write_to_file, args=(file_path6,))
    process7 = multiprocessing.Process(target=write_to_file, args=(file_path7,))
    process8 = multiprocessing.Process(target=write_to_file, args=(file_path8,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()

    print("Main process continues execution.")


if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())
