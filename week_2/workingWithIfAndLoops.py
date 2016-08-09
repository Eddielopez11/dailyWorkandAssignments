# Assignment working with if and loops

people = []
done = False

while not done:
    name = input('Who would you like to add? ')
    color = (input('what is ' + name + "'s favorite color? "))
    age = (input('thats a sucky color, how old is ' + name + "? "))
    answer = input('Would you like to add another person? ')
    if answer == "no":
        done = True
    people.append({'name': name, 'color': color, 'age': age})

for n in people:
     print('Name: ' + n['name'])
     print('Color: ' + n['color'])
     print('Age: ' + n['age'])
