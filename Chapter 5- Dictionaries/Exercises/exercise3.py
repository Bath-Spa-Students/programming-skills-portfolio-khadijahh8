programming_words={'string':'sequence of characters that is used as data',
                  'variable':'name that is used to store data to computer memory',
                  'dictionary':'object that stores a collection of data by a key and a value',
                  'list':'an object that contains multipule items of data',
                  'append':'to add item to a list is appende to the end of the existing list'}

# adding new terms
programming_words['Integar']= 'A whole number , positive oe negative without decimal'
programming_words['float']= 'A number positive or negative containing one or more decimals'
programming_words['if-else statement']= 'A control flow statement that allows code to be executed of a certain condition is true'
programming_words['Exeception']= 'An event that occurs during the exection of a program that disrupts the normal flow of the programs instructions'
programming_words['function'] = 'a block of code that performs a specific task'
 
for key, value in programming_words.items():
    print(f"{key} : {value}")