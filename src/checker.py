import os

def fileSizeChecker(fileName):
    fileStats = os.stat(fileName)
    print(f'File Size in Bytes is {fileStats.st_size}')
    print(f'File Size in MegaBytes is {fileStats.st_size / (1024 * 1024)}')