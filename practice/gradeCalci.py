print("This is the grade calculator ")
marks=[]
sum=0
def gradeCalculator():
    print("Enter the 6 subject marks:")
    for i in range(1,7):
        marks.append(int(input()));
       
   
gradeCalculator()    
for e in marks:
    sum+=e
print("Sum", sum)
percentage=sum/6  
print(percentage)
if percentage>=70:
    print("You pass with first class.")
elif percentage>50 and percentage<70:
    print("you pass with second class.")  
elif percentage>=35 and percentage<50:
    print("you pass")    
else:
    print("you are fail")
     




        
        
        
