import time
import threading
from datetime import datetime


def read_file(file_path) -> None:
    time.sleep(1)
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}\n")


def main() -> None:
    file_path1 = 'data/file1.txt'
    file_path2 = 'data/file2.txt'
    file_path3 = 'data/file3.txt'
    file_path4 = 'data/file4.txt'
    file_path5 = 'data/file5.txt'
    file_path6 = 'data/file6.txt'
    file_path7 = 'data/file7.txt'
    file_path8 = 'data/file8.txt'


    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path3,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))
    thread5 = threading.Thread(target=read_file, args=(file_path5,))
    thread6 = threading.Thread(target=read_file, args=(file_path6,))
    thread7 = threading.Thread(target=read_file, args=(file_path7,))
    thread8 = threading.Thread(target=read_file, args=(file_path8,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()



if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())