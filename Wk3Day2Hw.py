#Exercise #1
#Filter out all of the empty strings from the list below
#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

#solution 1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

new_places_list = list(filter(lambda x: x.strip(), places))
#strip removes white spaces
print(new_places_list)

#Exercise #2
#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF",\
"Gary A.J. Bernstein"]
print(author)

author = sorted(author, key = lambda x: x.split()[1])
print(author)

#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# F = (9/5)*C + 32
#places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

c_places = list(map(lambda x: (x[0],x[1]*1.8+32), places))
print(c_places)

#Exercise #4
#Write a recursion function to perform the fibonacci sequence up to the number passed in.

#Output for fib(5) => 
#ExerciseIteration 0: 1
#Iteration 1: 1
#Iteration 2: 2
#Iteration 3: 3
#Iteration 4: 5
#Iteration 5: 8

def Fibo(n):
    if n <=1:
        return 1
 
    else:
        return Fibo(n-1) + Fibo(n-2)

my_num = 10

if my_num < 0:
   print("The number has to be bigger than 0")
else:
   print("Fibonacci sequence:")
   for i in range(my_num):
       print(Fibo(i))
