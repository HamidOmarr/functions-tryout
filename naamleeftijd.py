def indentiteit():
    while True:
        name = input('Naam?')
        Leeftijd = input('Leeftijd?')
        print ('Hallo, ' + name +'.' ' Je bent ' + Leeftijd + ' jaar oud.')
        if name == 'stop' or Leeftijd == 'stop' :
            quit()
        else:
            continue

indentiteit()