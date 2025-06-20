# variable name and the technique of writing variable name
firstNumber=50  # this is the camel case 
_second_number=100  # this is the snake case
ThirdNumber=67  # this is the Pascal case
print(firstNumber)
print(_second_number)
print(ThirdNumber)


a=5
b='Python'
c=True
d=5.15
print(type(a))
print(type(b))
print(type(c))
print(type(d))



#many values to multiple variables
e,f,g='apple','ball','cat'
print(e,f,g) #o/p in the single line

#one values to the multiple variables
h=i=j='Python Django'
print(h) #o/p in the multiple lines
print(i)
print(j)

#unpack the collection
animals=['ant','bee','bug','spider']
k,l,m,n=animals
print(k,m,l,n,)
print(m,k,l,n,)





x='€guifo'
def func():
    print('my name is'+x)
func()


name='Python'
def my_fun():
    name='Django'
    print('This is '+name)
my_fun()
print('This is'+name)




lang='spiderman'
def hero():
    global lang
    lang='batman'
    print("He is "+ lang)
hero()
print('He is'+lang)