Section 01:
-----------
Supply the training folder path:
	* In the Analyzer.py : in main() : dir1 and dir2 should point to the location of the training folders POS and NEG folders respectively.
------------------------------------------------------------------------------------------------------------------------------------------
To run the program :
	* Analyzer.py => main(trainMode, binarized, testDir, resultFile) is run
	where  	trainMode is set to True if the program has to be run in Training Mode(explained in Section 03:)
			binarized is set to True if the program has to be run using BinarizedNaiveBayes classifier.
			testDir => directory where the test files are stored (format of test files described in Section 02:).
			resultFile => give a path where the result has to be stored. 
	* EX: main(True, False, r'R:\masters\fall2013\COMP579A\project\aclImdb\test\neg', r'results\nbNeg.txt');
		- The example makes the program to Run in Training mode and use Naive Bayes classifier.
----------------------------------------------------------------------------------------------------------------------------------		  
 Section 02:
 -----------
 Format of the TRAINING files:
 	* Each file should have only one review.
 	* All the positive files should be placed under the folder "pos".
 	* All the negative files should be placed under the folder "neg".
 Format of the TEST files:
 	* Each file should have only one review.
 	* All the positive files should be placed under the folder "pos".
 	* All the negative files should be placed under the folder "neg".
----------------------------------------------------------------------------------------------------------------------------------
 Section 03:
 -----------
 Training Mode:
 -------------
 Training mode is a mode where the bag of words are freshly created from the training files and are stored under the corpus folder.
 To do For Running the program in Training Mode:
 	* Empty the corpus folder. SHOULD NOT DELETE THE CORPUS FOLDER.
 	* Empty the results folder.
 Testing Mode:
 	* This mode can be used only if the program been run in Training mode atleast once.
 	* Check if the corpus has the files created from the training phase.
 	* Empty ONLY the results folder.
-----------------------------------------------------------------------------------------------------------------------------------
 Note about the existing state of the Program:
 	* The program has the corpus generated from both training set. Hence can be run directly on the test mode.