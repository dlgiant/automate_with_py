import sys

def print_metrics(filename, out, just):
	list_of_lines = []
	count = 0

	with open(filename, 'r') as f:
		for line in f:
			if count == 0:
				list_of_lines.append((" {} ".format(line.strip())).center(just, '*'))
			else:
				splitter = line.split(',')
				list_of_lines.append("{}".format(splitter[0].ljust(int(round(just/2)), '.')+
									 			 splitter[1].strip().rjust(just-int(round(just/2)), ' ')))
			count += 1

	with open(out, 'w+') as f:
		f.write('-'*just+'\n')
		for line in list_of_lines:
			f.write("{}\n".format(line))
		f.write('-'*just+'\n')

def main():
	filename = sys.argv[1]
	out = sys.argv[2]
	just = int(sys.argv[3])
	print_metrics(filename, out, just)

main()