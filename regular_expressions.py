import re
# findall, searcg, split, sub, finditer

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# patt = re.compile(r'fass')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)
#
# print(mystr[448:452])
# patt = re.compile(r'.')
# patt  = re.compile(r'.adm')
# any charactor = . and after given word
# patt  = re.compile(r'^adm')
# start from given word
# patt  = re.compile(r'$Tata')
# end of given word
# patt  = re.compile(r'ai*')
# in end a and after a number of i
# patt  = re.compile(r'$iin')
# patt = re.compile(r'ai{2}')
# how many i after a
# patt = re.compile(r'(ai){2}')
# group of ai
# patt = re.compile(r'ai{1}|Fax')
# patt = re.compile(r'\AFax')
# match
# patt = re.compile(r'\bFax')
# start from Fax
# patt = re.compile(r'Fax\b')
# end from Fax

# patt = re.compile(r'\d{5}-\d{4}')


# task
# given a string with a lot of indian numbers starting from +91







matches  = patt.finditer(mystr)
for match in matches:
    print(match)

# print(r"\n")

