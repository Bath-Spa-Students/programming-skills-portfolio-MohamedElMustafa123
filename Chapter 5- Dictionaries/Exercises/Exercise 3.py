programming_words = {'Algorithm' : 'An algorithm is a set of instructions that are followed to solve a problem.',
                     'Arrays': 'Arrays are containers that hold variables',
                     'Binary numbers': 'A binary number is a computer\'s way to represent information.',
                     'Variables': 'A reserved memory location to store values.',
                     'If statements': 'An if statement runs a block of code based on whether or not a condition is true.',
                     'input': 'Input is any interaction from the user to the program.',
                     'ASCII': 'American Standard Code for Information Interchange (ASCII) is a system for electronic communication.',
                     'Boolean': 'An expression that can only produce TRUE or FALSE statements is known as a Boolean expression.',
                     'For loops': 'For loops allow users to repeatedly run a block of code. They repeat a piece of code a predetermined number of times.',
                     'Operator': 'An operator is a term used to denote the object which can manipulate different operands.'
                     }
#using for loop to iterate through the dictionary. We use two variables since we are accesing the keys
#and values of the keys by using .item()
for x, y in programming_words.items():
    print(x + ": " + y)