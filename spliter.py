#Takes an string input
txt = input()

#Creats a function that takes the input above and splits the words when there is a space
def words(txt):
    for word in txt.split(' '):
        yield word

#Prints a list of the input but now with the words seperated 
print(list(words(txt)))
