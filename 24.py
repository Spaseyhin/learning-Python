hash = {
    '1': 'something',
    2 : 'other'
}

print(hash['1'])
print(hash[2])

a = 1
b = 2 
print(a, 'hello', b)

print(type(int(float('12.5'))))

a = ['something', 'text']

text = ', '.join(a) 
print(text)
print(type(text))

new_text = text.replace('text', 'words')
print(new_text)

setup = "a duck goes into a bar..."
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous', 100))