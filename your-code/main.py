#KIND REMAIND:
        # 2x3x5 3-dimensional array
        # 2 parrafos 
        # 3 lineas
        # 5 columnas


#1. Import the NUMPY package under the name np.

import numpy as np
import random

#2. Print the NUMPY version and the configuration.

print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

###3.1 . use random.random array method

array_m1 = np.random.random((2,3,5))

#dos parrafos por 3 lineas por 5 columnas 

#print(array_m1)

###3.2.create an empty array and fill it with random numbers with randint

array_m2 = np.zeros((2,3,5))

#print(array_m2)

"""

### -----ERROR FATAL ----- ###

Realmente aqui accedemos al valor del elemento y lo asignamos a una varible, 
luego sobreescribes el valor de la variable, pero no estas sobreescribiendo el 
elemento en si. 

****HAY QUE HACELO CON INDICES

for i in array_m2:
        for sub_i in i:
                for sub_sub_i in sub_i:
                        print(sub_sub_i)
                        #No accedes al elemento como tal sino al valor del elemento.
                        sub_sub_i = random.randint(0,100)
                        print(sub_sub_i)

print(array_m2)
"""

#OPCION CORRECTA (accediendo al elemento):

for i in range(len(array_m2)):
        for sub_i in range(len(array_m2[i])):
                for sub_sub_i in range(len(array_m2[i][sub_i])):
                        array_m2[i][sub_i][sub_sub_i] = random.randint(0,100)

#print(array_m2)


#4. Print a.

a = array_m1
print("-----ARRAY A------")
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3),dtype=np.int16)


#6. Print b.

print("-------ARRAY B-------")
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

"Yes, (5x2x3) == (2x3x5)"

print(a.size == b.size)

#8. Are you able to add a and b? Why or why not?

"No, because they are not the same shape"

#print(a + b ) 
"""ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) """

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

"OJO: se transponse con las posiciones de las dimensiones si (2,3,5) (0,1,2) --> (5,3,2) -->(2,1,0)"

c = np.transpose(b, (1, 2, 0))
print("-----ARRAY C (b transposed)------")
print(c)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print("-----ARRAY D (a + c) ------")
print(d)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("-----ARRAY A + D ------")
print(a+d)

"d = 2*a + c(1)"

#12. Multiply a and c. Assign the result to e.

e = a * c

print("-----ARRAY E (a * c) ------")
print(e)


#13. Does e equal to a? Why or why not?

print (" E == A ")
print(e == a)
"Yes because you multiply for 1's matrix"

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()

d_min = d.min()
 
d_mean = d.mean()

print(" MAX value in d {d_max} \n MIN value in d {d.min} \n MEAN value in d {d_mean}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

print("-----ARRAY F ------")
print(f)

f.shape

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

"""
#Voy a redefinir D para ver donde esta el error:

d = np.array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

d_max = d.max()

d_min = d.min()
 
d_mean = d.mean()
"""

print("------------------- EJERCICIO FINAL ------------------------")

print("--------- ARRAY F - vacia --------")
print(f)

#####CUIRIOSO, MUY CURIOSO##### 
#Cuando numpy genera una matriz vacia F la ha completado
#con los mismos valores que A (que tambien era una matriz vacia Random)
# Al parecer cuando python genera una matriz "vacia", no esta vacia como tal 
#sino que le asigna valores random. Se ve que al volver a ejecutar 
#mantiene los mismos valores.

for i in range(len(f)):
        for b in range(len(f[i])):
                for e in range(len(f[i][b])):
                        val_pos_f = f[i][b][e]
                        val_pos_d = d[i][b][e]

                        "if it's larger than d_min but smaller than d_mean,"
                        "assign 25 to the corresponding value in f."

                        if val_pos_d > d_min and val_pos_d < d_mean:
                                f[i][b][e] = 25

                        "If a value in d is larger than d_mean but smaller than d_max," 
                        "assign 75 to the corresponding value in f."

                        if val_pos_d > d_mean and val_pos_d < d_max:
                                f[i][b][e] = 75

                        "If a value equals to d_mean, assign 50" 
                        "to the corresponding value in f."

                        if val_pos_d == d_mean:
                                f[i][b][e] = 50

                        "Assign 0 to the corresponding value(s) in f for d_min in d."

                        if val_pos_d == d_min:
                                f[i][b][e] = 0
                        
                        "Assign 100 to the corresponding value(s) in f for d_max in d."

                        if val_pos_d == d_max:
                               f[i][b][e] = 100 


print("--------- ARRAY D -----------")
print(d)

print("-------ARRAY F TRANSFORMADA-------------")
print(f)
                    

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

#Cuando creamos un ARRAY (matriz) por defecto lo crea de tipo float
#En una array todos los elementos tienen que ser del mismo tipo 
#Existe un tipo que es objeto que engloba "cualquier otro tipo" - mas o menos
#Para castear un array hay que hacerlo con la array entera. 
#No se puede castear individual por elemento (accediendo al elemento --> Suerte, animo y de todo.
f = f.astype('object')

for i in range(len(f)):
        for b in range(len(f[i])):
                for e in range(len(f[i][b])):
                        val_pos_f = f[i][b][e]


                        # 25 now B

                        if val_pos_f == 25:
                                f[i][b][e] = "B"

                        # 75 now D

                        if val_pos_f == 75:
                                f[i][b][e] = "D"

                        # 50 now C

                        if val_pos_f == 50:
                                f[i][b][e] = "C"

                        # 0 now A

                        if val_pos_f == 0:
                                f[i][b][e] = "A"
                        
                        # 100 now E

                        if val_pos_f == 100:
                               f[i][b][e] = "E"


print("-------ARRAY F con LETRAS -------------")
print(f)

