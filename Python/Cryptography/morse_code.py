"""----------------------------------------------Introduction---------------------------------------------------------------------------
Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes. 
Morse Code defines a standard encoding where each letter is mapped to a series of  dots and dashes, as follows:
 “a” maps to “.-“, “b” maps to “-…”, “c” maps to “-.-.”, and so on.
----------------------------------------------Algorithm------------------------------------------------------------------------------
Every character in the English language is substituted by a series of 'dots' and 'dashes' or sometimes just singular 'dot' or 'dash' and vice versa.
Every text string is converted into the series of dots and dashes. For this every character is converted into its Morse code and 
appended in encoded message and have considered both numbers and alphabets."""

# function to encode a alphabet as
# Morse code
def morseEncode(x):
	
	# refered to the Morse table
	
	if x is 'a':
		return ".-"
	elif x is 'b':
		return "-..."
	elif x is 'c':
		return "-.-."
	elif x is 'd':
		return "-.."
	elif x is 'e':
		return "."
	elif x is 'f':
		return "..-."
	elif x is 'g':
		return "--."
	elif x is 'h':
		return "...."
	elif x is 'i':
		return ".."
	elif x is 'j':
		return ".---"
	elif x is 'k':
		return "-.-"
	elif x is 'l':
		return ".-.."
	elif x is 'm':
		return "--"
	elif x is 'n':
		return "-."
	elif x is 'o':
		return "---"
	elif x is 'p':
		return ".--."
	elif x is 'q':
		return "--.-"
	elif x is 'r':
		return ".-."
	elif x is 's':
		return "..."
	elif x is 't':
		return "-"
	elif x is 'u':
		return "..-"
	elif x is 'v':
		return "...-"
	elif x is 'w':
		return ".--"
	elif x is 'x':
		return "-..-"
	elif x is 'y':
		return "-.--"
	elif x is 'z':
		return "--.."
	elif x is '1':
		return ".----"
	elif x is '2':
		return "..---"
	elif x is '3':
		return "...--"
	elif x is '4':
		return "....-"
	elif x is '5':
		return "....."
	elif x is '6':
		return "-...."
	elif x is '7':
		return "--..."
	elif x is '8':
		return "---.."
	elif x is '9':
		return "----."
	elif x is '0':
		return "-----"

# character by character print
# Morse code
def morseCode(s):
	for character in s:
		print(morseEncode(character), end = "")



	s = input("Enter a string:")
	morseCode(s)




