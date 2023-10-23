'''
Create a file named mydata2.txt
Open the file without using with (open in try)
Catch FileNotFoundError
In else print contents
In finally
Open nonexistent file mydata3.txt
'''

try:
    myFile = open("mydata3.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File : {}".format(myFile.read()))
    myFile.close()

finally:
    print("Finished Working with File")