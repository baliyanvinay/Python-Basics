import re

# \s matches any whitespace character [ \r\n\t\f ] \S is the compliment of \s and result of \S=Total Set-\s
# \r returns \n newline \t tab \f
regex_patter = r"\S{2}\s\S{2}\s\S{2}"
# pattern: XXxXXxXX
# Here, x denotes whitespace characters, and X denotes non-white space characters.

# r means it is gonna treat the string pattern as raw string and will count even any escape expression
string = r'\nThis shall not be printed in new line'

# pattern: xxxXxxxxxxxxxxXxxx
# Here, x denotes any word character and X denotes any non word character
# for example, $ is non word character, 'www.hackerrank.com'
regex_pattern = re.compile(r"\w{3}\W\w{10}\W\w{3}")
string = 'www.hackerrank.com'


# Caret ^ symbol matches the position at the start of a string.
# For example, ^123 will match with 12345123 only the first 123 as output or as count
# The $ symbol matches the position at the end of a string.
# Consider a string of 6 characters starting with digit and following 5 any word chacters
# \W means that it is gonna be a special character $ checks that the following patter of 6 characters are followed or not
# if characters are more than 6 then the result is gonna be false
regex_pattern = r"\d\w{4}\W$"
string = '6abcd.'


# The character class [ ] matches only one out of several characters placed inside the square brackets.
# For example, regex_patter= r"^[aeiou]", string='a is a vowel'
# String must be of length: 6
# First character: 1, 2 or 3
# Second character: 1, 2 or 0
# Third character: x, s or 0
# Fourth character: 3, 0 , A or a
# Fifth character: x, s or u
# Sixth character: . or ,
regex_pattern = r"^[1-3][0-2][x,s,0][0,3,a,A][x,s,u][.,,]$"
string = '1203x,'

# The negated character class [^] matches any character that is not in the square brackets.
# String must be of length 6.
# First character should not be a digit (0-9).
# Second character should not be a lowercase vowel (aeiou).
# Third character should not be b, c, D or F.
# Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
# Fifth character should not be a uppercase vowel (AEIOU).
# Sixth character should not be a . or , symbol.
regex_pattern = r"^[^0-9][^aeiou][^c,D-F]\S[^AEIOU][^.,,]$"
string = 'think?'

# The string's length is >=5.
# The first character must be a lowercase English alphabetic character.
# The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
# The third character must not be a lowercase English alphabetic character.
# The fourth character must not be an uppercase English alphabetic character.
# The fifth character must be an uppercase English alphabetic character
regex_pattern = r"^[a-z][1-9][^a-z][^A-Z][A-Z]"
string = 'a0$?ZWe'

# Write a regex expression where the string length is equal to 45 and first 40 can be uppercase, lowercase and even digits.
# The last 5 characters should consist of odd digits or whitespace characters.
regex_pattern = r"^[02468a-zA-Z]{40}[13579\s]{5}$"
string = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa'
string = 'x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779'


# The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group.
# For Example: w{3,5} : It will match the character w 3, 4 or 5 times.
# [xyz]{5,} : It will match the character x, y or z 5 or more times.
# \d{1, 4} : It will match any digits 1, 2, 3, or 4 time
# Write a regex expression where string should begin with 1,2 digits, after that string should have 3 or more letters(u/l)
# Then string should end upto 3 '.' symbols {0,3}
regex_pattern = r"^\d{1,2}[a-zA-Z]{3,}[.]{0,3}$"
string = '3threeormorealphabets.'


# The * tool will match zero or more repetitions of character/character class/group.* is equivalent to {0,}
# w* : It will match the character w 0 or more times.
# [xyz]* : It will match the characters x, y or z 0 or more times.
# \d* : It will match any digit 0 or more times.
# Write a regex expression where string should begin with 2 or more digits, after that string should have 0 or more
# lowercase letter and then string should end with 0 or more uppercase letters.
regex_pattern = r"^\d{2,}[a-z]*[A-Z]*$"
string = '1akldflkvnlDFVDFVDFVD'

# The + tool will match one or more repetitions of character/character class/group.
# w+ : It will match the character w 1 or more times.
# [xyz]+ : It will match the characters x, y or z 1 or more times.
# \d+ : It will match any digit 1 or more times.
# Write a regex expression where string should begin with 1 or more digits, after that string should have 1 or more
# uppercase letter and then string should end with 1 or more lowercase letters.
regex_pattern = r"^\d+[A-Z]+[a-z]+$"
string = '1DFVDFVDFVDakldflkvnl'

# The $ boundary matcher matches an occurrence of a character/character class/group at the end of a line.
# Write a regex expression where string should consist of only lowercase and uppercase letters (no numbers or symbols)
# and should end in s.
regex_pattern = r"^[a-zA-Z]*[s]$"
string = 's'

# \b assert position at a word boundary.
# Three different positions qualify for word boundaries :
# ► Before the first character in the string, if the first character is a word character.
# ► Between two characters in the string, where one is a word character and the other is not a word character.
# ► After the last character in the string, if the last character is a word character.
# Write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U).
# The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
# The matched word must start and end with a word boundary.
regex_pattern = r"\b[AEIOUaeiou][a-zA-Z]*\b"
string = 'Ajaya'

string = 'saveChangesInTheEditor'
Regex_Pattern = r"[A-Z]"
match = re.findall(Regex_Pattern, string)

# from a given string, verify if it is an email address, print name of the user is the address is of gmail domain
# email address consists of lower case [a-z], @ and a dot
string = 'manojkumar@gmail.com'
regex_pattern = r"[a-z]+@gmail.com$"

# Checking if a given string is a floating point number
regex_pattern = r"^[-+]?[0-9]*\.[0-9]+$"
string = '123..42'

# Check any email
string = 'name@tcs.de'
regex_pattern = r"^[a-z0-9]+[\w.\-]*\@[a-z]+\.[a-z]{1,3}$"
