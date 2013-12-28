'''
Created on 14-Nov-2013
@author: Ambika Babuji
File IO operations are handled here.
'''
import os;

def readTrainFiles(dirPath):
    contents = "";
    for dir_entry in os.listdir(dirPath):
        dir_entry_path = os.path.join(dirPath, dir_entry);
        print ('opening file >', dir_entry_path);
        contents = contents + readFile(dir_entry_path);
    return contents;

def wrtieToFile(fileName, mode, contents):
    fileHandler = open(fileName, mode);
    for line in contents:
        fileHandler.write(line);

def readFile(fileName):
    contents = '';
    if os.path.isfile(fileName):
            with open(fileName, 'r', encoding='cp1252', errors='ignore') as my_file:
                contents = contents + my_file.read();
    return contents;

def countFiles(dirPath):
    count = 0;
    for dir_entry in os.listdir(dirPath):
        if os.path.isfile(os.path.join(dirPath, dir_entry)):
            count = count + 1;
    return count;