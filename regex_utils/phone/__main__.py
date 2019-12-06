#! python2.7

import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
test = "My number is 999-999-9999"

find_it = phone_regex.search(test)

print "Found this phone number: {}".format(find_it.group())

phone_regex_2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

find_it_2 = phone_regex_2.search(test)
area_code = find_it_2.group(1)
rest = find_it_2.group(2)
full = find_it_2.group(0)

print "Area Code: {}, Rest: {}, Full: {}".format(area_code, rest, full)

print "Area Code: %s, Main: %s" % find_it_2.groups()

escaped = "\.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)"
print "Escaped characters: %s" % escaped

piping_phones = re.compile(r'(\(\d\d\d\)|\d\d\d)-(\d\d\d-\d\d\d\d)')
test2 = "My numer is also (999)-999-9999"
find1 = piping_phones.search(test)
find2 = piping_phones.search(test2)

print "%s %s" % find1.groups()
print "%s %s" % find2.groups()

hypo_regex = re.compile(r'hypo(condryac|glucemia|pothamus)')

h1 = "hypocondryac"
h2 = "hypoglucemia"
h3 = "hypopothamus"
h4 = "hypothesis"

h1_find = hypo_regex.search(h1)
h2_find = hypo_regex.search(h2)
h3_find = hypo_regex.search(h3)
h4_find = hypo_regex.search(h4)

print "%s %s %s" % (h1_find.group(), h2_find.group(), h3_find.group())
if h4_find:
	print h4_find.group()

phone_regex_3 = re.compile(r'(\(?\d\d\d\)?)?-?(\d\d\d)-(\d\d\d\d)')
p_1 = phone_regex_3.search(test)
p_2 = phone_regex_3.search(test2)
p_3 = phone_regex_3.search('555-5555')

print "%s %s %s" % (p_1.group(), p_2.group(), p_3.group())

# Testing findall
test3 = 'Cell: 415-555-9999 Work: 212-555-0000 '+test+' '+ test2
for i, num in enumerate(phone_regex_3.findall(test3)):
	print "Number {}: {} {} {}".format(i, *num)


phone_regex_verbose = re.compile(r'''(
	(\d{3}|\(\d{3}\))?					# area code
	(\s|-|\.)?							# first separator
	\d{3}								# initial digits
	(\s|-|\.)							# second separator
	\d{4}								# last digits
	(\s*(ext|x|ext.)\s*\d{2,5})?		# extension
	)''', re.VERBOSE)

f5 = phone_regex_verbose.search(test)
f6 = phone_regex_verbose.search(test2)
f7 = phone_regex_verbose.search(test3)
f8 = phone_regex_verbose.search(" kjlkasjdlkjaskd 443-323-1233 ext 3332 kldjkalsjdljalskd")

print "Number %s" % f5.group()
print "Number %s" % f6.group()
print "Number %s" % f7.group()
print "Number %s" % f8.group()

