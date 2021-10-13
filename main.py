import json

def getData():
    f = open("./apiResponse.json", "r")
    return f.read()


#Funktion getData() returnere JSON som string, som en API for eksempel kunne gøre. 
#Svaret fra getData() skal parses som JSON, så det bliver muligt at data behandle det i Python. 
#Lav herefter en funktion der tager alt data ind og KUN returnere brugere hvis mail ikke er et .com domæne, 
#og hvis gender hverken er "Male" eller "Female". Data'en skal være sorteret efter IP, men kun tallet mellem 1. og 2. punktum. 

