statement = input('enter the sentence: ')

if statement:
	    
    lower_ = statement.lower()


    for letter in lower_:
        
        statement_ = lower_.find(letter,lower_.index(letter)+1,len(lower_))
    
        if statement_ != -1 :
                        
            print(f'second occurance of the "{letter}" is {statement_}.')
                    
        else:

            print(f'"{letter}" has no second occurance and its index is {lower_.find(letter)}.')
else:
    print("please enter something")
