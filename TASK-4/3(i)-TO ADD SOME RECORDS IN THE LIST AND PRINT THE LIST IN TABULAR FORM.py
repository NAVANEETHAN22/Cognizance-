str = input("TO ADD SOME RECORDS IN THE LIST AND PRINT THE LIST IN TABULAR FORM\n")
a = [ [1, "Abc", 90],
     [2, "Def", 95],
     [3, "Ghi", 85]]
     
print ("{:<8} {:<8} {:<8}".format('Roll No','Name','Marks'))

for b in a:
    Roll, name, marks = b
    print ("{:<8} {:<8} {:<8}".format( Roll, name, marks))
