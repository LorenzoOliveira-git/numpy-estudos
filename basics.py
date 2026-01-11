#%%

import numpy as np

#O irmpontante dentro do numpy é entender a diferença entre esses nomes que podem comumente aparecer:
#Tipos de arrays são chamados de "ndarrays" - N quer dizer um número especifico e D para dimensões
#1-D array: Possui apenas uma dimensão e é chamado comumente de vetor ou vector
#2-D array: Possui duas dimensões e é chamado comumente por matrix ou matrix
#3-D array: Possui 3 ou mais dimensões e é chamado comumente de tensor

#Utilidades principais da biblioteca:
#É a base para quase todos os processamentos de dados quando se diz em rapidez de processamento, pois um loop for, por exemplo, no python puro, demoraria muito mais do que eu simplesmente manipular os mesmos dados com o próprio numpy. (OBS: Por trás, o numpy roda em linguagem C e não em python, pois o fato da linguagem C ser uma linguagem compilada, ela dá muito mais poder de performace para rodar diversos cálculos com bases de dados gigantes)
#Vetorização de dados: pensar os dados como blocos, e não como loops (o mesmo ocorre com o pandas, onde os dataframes tratam os dados em linhas e colunas, o que permite mudar uma grande quantidade de dados sem a necessidade de um loop). Um exemplo disso é em uma pedido para aumentar o salário de todos os funcionários em 10%, com o loop isso ia demorar muito, já com o numpy (que trabalha em blocos) esse processo fica muito mais rápido e légivel.
#DIVERSAS bibliotecas de ciência de dados trabalhas com essa biblioteca no background.
#É uma biblioteca ótima para trabalhas com estatísticas.
#É a base do machine learning. Essa tecnologia não faz os seus cálculos com dataframas, e sim com arrays numpy.
#Armazena menos memória em relação a lista python por exemplo.
#É exelente para limpeza e transformação de dados, um dos trabalhos do próprio ciêntista de dados.

#Attibutes of numpy arrays

#Number of dimension
np.ndarray.ndim

#Number of line and columns in a numpy array, represented for (n,m), n = rows m = columns
np.ndarray.shape

#Type of data in numpy array
np.ndarray.dtype

#Size of type data in numpy array, in other words, if you have the type int64, the result is 8, because the attribute gets the number of bytes (64) and divite to 4.
np.ndarray.itemsize

#Size of array
np.ndarray.size

# %%

#let's make a new array - this is the simple array, but you type it's ndarray
array1 = np.array([1,2,3])
type(array1)

# %%

#Let's make a new array with more than dimension
array2 = np.array([(1,2,3),(1,3,4)])
array2

# %%
np.array([[1,2,3,4],[2,4,5,6]])

#You can especific the array's data type in onw method
array3 = np.array([[1,2,3],[4,5,6]],dtype=np.complex128)
array3

# %%

#You can make null matriz (matriz only zeros), indentity matrix (matriz only ones) 
zeros = np.zeros([5,5])
zeros
ones = np.ones([5,5])
ones
#The default type data is float64, if you change the type, you have to use the parameter dtype=

# %%

#If you need the array with one sequence of numers, use the method arange, the first argument is the number initial value, the second number is the end value and the third value is of how much in how much it will jump.
sequence = np.arange(3,4,0.2)

#But, if you want a specific number of data in you array, use this method: (The third parameter is the number of data that you need)
sequence = np.linspace(0,2,40)

#%%%
# add a new dimension in your array
array = np.array([1,2,3])
print(array.shape)
print(array.ndim)

array2 = array[np.newaxis,:]
print(array2.shape)
print(array.ndim)
print(array2)

array3 = array[:,np.newaxis]
print(array3.shape)
print(array.ndim)
print(array3)

# %%

#To access values in array
#       0 1 2
#     columns
#0 line 1 1 1
#1      1 1 1
#2      1 1 1
#it's the same way with pandas, you access values in array for index
array = np.array([[1,2,3],
                 [1,5,9]])
# I want to get the number 5 in my array
print(array[1][1])

# %%

#concat arrays
a = np.array([1,2,3])
b = np.array([2,3,5])

c = np.concatenate((a,b))
d = np.concatenate((b,a))

print(c)
print(d)

# %%
