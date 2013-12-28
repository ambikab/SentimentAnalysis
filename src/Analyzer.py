'''
Created on 14-Nov-2013
@author: Ambika Babuji
Predicts the sentiment of the given text.
'''
import os;
import Tokenizer;
import FileIO;
import Classifier

def fetchLabel(path):
    tag = (path[path.rfind('\\') + 1:]);
    return tag.upper();
        
def buildCorpus(dirPath, corpusName):
    print('creating corpus!!');
    tagClass = fetchLabel(dirPath);
    classCnt = FileIO.countFiles(dirPath);
    dictionary = {};
    FileIO.wrtieToFile("corpus\classCount.txt", 'a', (tagClass + '\t' + str(classCnt) + '\n' ));
    for dir_entry in os.listdir(dirPath):
        text = FileIO.readFile(os.path.join(dirPath, dir_entry));
        text = Tokenizer.tokenizer(text);
        for token in text.split('\n'):
            if token not in dictionary:
                dictionary[token] = {};
            if tagClass not in dictionary[token]:
                dictionary[token][tagClass] = 0;
            dictionary[token][tagClass] = dictionary[token][tagClass] + 1;
    for key, value in dictionary.items():
        FileIO.wrtieToFile(corpusName, 'a', (key + '\t' + str(value[tagClass]) + '\t' + tagClass + '\n'));
    print('Corpus creation : Done..');

def buildBinarizedCorpus(dirPath, corpusName):
    print('creating binarized corpus!!');
    tagClass = fetchLabel(dirPath);
    classCnt = FileIO.countFiles(dirPath);
    FileIO.wrtieToFile("corpus\classCount.txt", 'a', (tagClass + '\t' + str(classCnt) + '\n' ));
    corpusDict = {};
    for dir_entry in os.listdir(dirPath):
        fileTokens = {};
        text = FileIO.readFile(os.path.join(dirPath, dir_entry));
        text = Tokenizer.tokenizer(text);
        for token in text.split('\n'):
            if token not in fileTokens:
                fileTokens[token] = 1;
                if token not in corpusDict:
                    corpusDict[token] = {};
                    corpusDict[token][tagClass] = 1;
                else:
                    corpusDict[token][tagClass] = corpusDict[token][tagClass] + 1;
    for key, value in corpusDict.items():
        FileIO.wrtieToFile(corpusName, 'a', (key + '\t' + str(value[tagClass]) + '\t' + tagClass + '\n' ));
    print('binarized corpus creation done!!');

def test(testText, dictionary):
    classCntTxt = FileIO.readFile('corpus\classCount.txt');
    classCnt = {};
    for line in classCntTxt.split('\n'):
        statistics = line.split('\t');
        if len(statistics) > 1:
            classCnt[statistics[0]] = statistics[1];
    return Classifier.naiveBayes(dictionary, classCnt, testText);

def loadCorpus(corpusName):
    dictionary = {};
    fileText = FileIO.readFile(corpusName);   
    for line in fileText.split('\n'):
        words = line.split('\t');
        if len(words) > 2:
            if words[0] not in dictionary:
                dictionary[words[0]] = {};
            dictionary[words[0]][words[2]] = words[1];        
    return dictionary; 

def getTestText(fileName):
    testText = FileIO.readFile(fileName);
    testText = Tokenizer.tokenizer(testText);
    return testText;

def getBinTestText(fileName) :
    fileText = FileIO.readFile(fileName); 
    tokens = Tokenizer.tokenizer(fileText);
    wordOccurence = {};
    resultTokens = "";
    for token in tokens.split("\n"):
        if token not in wordOccurence:
            wordOccurence[token] = 1;
            resultTokens = resultTokens + token + "\n";
    return resultTokens;
    
def main(trainMode, binarized, testDir, resultFile):
    dir1 = r'R:\masters\fall2013\COMP579A\project\aclImdb\train\pos';
    dir2 = r'R:\masters\fall2013\COMP579A\project\aclImdb\train\neg';
    corpusName = r'corpus\binCorpus.txt';
    if(not binarized):
        corpusName = r'corpus\corpus.txt';
    if(trainMode):
        if(binarized):
            buildBinarizedCorpus(dir1, corpusName);
            buildBinarizedCorpus(dir2, corpusName);
        else:
            buildCorpus(dir1, corpusName);
            buildCorpus(dir2, corpusName);
    
    dictionary = loadCorpus(corpusName);
    testText = '';
    print('test for dir' , testDir);
    for dir_entry in os.listdir(testDir):
        if binarized:
            testText = getBinTestText(os.path.join(testDir, dir_entry));
        else:
            testText = getTestText(os.path.join(testDir, dir_entry));
        result =test(testText, dictionary);
        FileIO.wrtieToFile(resultFile, 'a' ,"The file " + os.path.join(testDir, dir_entry) + " is classified as " + result + "\n");
    print("Done....");

main(False, True, r'R:\masters\fall2013\COMP579A\project\aclImdb\test\neg', r'results\nbBinNeg.txt');
main(False, True, r'R:\masters\fall2013\COMP579A\project\aclImdb\test\pos', r'results\nbBinPos.txt');
main(False, False, r'R:\masters\fall2013\COMP579A\project\aclImdb\test\neg', r'results\nbNeg.txt');
main(False, False, r'R:\masters\fall2013\COMP579A\project\aclImdb\test\pos', r'results\nbPos.txt');