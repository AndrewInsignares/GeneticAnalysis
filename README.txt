
Simons Foundation Software Engineering Programming Project

-----------------------------------------------

README.txt

This is documentation for the Simons Foundation Python programming project 
performing string based analysis on a specified genome
sequence from the GenBank databases for DNA and protein sequences. 
This application is built with Python using "eFetch" requests from the 
NCBI Database. 

Files Included:

DNA_Analysis.py				- python project program
HumanChromosome1_analysis.txt		- CSV analysis for PART II
out.csv					- sample test output from famed file
out.txt					- Output from DNA_Analysis.py	
err.txt					- Error output from DNA_Analysis.py	

________

Runtime Analysis

The program first accepts user input. This input is validated and creates 
an eFetch url request to the NCBI database with the given info. The 
sequence requested is then parsed and analyzed with the regex input parameter. 

The genome is parsed and checked for matches against the regex string. The first
element of the regex is compared with the genome, and if there is a match, 
the rest of the regex string is then compared with the following characters in 
the genome. If a full match exists, it is then appended to the outputCSV file
with the sequence count, starting position, and ending position. The sequence count
is incremented if the same regex string follows the initial match.This entry 
is then valued and inserted into the outputCSV file, placing it with higher 
priority being found at the top of the outputCSV file. 

An example of this analysis can be found in HumanChromosome1_analysis.txt which
shows the sorted output of the analysis of the HumanChromosome1 against the 
regex string "ACT". The matches are ordered from highest sequence count to lowest, 
and then by starting location. 

________

To Run

1. Open Terminal / Execution environment  

2. Enter directory of existing DNA_Analysis.py program

3. Run file with the python interpreter as follows:
	
	python DNA_Analysis.py	

4. Program interface will execute in Shell window and ask for user input

5. Enter desired input: Database Name, Unique ID, Regex, CSVOutput File Name

6. Output streams will dump into the following files:
	
	1) out.txt 			- output of program
	2) err.txt			- error output of program
	3) [chosen file name].csv 	- CSV analysis of DNA with queried Regex 
	
	