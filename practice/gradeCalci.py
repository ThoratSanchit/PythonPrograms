print("--------------------This is the grade calculator------------- ")
marks=[]
sum=0
def gradeCalculator():
   
    for i in range(1,7):
        print("Enter the subject {} mark ".format(i))
        marks.append(int(input()));
       
   
gradeCalculator()    
for e in marks:
    sum+=e

percentage=sum/6  
print(percentage)
if percentage>=70:
    print("You pass with first class.")
elif percentage>50 and percentage<70:
    print("You are pass with second class.")  
elif percentage>=35 and percentage<50:
    print("You are pass")    
else:
    print("Sorry you are fail")
     




        
        
        
