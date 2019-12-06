#! python3
# 

SENTENCES = {
	'yes': """
Agree dude
	""",
	'no': """
Naaaaaaaah
	""",
	'jira': """
Plan:
Goal:
Expect:
Description:
Tests:
	"""

}

import sys 
from pyperclip import copy

def main():
	if len(sys.argv) < 2:
		sys.exit()

	choice = sys.argv[1]
	if choice in SENTENCES.keys():
		copy(SENTENCES[choice])
		print("Text for "+ choice +" copyied")
	else:
		print("Choice not found")

main()