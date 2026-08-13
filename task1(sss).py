import re 
pattern1 = re.compile(r'abc')  
result1 = pattern1.match('abcdef') 
if result1: 
    print("Match found:", result1.group()) 
pattern2 = re.compile(r'.') 
result2 = pattern2.search('Hello') 
if result2: 
    print("Character found:", result2.group()) 
pattern3 = re.compile(r'[aeiou]') 
result3 = pattern3.search('Hello') 
if result3: 
    print("Vowel found:",result3.group())
pattern4 = re.compile(r'\d{3}-\d{2}-\d{4}') 
result4 = pattern4.match('123-45-6789') 
if result4: 
    print("Social Security Number:", result4.group()) 
pattern5 = re.compile(r'\.') 
result5 = pattern5.search('www.example.com') 
if result5: 
    print("Dot found:", result5.group()) 
pattern6 = re.compile(r'(\d{2})/(\d{2})/(\d{4})') 
result6 = pattern6.match('01/09/2024') 
if result6: 
    print("Day:", result6.group(1)) 
    print("Month:", result6.group(2)) 
    print("Year:", result6.group(3)) 
pattern7 = re.compile(r'cat|dog') 
result7 = pattern7.search('I have a cat and a dog') 
if result7: 
    print("Animal found:", result7.group())
