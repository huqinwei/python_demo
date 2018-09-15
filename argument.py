import argparse
import sys
import getopt


print("script_name:",sys.argv[0])

for i in range(1,len(sys.argv)):
	print("param",i,sys.argv[i])

opts,args = getopt.getopt(sys.argv[1:],"hi:o:")
input_file=""
output_file=""
for op,value in opts:
	if op == "-i:":
		input_file = value
	elif op == "-o":
		output_file = value
	elif op == "-h":
		usage()
		sys.exit()	



print("input_file = ",input_file)
print("output_file = ",output_file)
'''

'''


