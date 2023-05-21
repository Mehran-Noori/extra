import re
import nltk
import os


input_file = open('input_file.txt')
input_program = input_file.readlines()




RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"



# Counters
Keywords_count=0 
Operators_count=0
Numerals_count=0
Special_Characters_count=0
Identifiers_count=0
Unknown_count = 0




# Categorize The Tokens
line_nth = 0
output_data = []

for line in input_program:
    line_data = []
    line_nth += 1
    input_program_tokens = nltk.word_tokenize(line,language='english')
    # input_program_tokens = nltk.wordpunct_tokenize(line)

    for token in input_program_tokens:

        if(re.findall(RE_Keywords,token)):
            line_data.append(["Keyword", token])
            Keywords_count += 1

        elif(re.findall(RE_Operators,token)):
            Operators_count += 1

            if token == "+":
                line_data.append(["Addition", token])
 
            elif token == "-":
                line_data.append(["Subtraction", token])

            elif token == "*":
                line_data.append(["Multiplication", token])
               
            elif token == "/":
                line_data.append(["Division", token])
               
            elif token == "%":
                line_data.append(["Modulus", token])
               
            elif token == "++":
                line_data.append(["Increment", token])
               
            elif token == "--":
                line_data.append(["Decrement", token])
               
            elif token == "=":
                line_data.append(["Equal", token])
               
            elif token == "==":
                line_data.append(["Equal to", token])
               
            elif token == "!=":
                line_data.append(["Not equal", token])
               
            elif token == ">":
                line_data.append(["Greater than", token])
               
            elif token == "<":
                line_data.append(["Less than", token])
               
            elif token == ">=":
                line_data.append(["Greater than or equal to", token])
               
            elif token == "<=":
                line_data.append(["Less than or equal to", token])

            else:
                line_data.append(["Operator", token])


        elif(re.findall(RE_Numerals,token)):
            line_data.append(["Numeral", token])
            Numerals_count += 1

        elif(re.findall(RE_Special_Characters,token)):
    
            Special_Characters_count += 1

            if token == "(":
                line_data.append(["Parenthese open", token])
 
            elif token == ")":
                line_data.append(["Parenthese close", token])
                
            elif token == "[":
                line_data.append(["Square Bracket open", token])
 
            elif token == "]":
                line_data.append(["Square Bracket close", token])
                
            elif token == "{":
                line_data.append(["Curly Bracket open", token])
 
            elif token == "}":
                line_data.append(["Curly Bracket close", token])
                
            elif token == ".":
                line_data.append(["dot", token])
 
            elif token == ",":
                line_data.append(["Comma", token])
 
            elif token == "\"" or token == "\'":
                line_data.append(["Quotation Mark", token])
 
            elif token == "!":
                line_data.append(["Exclamation Mark", token])
 
            elif token == "?":
                line_data.append(["Question Mark", token])
 
            elif token == ";":
                line_data.append(["Semicolon", token])
            

        elif(re.findall(RE_Identifiers,token)):

            line_data.append(["Identifiers", token])
            Identifiers_count += 1
            
        else:
            line_data.append(["Unknown Value", token])
            Unknown_count += 1


    output_data.append([f"line({line_nth})", line_data ])
    
input_file.close()
output_file = 'output.txt'
if os.path.exists(output_file):
  os.remove(output_file)

output_file = open('output.txt', "w")

for line in output_data:
    output_file.write(f"{str(line)}\n")
output_file.write(f"\n\n\n\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Data///////////////////////////////////\n\n")
output_file.write(f"Keywords_count = {Keywords_count} -- ")
output_file.write(f"Operators_count = {Operators_count} -- ")
output_file.write(f"Numerals_count = {Numerals_count} -- ")
output_file.write(f"Special_Characters_count = {Special_Characters_count} -- ")
output_file.write(f"Identifiers_count = {Identifiers_count} -- ")
output_file.write(f"Unknown_count = {Unknown_count} -- ")

output_file.close()
