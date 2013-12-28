'''
Created on 14-Nov-2013
Text classifiers
@author: Ambika Babuji
'''
import decimal;

def naiveBayes(dictionary, classFreq, testWords):
    totCorpusDoc = int(classFreq['POS']) + int(classFreq['NEG']); 
    tmpProbPOS = 1.0;
    tmpProbNEG = 1.0;
    modV = len(dictionary);
    for testWord in testWords.split('\n'):
        if testWord in dictionary:
            if 'POS' in dictionary[testWord]:
                valuePOS = float(dictionary[testWord]['POS']); #TODO: check if the tag exists for the given word else apply smoothing
            else:
                valuePOS = 0.0;
            if 'NEG' in dictionary[testWord]:
                valueNEG = float(dictionary[testWord]['NEG']);
            else:
                valueNEG = 0.0;
        else:
            valueNEG = 0.0;
            valuePOS = 0.0;
        tmpProbPOS = decimal.Decimal(tmpProbPOS) * decimal.Decimal( (valuePOS + 1.0) / (float (classFreq['POS']) + modV) );
        tmpProbNEG = decimal.Decimal(tmpProbNEG) * decimal.Decimal( (valueNEG + 1.0) / (float (classFreq['NEG']) + modV) );
    finalPOSProb = decimal.Decimal(tmpProbPOS) * decimal.Decimal((float (classFreq['POS']) / totCorpusDoc));
    finalNEGProb = tmpProbNEG * decimal.Decimal(float (classFreq['NEG']) / totCorpusDoc);
    #print('final -ve prob value is : ', decimal.Decimal(finalNEGProb));
    #print('final +ve prob value is : ', decimal.Decimal(finalPOSProb));
    if decimal.Decimal(finalNEGProb) - decimal.Decimal(finalPOSProb) > 0.0:
        return "NEGATIVE REVIEW";
    else:
        return "POSITIVE REVIEW"; 