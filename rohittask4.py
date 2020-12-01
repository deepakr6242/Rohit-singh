a=input(int("enter average marks", 70<80))
b=input(int("enter distinct marks", 80<90))
c=input(int("enter elite marks)", 90<100)
        if a<b:
        print("average marks")
        if ab<c:
        print("distinct marks")
        else:
          print("elite marks")


# Reviewed Code Below


marks = int(input('Enter the marks: '))

if 70 <= marks < 80:
	    print('checking 70-75 category and 75-80 category....... ')
	    if 70 <= marks <= 75:
	        print('Average')
	    else:
	        print('above average')
elif 80 <= marks <90:
	    print('Distinction')
elif 90 <= marks <=100:
	    print('elite')
elif 0 <= marks < 70:
	    print('Poor students')
else:
		print('Give valid marks within 100')
    
