import math
import sys	
import urllib
import re
import time

from xml.dom import minidom
from xml.dom.minidom import parse
from array import array

sys.stderr = open('err.txt','w')

def getSequence(seq_string):

	seq_num = int(seq_string)
	return seq_num

print '''
|~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*
|~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*
|~~*
|~~*	Simons Foundation Software Engineering Programming Project
|~~*	Python command-line application analysis
|~~*	Andrew Insignares
|~~*
|~~*	**************'''


##ask user for input, either run test case, or run desired input

# a database name, a database identifier, a regular expression 
#(regex) string, and an output file name.
   
db_name = raw_input("|~~*	Enter a dabase name: ").lower()		
db_id = raw_input("|~~*	Enter a dabase identifier: ")
regex = raw_input("|~~*	Enter a regular expression (ex: ACT): ").upper()
file_name = raw_input("|~~*	Enter the desired file name: ")


##test data
#db_name = 'nucleotide'	
#db_id = '30271926'
#regex = 'ACT'
#file_name = 'AwesomeSauce'


##print database input info
print '|~~*    '
print "|~~*    Database: ", db_name
print "|~~*    Database ID: ", db_id
print "|~~*    Regex: ", regex
print "|~~*    File Name: ", file_name
print "|~~*"


##check if string is of only letters / numbers
if re.match("^[A-Za-z]*$", db_name):
	error = False
else:
	print >> sys.stderr, "Error in database name, please only use letters A-Z to sepecify a databse:"
	error = True
	
	
##replace special characters if applied in regex expression
regex = regex.translate(None, '|{}[]()!@#$')

if re.match("^[A-Za-z]*$", regex):
	error = False
else:
	print >> sys.stderr, "Error in regex query, please only use letters A-Z to sepecify a regex:"
	error = True	

try:
	int(db_id)
except: 
	print >> sys.stderr, "Error in database ID, please only use numbers in order to sepecify a databse:"
	error = True

	
##construct url for query    
xmlurl = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'
xmlpath = xmlurl + 'db=' + db_name + '&id=' + db_id + '&rettype=fasta&retmode=xml'

print "|~~*    Attempting eFetch Request..."

##start time clocks
start = time.clock()

try:

    xml = urllib.urlopen(xmlpath)
    dom = parse(xml)
except:
    print 'Error opening the desired xmlURL\n'   
    error = True

if(error == False):
	print '|~~*    xmlPath successful'

elapsed = (time.clock() - start)
print '|~~*    Runtime: ',elapsed, " seconds"
start2 = time.clock()

try:
	name = dom.getElementsByTagName('TSeq_sequence')
	genome = name[0].firstChild.nodeValue
except:
	error = True
	print >> sys.stderr, "There has been an error in your database request, please re-check your database name and ID"

## Printing the genomes from parsed xml for Debug
##print name
##print genome

##perform error checking on input	
if(error == True):
	print >> sys.stderr, "\nError in database request, query will not run\n"
	print 'System will exit now by error, please see err.txt for more information'
	sys.stderr.close()
	sys.exit()
else:
	print >> sys.stderr, "No Errors"

##*************DNA ANALYSIS , MATCHING SUBSEQUENCE******************	
print '|~~*    '
print '|~~*    Output directed to out.txt'

##open output stream	
sys.stdout = open('out.txt','w')
##all output now directed to stdout.txt

print '''
|~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*
|~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*
|~~*
|~~*	Simons Foundation Software Engineering Programming Project
|~~*	Python command-line application analysis
|~~*	Andrew Insignares
|~~*
|~~*	**************'''

##get length of genome string
genome_length = len(str(genome))
print '|~~*    Genome Length:', genome_length


#conver string into itterable object
genome_array = list(genome)
##print '\n',genome_array[1],'\n'

##init values for analysis
testCounter = 0
matchCounter = 0
realMatchCounter = 0
matched_sequences = []

##sequence boolean and building
sequence_bool = False

sequence_split_count = 0
sequence_split_int = 0

##values for printing
sequence_count = 0
subcounter = 0
start_location = 0
end_location = 0
print_string = ""

regex_array = list(regex)
regex_len = len(regex)
print "|~~*    Regex Query Length:",regex_len

