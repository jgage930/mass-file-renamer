import os

def main():
    extension = '.png'
    folder_name = 'Named_Files'

    # read names file
    names = []
    with open('names.txt', 'r') as file:
        names = file.readlines()

    # read name of the files to rename
    filesToName = sorted(os.listdir('Files'))

    #rename
    for index, file in enumerate(filesToName):
        os.rename(f"Files/{file}", f"{folder_name}/{names[index].strip()}{extension}")
    print(names)
    print(*filesToName, sep='\n')

if __name__ =='__main__':
    main()