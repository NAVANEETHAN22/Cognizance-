import pandas as pd
ser= pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
result = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])
print("\nQ4) TO CONVERT THE FIRST CHARACTER OF EACH ELEMENT IN A SERIES TO UPPERCASE")
print(result)