matched_sequences.append('Sequence Count, Start Location, End Location ')	

for i in range(genome_length - regex_len):
	##print 'buildingarray'
	if genome_array[i] == regex_array[0]:
		regex_testarray = []
		counter = i
		sequence_count = 0
		
		
		##build test array
		for k in range(regex_len):
			regex_testarray.append(genome_array[counter])
			counter = counter + 1
	
		#join test string
		regex_comparison = "".join(regex_testarray)		
		
		##if comparison is a match, throw into array
		if ( regex_comparison == regex ):
			##counts if regex string was matched
			matchCounter = matchCounter + 1
			
			##variables for sequence checking
			regex_testarray = []
			sequence_bool = True
			subcounter = i + regex_len
			
			##build test array of next existing sequence
			for k in range(regex_len):
				regex_testarray.append(genome_array[subcounter])
				subcounter = subcounter + 1
				
			regex_comparison2 = "".join(regex_testarray)	

			##checks for a match of next sequence of genome
			if ( regex_comparison2 == regex ):
				#print "Sequence exists at:",i
				sequence_count = sequence_count + 1
				sequence_bool = True
			else:
				sequence_bool = False
			
			
			while sequence_bool != False:
			
				subcounter = subcounter + regex_len
				##check if next seqeuence exists
				regex_testarray = []
				
				
				
				##build test array
				for k in range(regex_len):
					regex_testarray.append(genome_array[subcounter])
					subcounter = subcounter + 1
			
				regex_comparison2 = "".join(regex_testarray)		

				##checks for another match of next existing sequence
				if ( regex_comparison2 == regex ):
					##increment sequence counter for sorting
					sequence_count = sequence_count + 1
					sequence_bool = True
				else:
					sequence_bool = False
				
			##endWhile	
			
			##properly insert into SORTED array
			start_location = i + 1
			end_location = i + 1 + (3*sequence_count)
			
			###Array Insert / Swapping
			#	
			#	Insert if seqeuence count > 1
			#		Swap for correct array position
			#
			#	If sequence_count == 0
			#		append bottom of array normally, list grows inorder
			#	matched_sequences[]
			#
			
			##print string for CSV printing
			print_string = str(sequence_count)+","+str(start_location)+","+str(end_location)+","
			
			##if sequence_count is 0, append to array normally
			if( sequence_count == 0):
				matched_sequences.append(print_string)	
			
			##if sequence is > 0, insert into proper element
			if ( sequence_count > 0 ):
				
				##check if value (sequence_count) is larger than compared array list
				sizeOf = len(matched_sequences)
				##print 'now we will have to insert sequences that exists'

				entry = False

				while entry != True:
					for l in range(sizeOf-1):
					
						##retrieve value of array substring
						sequence_count_entry = matched_sequences[l+1]
						
						sequence_split = sequence_count_entry.split(",", 1)
						sequence_split_count = sequence_split[0]
						
						#print sequence_split_count
						#print type(sequence_split_count)
						
						
						##print sequence_split_count
						getNum = getSequence(sequence_split_count)
						
						if(sequence_count > getNum):
							##print "INSERT HERE"
							matched_sequences.insert(l+1, print_string) 
							entry = True
							break	

elapsed2 = (time.clock() - start2)
print "|~~*    Matches complete " 	
print "|~~*    Runtime: ",  elapsed2," seconds"	
##matches complete	

print "|~~*    "
print "|~~*    Data Output:"
print "|~~*    CSV Structure:"
print "|~~*    ",matched_sequences[0]
print "|~~*    "
print "|~~*    Highest Sequence Count:"
print "|~~*    ",matched_sequences[1]
print "|~~*    "
print "|~~*    Last Sequence Match:"
print "|~~*    ",matched_sequences[matchCounter]
print "|~~*    "
print "|~~*    "
##*******************************************************************	
	
##write data to output files
file_name = file_name + ".csv"
outputCSV = open(file_name ,'w')

finalOutput = "\n".join(matched_sequences)
outputCSV.write( finalOutput)

sys.stdout.close()
sys.stderr.close()
outputCSV.close()

print 'Fin'







