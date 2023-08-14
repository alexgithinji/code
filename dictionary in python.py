capitals ={"USA":"Washington Dc",
           "India":"New Delhi",
           "China":"Beijing",
           "Russia":"Moscow"}

capitals.update({"German":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")
#print(capitals["Russia"])
#print(capitals.get("Nairobi"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key,value)