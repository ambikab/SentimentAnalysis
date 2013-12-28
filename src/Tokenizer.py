'''
Created on 14-Nov-2013
@author: Ambika Babuji
Tokenizes the test files.
'''
import re;

def tokenizer(text):
    notPtn = re.compile(r'\b[Nn][Oo][Tt]\b');
    text = text.lower();
    text = re.sub(r"([A-Za-z]+)(n't)\b", '\g<1> not', text);
    text = re.sub(r"([A-Za-z]+)('s)\b", '\g<1> is', text);
    text = re.sub(r"([A-Za-z]+)('m)\b", '\g<1> am', text);  
    text = re.sub("(.)\1{2,}",  '\1\1', text); #shortening
    text = re.sub(r"([^A-Za-z 0-9])", ' \g<1> ', text);
    text = re.sub("[ ]+", " ", text);
    tokens = ''; #to store the double negated text;
    for line in text.split("\n"):
        negated = False;
        if(notPtn.search(line)):
            contents = '';
            for words in line.split(" "):
                if (negated):
                    words = 'NOT_' + words;
                if (notPtn.match(words) ):
                    negated = not negated;
                punctuation = re.compile(r'(NOT_)?([^A-Za-z 0-9])');
                if (punctuation.match(words)):
                    negated = False;  
                contents = contents + ' ' + words; 
        else:
            contents = line;
        tokens = tokens + contents;         
    tokens = re.sub("[ ]+", '\n', tokens); 
    return tokens; 
