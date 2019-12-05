import sys

def pretty_log(filename, out):
	list_of_strings = []
	with open(filename, "r") as f:
		for line in f:
			splitter = line.split(':')
			list_of_strings.append("".join([splitter[0].ljust(35,' '),
									   		splitter[1].rjust(35,' ')]))

	with open(out, 'w+') as f:
		for line in list_of_strings:
			f.write("{}\n".format(line))

def main():
	filename = sys.argv[1]
	out = sys.argv[2]
	pretty_log(filename, out)

main()