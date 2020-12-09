statement="Hello how are you@"
if statement:
    
    x=statement.lower()
    
    vowels="a,e,i,o,u"

    numbers="0,1,2,3,4,5,6,7,8,9"

    symbols="@Αß©"

    for sentence in x:

        statement=x.find(sentence,x.index(sentence)+1,len(x))

        if statement==-1:

            if sentence in vowels:
                print(f"unique character is {sentence}, it is vowel and its ord is {ord(sentence)}")
            elif sentence in symbols:
                print(f"{symbols.encode()} its a symbol")
            elif sentence in numbers:
                print("")
            else:
                print(f"unique character is {sentence}, it is consonent and its ord is {ord(sentence)}")

else:
    print("anything")
                

	# lEAVE SPACE BEFORE AND AFTER 
	# DEFINE   VARAIABLES  NT IN LOGIC
	# meaning vara
