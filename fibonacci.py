def fibonacci(positie):
    voriggetal = 1
    getal = 1
    voriggetal = getal
    for i in range (positie):
        toekomstgetal = voriggetal + getal
      
        voriggetal = getal
        getal = toekomstgetal

    return toekomstgetal
   


print (fibonacci(6))