string1='''Python is a ___1___ level programming language.
Python doesn't use braces({}) to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line ___2___.
The number of spaces in the ___2___ is variable, but all statements within the block must be indented the same amount.
Python accepts single ('), double (") and triple quotes to denote ___3___ literals, as long as the same type of quote starts and ends the string.A comment in python start with ___4___ symbol.All characters after the ___4___ and up to the end of the physical line are part of the comment and the Python interpreter ignores them '''

answer1=['high','indentation','string','#']

string2='''String is a sequence of ___1___. Whereas ___2___ can contain hetrogenous value.The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.string is ___3___ Whereas ___2___ is mutable. 
Both string and list can be accessed using square brackets.Lists and strings respond to the + and * operators. list.append(obj) is used to ___4___ object in list. A function is a block of organized, reusable code that is used to perform a single, related action. It starts with the keyword ___5___. '''

answer2=['characters','list','immutable','append','def']

string3='''What is the output of print str * 2 if str = 'hello world!'? output: ___1___.\n
colors = [‘Red’, ‘Black’, ‘White’, ‘Green’]
x = colors.index(“White”)
print(x)
output:___2___\n
colors = [‘red’, ‘white’, ‘blue’, ‘green’]
What will be the value of colors[-2]?
output:___3___\n
Say s=”hello” what will be the return value of type(s). output: ___4___.
 '''

answer3=['hello world!hello world!','2','blue','str']

to_be_replaced=['___1___','___2___','___3___','___4___','___5___']

# variable to keep the counts
k=0
count_wrongsol=0

def check_answer(user_sol,user_input):
    # this function checks whether the input answer given by the user is correct or not
    # and return true if correct else returns false.
    # It takes as input the user answer(user_sol) and the quiz level(user_input).
    global k
    if(user_input=='easy'):
        if(user_sol==answer1[k]):
            k+=1
            return True
    if(user_input=='medium'):        
        if(user_sol==answer2[k]):
            k+=1
            return True
    else:        
        if(user_sol==answer3[k]):
            k+=1
            return True    
    return False    
     
def word_in_pos(word, parts_of_speech):
    # this function takes as input the string word and a list to be replaced.
    #If there is a word in to be replaced 
    # that is a substring of the variable word, then return that word in parts_of_speech, 
    # else return None.
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(teststring, to_be_replaced,user_input,user_input2):
    # It takes as input the quiz string(teststring),list(to_be_replaced)and variable(user_input2)
    # This function prompts the quiz and prompt the user to enter answer
    # If the guess is correct it prompt the answer is correct and replaces the blank
    # with answer else prompt to try again. It also keep track of how many wrong answer
    # are given and if the number is equal to the limit user entered in the begining of
    # the quiz it prompts game over. 
    global count_wrongsol
    word=0 
    print teststring + '\n'
    teststring = teststring.split()
    while(word<len(teststring)):
        replacement = word_in_pos(teststring[word],to_be_replaced)
        if replacement != None:
            user_sol = raw_input("Fill in the blank:  " + replacement + " ").lower()
            if(check_answer(user_sol,user_input)):
                print 'CORRECT !'
                teststring = [w.replace(replacement, user_sol) for w in teststring]
                teststring=" ".join(teststring)
                print'\n'+ teststring + '\n' 
                teststring = teststring.split()
                word+=1
            else:
                count_wrongsol+=1
                if(user_input2==count_wrongsol):
                   print 'GAME OVER :(\n'
                   
                print
                print 'WRONG ANSWER ! Try Again \n'
        else:
            word+=1    
    return 

def start_game():
    #This function takes the user choice i.e. the level(easy,medium,hard)
    # and the no of try that user can make before they lose
    # this function calls other function play_game.
    print 'Choose the level'
    print 'EASY MEDIUM HARD'
    user_input =raw_input("Enter level: ")
    print 'After how many wrong answer the gave should be over'
    user_input2 = int(raw_input("Enter: "))
    user_input=user_input.lower()
    if(user_input=='easy'):
       play_game(string1,to_be_replaced,user_input,user_input2) 
    if(user_input=='medium'):
       play_game(string2,to_be_replaced,user_input,user_input2)
    if(user_input=='hard'):
       play_game(string3,to_be_replaced,user_input,user_input2)         
    
    return
    
start_game()
 