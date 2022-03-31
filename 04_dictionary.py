dict={
    "Hello" : "Greeting",
    "corona": "Virus",
    "Human" : "Living beings",
    "Marks" : [ 34, 76, 92],
    "nestedict":{"Human": 'Immortal',}
}
print(dict['corona'])
print(dict['Marks'])
# nested dictionary
print(dict['nestedict']['Human'])
dict['Marks']= [43, 67, 29]
print(dict['Marks'])
print(dict.get("Human"))
print(dict.get("Humans"))  #returns none if key unavailable


# solutions
mydict={ 
         "me" : "I",
         "you" : "they",
         "them" : "their",
         "swim" : "water",
         "fly" : "air",
         "walk" : "road",
}
print("Options are-" , mydict.keys())
w=input("User look for a word- \n")
# print("Meaning of your word is-" , mydict[w])    throws error if not exist
print("Meaning of your word is-" , mydict.get(w))


