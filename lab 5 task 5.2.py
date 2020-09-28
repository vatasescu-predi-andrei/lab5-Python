date=str(input("Please enter your birthday in dd/mm/yyyy format please"))

month=int(date[3]+date[4])
day=int(date[0]+date[1])
year=int(date[6]+date[7]+date[8]+date[9])
if month==1:
   print(day,"January",year)
elif month==2:
   print(day,"February",year)
elif month==3:
   print(day,"March",year)
elif month==4:
   print(day,"April",year)
elif month==5:
   print(day,"May",year)
elif month==6:
   print(day,"June",year)
elif month==7:
   print(day,"July",year)
elif month==8:
   print(day,"August",year)
elif month==9:
   print(day,"September",year)
elif month==10:
   print(day,"October",year)
elif month==11:
   print(day,"November",year)
elif month==12:
   print(day,"December",year)
