#Program Created by N.G. SANTHOSH SUDHAAN
#send your feedback to santhoshsudhaan@yahoo.com

def yep():

    print("\nPlease let me know your current temperature in degree Fahrenheit:")
    temp=int(input("\n1.Normal(96F-98.6F)\n2.Fever(98.6F-102F)\n3.High Fever(>102F)\n4.Don't know\n"))

    if(temp==1 or temp==2 or temp==3 or temp==4):
        symp();
    else:
        print("\nWrong Entry!, Sorry start from the beginning!")
        yep();

def trav():

    print("\nNow please select your travel and exposure details:")
    tra=int(input("\n1.No Travel History\n2.No contact with anyone with Symptoms\n3.History of abroad travel in last 14 days\n"))

    if tra==1 or tra==2:
            hist();
    elif tra==3:
            final();
    else:
        print("\nWrong Entry!, Sorry start from the beginning!")
        yep();
        
def symp():

    global ris,symptoms,g;
    ris=0;
    
    print("\nAre you experiencing any of the symptoms below?")
    symptoms=["Dry cough","Sore throat","Weakness","Change in Appetite","Difficulty in Breathing","Drowsiness","none of these"]
    for i in range(len(symptoms)):
        print(i+1,".",symptoms[i])
        
    g=int(input("\n"))
    if (g==1 or g==2 or g==3 or g==4 or g==5 or g==6):
           ris=ris+1;
           trav();
          
    elif(g==7):
          trav();
    else:
        print("\nWrong Entry!, Sorry start from the beginning!")
        yep();
          
def hist():
    print("\nDo you have any of these conditions?")
    his=int(input("\n1.diabetes\n2.High Blood Pressure\n3.Heart disease\n4.Lung diseases\n5.None of these\n"));

    if(his==1 or his==2 or his==3 or his==4):
        if(ris!=0):
            final();
        else:
            print("Except this condition, there is no more sign for corona.,\n")
            good();
    elif(his==5):
        if(ris==0):
            good();
        else:
            print("Good.. But still it is suggested to have a physical test at nearby Hospital! As you have the",symptoms[g-1],"Symptom")
    else:
        print("\nWrong Entry!, Sorry start from the beginning!")
        yep();
    
    
def good():
    
    print("\nThat's good., You are all fine!")
    
def final():

    print("Seems Risky.., It is recommmended to have a physical test at nearby hospital!")
    

intr="Hello and Welcome to Coronavirus Self-Assess Test!"
intr2="Created by Santhosh"

print(intr.center(75,"*"))
print(intr2.center(75,"~"))

a=input("\nPlease enter your name: ")
name=a.capitalize()

print("\nHello, {}.. here I have created a assessment scan., Do answer the questions honestly!".format(name))
print("So, lets get started!")
print("\nNOTE: For Multi choice questions, Reply your answers with respective numbers (i.e., 1,2..etc.)")

age=int(input("\nHow old are you? "))

if(age>12):
    gen=int(input("\nplease select your gender:\n1.Male\n2.Female\n3.Others\n"))
    if(gen==1 or gen==2 or gen==3):
            yep();
    else:
        print("\nWrong Entry!, Sorry start from the beginning!")
else:
    print("\nSorry! This Assess test suits only for the agers above 12.");
    
print("\nThanks for your time, {}..\n\nProgrammed by Santhosh ~ VCET IT 1st year.".format(name));
print("\nSTAY HOME! STAY SAFE!")


