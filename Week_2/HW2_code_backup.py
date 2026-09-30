 1/1:
import pandas as pd
import numpy as np
 2/1: import numpy as np
 2/2: a = np.zeros(5)
 2/3:
a = np.zeros(5)
print(a)
 2/4:
a = np.zeros(3,5)
print(a)
 2/5:
a = np.zeros((3,5))
print(a)
 2/6:
a = np.zeros((3,5), dtype=int)
print(a)
 2/7:
b = np.ones(5)
print(b)
 2/8: np.full(10)
 2/9:
c = np.full(10,5)
print(c)
2/10:
d = np.arange(10,50)
print(d)
2/11:
d = np.arange(10,50,5)
print(d)
2/12: np.linspace(1,10)
2/13: np.linspace(1,10,2)
2/14: np.linspace(1,10,10)
2/15: np.linspace(1,10,10)
2/16: np.zeros(5,2)
2/17: np.zeros((5,2))
2/18: np.arange(10,50,5)
2/19:
np.array(
    [1,2,3]
    [4,5,6]
    [7,8,9]
         )
2/20:
np.array(
    [1,2,3],
    [4,5,6],
    [7,8,9]
         )
2/21:
np.array((
    [1,2,3],
    [4,5,6],
    [7,8,9])
         )
2/22:
np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
         )
2/23: f[:]
2/24:
f = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
         )
2/25: f[:]
2/26: f[:,1]
2/27: f[2,:]
2/28:
## randomly generated arrays

np.random.rand(5,4)
2/29:
## randomly generated arrays

np.random.seed(5,4)
2/30:
## randomly generated arrays

np.random.seed(5)
2/31:
## randomly generated arrays

x = np.random.seed(5)
2/32:
## randomly generated arrays

x = np.random.seed(5)
print(x)
2/33:
## randomly generated arrays

np.random.rand(5,4)
2/34:
## randomly generated arrays

np.random.rand(5,4)
2/35:
## randomly generated arrays

np.random.rand(5,4)
2/36:
## randomly generated arrays

np.random.rand(5,4)
2/37:
## randomly generated arrays

np.random.seed(2) ## makes sure that the random numbers are the same every time you run the code
np.random.rand(5,4)
2/38:
## randomly generated arrays

np.random.seed(3) ## makes sure that the random numbers are the same every time you run the code
np.random.randn(5,4)
2/39:
## randomly generated arrays

np.random.seed(3) ## makes sure that the random numbers are the same every time you run the code
np.random.randn(5,4) ## generates random numbers from a normal distribution with mean 0 and standard deviation 1
2/40:
np.random.seed(4)
np.random.randint(low=0,high=1000,size=(5,5))
2/41: a = np.arange(5)
2/42:
a = np.arange(5)
a+1
2/43:
a = np.arange(5)
print(a)
2/44:
a = np.arange(5)
print(a)

a+1
 3/1: import pandas as pd
 3/2:
data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]
 3/3: a = pd.DataFrame(data)
 3/4:
a = pd.DataFrame(data)
print(a)
 3/5:
a = pd.DataFrame(data,columns=columns)
print(a)
 3/6:
a = pd.DataFrame(data)
print(a)
 3/7:
a = pd.DataFrame(data, columns=columns)
print(a)
 3/8:
df = pd.DataFrame(data, columns=columns)
print(df)
 3/9: df.Make
3/10: df['Make']
3/11: df[['Make', 'Engine HP', 'MSRP']]
3/12: df.index
3/13:
df.index #shows the index of the dataframe which means the row numbers
df.Make.index
3/14: df.loc[1]
3/15: df.loc[1,2]
3/16: df.loc[[1,2]]
3/17: df.iloc[[1,2]]
3/18:
df.id = [1,2,3,4,5]
df.loc[[1,2]]
3/19:
df.id = [a,b,c,d,e] #adds a new column to the dataframe
df.loc[[1,2]]
3/20:
df.id = [a,b,c,d,e] #adds a new column to the dataframe
df.head()
3/21:
df.id = ['a','b','c','d','e'] #adds a new column to the dataframe
df.head()
3/22:
df.id = ['a','b','c','d','e'] #adds a new column to the dataframe
df
3/23:
df.id = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index
3/24:
df.id = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index
df
3/25:
df.id = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index('id', inplace=True) #sets the index of the dataframe to the 'id' column
df
3/26:
df['id'] = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index('id', inplace=True) #sets the index of the dataframe to the 'id' column
df
3/27: df.reset_index(inplace=True) #resets the index of the dataframe to the default integer index
3/28: df.reset_index(inplace=True) #resets the index of the dataframe to the default integer index
3/29:
df.reset_index(inplace=True) #resets the index of the dataframe to the default integer index
df
3/30:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df
3/31:
df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
3/32:
df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
3/33:
df = df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
3/34:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df
3/35:
df['id'] = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index('id') #sets the index of the dataframe to the 'id' column
df
3/36:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True) #drops the columns 'level_0' and 'index' from the dataframe
3/37:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True) #drops the columns 'level_0' and 'index' from the dataframe
df
3/38:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True) #drops the columns 'level_0' and 'index' from the dataframe
df.columns
3/39:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True, errors='ignore')
df.columns
3/40:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True, errors='ignore')
df
 4/1:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True, errors='ignore')
df = df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
 4/2: df.iloc[[1,2]]
 4/3: import numpy as np
 4/4:
a = np.zeros((3,5), dtype=int)
print(a)
 4/5:
b = np.ones(5)
print(b)
 4/6:
c = np.full(10,5)
print(c)
 4/7:
d = np.arange(10,50,5)
print(d)
 4/8: np.linspace(1,10,10)
 4/9: np.zeros((5,2))
4/10:
f = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
         )
4/11: f[2,:]
4/12:
## randomly generated arrays

np.random.seed(2) ## makes sure that the random numbers are the same every time you run the code
np.random.rand(5,4)
4/13:
## randomly generated arrays

np.random.seed(3) ## makes sure that the random numbers are the same every time you run the code
np.random.randn(5,4) ## generates random numbers from a normal distribution with mean 0 and standard deviation 1
4/14:
np.random.seed(4)
np.random.randint(low=0,high=1000,size=(5,5))
4/15:
a = np.arange(5)
print(a)

a+1
4/16: import pandas as pd
4/17:
data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]
4/18:
df = pd.DataFrame(data, columns=columns)
print(df)
4/19:
df['Make']
#df.Make
4/20: df[['Make', 'Engine HP', 'MSRP']]
4/21:
df.index #shows the index of the dataframe which means the row numbers
df.Make.index #shows the index of the series which means the row numbers
4/22:
df['id'] = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index('id') #sets the index of the dataframe to the 'id' column
df
4/23: df.iloc[[1,2]]
4/24:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True, errors='ignore')
df = df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
4/25: df = df.set_index('id') #sets the index of the dataframe to the 'id' column
4/26:
df = df.set_index('id') #sets the index of the dataframe to the 'id' column
df
4/27: df = df.set_index('id') #sets the index of the dataframe to the 'id' column
4/28: df = df.set_index('id', drop=False) #sets the index of the dataframe to the 'id' column
4/29: df = df.set_index('id', drop=True) #sets the index of the dataframe to the 'id' column
4/30: df.set_index('id', drop=True) #sets the index of the dataframe to the 'id' column
4/31: df
4/32: df['Engine HP']
4/33: df['Engine HP']/100
4/34: df['Year'] > 2015
4/35: df[df['Year']] > 2015
4/36: df[df['Year'] > 2015]
4/37:
df[
    df['Year'] > 2015 & df['Make'] == 'Nissan'
]
4/38:
df[
    (df['Year'] > 2015) & (df['Make'] == 'Nissan')
]
4/39: df['Vehicle_Style']
4/40: df['Vehicle_Style'].str.lower()
4/41: df['Vehicle_Style'] = df['Vehicle_Style'].str.lower()
4/42:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower()
df['Vehicle_Style']
4/43:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower(inplace=True) 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_', inplace=True)
4/44:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower(inplace=True) 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_')
4/45:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower() 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_')
4/46:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower() 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_')
df
4/47:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower() 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_')
df['Vehicle_Style']
4/48: df.MSRP
4/49: df.MSRP.min()
4/50: df.MSRP.min
4/51: df.MSRP.min()
4/52: df.MSRP.max()
4/53: df.MSRP.mode()
4/54: df.MSRP.desc()
4/55: df.MSRP.describe()
4/56: df.describe()
4/57: df.describe(include='all')
4/58: df.describe()
4/59: df.describe().round(1)
4/60: df.Make.nunique
4/61: df.Make.nunique<>
4/62: df.Make.nunique()
4/63:
df.Make.nunique()
df.Make.nunique
4/64:
df.nunique()
df.Make.nunique
4/65:
df.nunique()
df.Make.nunique
4/66:

df.Make.nunique
4/67: df.nunique()
4/68: df.nunique()
4/69: df.isnull()
4/70: df.isnull()
4/71: df.isnull().sum() #shows the number of missing values in each column
4/72:
## Grouping and aggregating data

df.groupby('Transmission Type').MSRP.mean())
4/73:
## Grouping and aggregating data

df.groupby('Transmission Type').MSRP.mean()))
4/74:
## Grouping and aggregating data

df.groupby('Transmission Type').MSRP.mean())
4/75:
## Grouping and aggregating data

df.groupby('Transmission Type').MSRP.mean()
4/76:
## Grouping and aggregating data

df.groupby('Transmission Type').(`MSRP`).mean()
4/77: df.isnull().sum() #shows the number of missing values in each column
4/78: df.groupby('Transmission Type').agg({'MSRP': 'mean'})
4/79: df.groupby('Transmission Type').agg({'MSRP': 'mean'})
4/80: df.groupby('Transmission Type','MSRP').mean()
4/81:
df.groupby('Transmission Type').MSRP.mean()
#df.groupby('Transmission Type','MSRP').mean()
4/82: df.groupby(['Transmission Type', 'Make']).mean()
4/83: df.groupby(['Transmission Type', 'Make']).MSRP.mean()
4/84:
# several stats on one column
df.groupby('Transmission Type').agg({'MSRP': ['mean', 'median', 'count']})
4/85:
# several stats on one column
df.groupby('Transmission Type').agg({'MSRP': ['mean', 'median', 'count']})
4/86: df.groupby('Transmission Type').agg({'MSRP': 'mean', 'Engine HP': 'max'})
4/87: df.groupby('Transmission Type').agg({'MSRP': 'mean', 'Engine HP': 'max'})
4/88:
df.groupby('Transmission Type').agg(
    avg_price=('MSRP', 'mean'),
    n=('MSRP', 'count')
)
4/89: df
4/90: df.groupby(['Make','Transmission Type']).agg({'Engine HP':'mean'})
4/91: df.groupby(['Make','Transmission Type']).agg({'Engine HP':'max'})
4/92:
df.groupby(['Year','Make']).agg(
    max_horsepower=('Engine HP','max'),
    avg_price=('MSRP','mean')) 
)
4/93:
df.groupby(['Year','Make']).agg(
    max_horsepower=('Engine HP','max'),
    avg_price=('MSRP','mean')
)
4/94: df
4/95: df
4/96: df.Year.values
4/97: df.Year.value_counts()
4/98: df.Year.value_counts()
4/99: df.to_dict("dict")
4/100: df.to_dict()
4/101: df.to_dict(orient='records')
4/102: df.to_dict(orient='records')
4/103:
u = np.array([1,2,3])
v = np.array([4,5,6])

def vector_multiplication (u,v):
    return u*v
4/104:
u = np.array([1,2,3])
v = np.array([4,5,6])

def vector_multiplication (u,v):
    return u*v

vector_multiplication(u,v)
4/105:
u = np.array([1,2,3])
v = np.array([4,5,6])

def vector_multiplication (u,v):
    return np.dot(u,v)

vector_multiplication(u,v)
4/106:
u = np.array([1,2,3])
v = np.array([4,5,6])
4/107:
def vector_multiplication (u,v):
    return np.dot(u,v)
# return u*v #Hadamard product

vector_multiplication(u,v)
4/108:
u = np.array([1,2,3])
v = np.array([4,5,6])

u.shape()
4/109:
u = np.array([1,2,3])
v = np.array([4,5,6])

u.shape
4/110:
u = np.array([1,2,3])
v = np.array([4,5,6])

u.shape
v.shape
4/111:
u = np.array([1,2,3])
v = np.array([4,5,6])

#u.shape
v.shape
4/112:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    return np.dot(u,v)
# return u*v #Hadamard product

vector_multiplication(u,v)
4/113:
u = np.array([1,2,3])
v = np.array([4,5,6])

#u.shape
v.shape

n = u.shape
print(n)
4/114:
u = np.array([1,2,3])
v = np.array([4,5,6])

#u.shape
#v.shape

n = u.shape
print(n)
4/115:
u = np.array([1,2,3])
v = np.array([4,5,6])

#u.shape
#v.shape

n = u.shape[0]
print(n)
4/116:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    n = u.shape[0] # assigns the total value of the first dimension of the array to n which is the number of elements in the vector

    result == 0.0

    for i in range(n):
        result = result + u[i]*v[i]






    #return np.dot(u,v)
    # return u*v #Hadamard product

vector_multiplication(u,v)
4/117:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    n = u.shape[0] # assigns the total value of the first dimension of the array to n which is the number of elements in the vector

    result == 0.0

    for i in range(n):
        result = result + u[i]*v[i]

    return result




    #return np.dot(u,v)
    # return u*v #Hadamard product

vector_multiplication(u,v)
4/118:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    n = u.shape[0] # assigns the total value of the first dimension of the array to n which is the number of elements in the vector

    result == 0.0

    for i in range(n):
        result = result + u[i]*v[i]

    return result

    #return np.dot(u,v)
    # return u*v #Hadamard product

vector_multiplication(u,v)
4/119:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    n = u.shape[0] # assigns the total value of the first dimension of the array to n which is the number of elements in the vector

    result = 0.0

    for i in range(n):
        result = result + u[i]*v[i]

    return result

    #return np.dot(u,v)
    # return u*v #Hadamard product

vector_multiplication(u,v)
4/120:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
4/121:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([[10,11,12]])
4/122:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])
4/123:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])
print b
4/124:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])
print(b)
4/125:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])

a.shape()
4/126:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])

a.shape
4/127:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])

a.shape
b.shape
4/128:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])

#a.shape
b.shape
4/129:
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
     ])
b = np.array([10,11,12])

#a.shape
a.shape
4/130:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape
4/131:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape
4/132:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape[0]
4/133:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape[1]
4/134:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape[2]
4/135:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape[1]
4/136:
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
b = np.array([10,11,12])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array
4/137:
def matrix_vector_multiply(a,b):
    assert a.shape[1] == b.shape[0]

    num_rows = a.shape[0]
 6/1:
## computing a*b

## a is a 3x4 matrix
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
## b is a 1x3 matrix
b = np.array([10,11,12])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array

result = 0.0

def matrix_vector_multiplication(a,b):

    assert b.shape[1] == a.shape[0]
    n_mat1 = a.shape[0] ## assigns the number of rows in the first matrix
    n_mat2 = b.shape[1] ## assigns the number of columns in second matrix

    for i in range(n_mat1): 
        for j in range(n_mat2):
            result = result + a[i]*b[j]
    return result
 6/2: import numpy as np
 6/3:
a = np.zeros((3,5), dtype=int)
print(a)
 6/4:
b = np.ones(5)
print(b)
 6/5:
c = np.full(10,5)
print(c)
 6/6:
d = np.arange(10,50,5)
print(d)
 6/7: np.linspace(1,10,10)
 6/8: np.zeros((5,2))
 6/9:
f = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
         )
6/10: f[2,:]
6/11:
## randomly generated arrays

np.random.seed(2) ## makes sure that the random numbers are the same every time you run the code
np.random.rand(5,4)
6/12:
## randomly generated arrays

np.random.seed(3) ## makes sure that the random numbers are the same every time you run the code
np.random.randn(5,4) ## generates random numbers from a normal distribution with mean 0 and standard deviation 1
6/13:
np.random.seed(4)
np.random.randint(low=0,high=1000,size=(5,5))
6/14:
a = np.arange(5)
print(a)

a+1
6/15: import pandas as pd
6/16:
data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]
6/17:
df = pd.DataFrame(data, columns=columns)
print(df)
6/18:
df['Make']
#df.Make
6/19: df[['Make', 'Engine HP', 'MSRP']]
6/20:
df.index #shows the index of the dataframe which means the row numbers
df.Make.index #shows the index of the series which means the row numbers
6/21:
df['id'] = ['a','b','c','d','e'] #adds a new column to the dataframe
df.set_index('id') #sets the index of the dataframe to the 'id' column
df
6/22: df.iloc[[1,2]]
6/23:
df.reset_index(drop=True, inplace=True) #resets the index of the dataframe to the default integer index
df.drop(columns=['level_0', 'index'], inplace=True, errors='ignore')
df = df.reset_index(drop=True) #resets the index of the dataframe to the default integer index
df
6/24: df
6/25: df['Engine HP']/100
6/26:
df[
    (df['Year'] > 2015) & (df['Make'] == 'Nissan')
]
6/27:
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower() 
df['Vehicle_Style'] = df['Vehicle_Style'].str.replace(' ', '_')
df['Vehicle_Style']
6/28: df.MSRP.describe()
6/29: df.describe().round(1)
6/30: df.describe(include='all')
6/31:

df.Make.nunique
6/32: df.nunique()
6/33: df.isnull()
6/34: df.isnull().sum() #shows the number of missing values in each column
6/35: df.groupby('Transmission Type').agg({'MSRP': 'mean'})
6/36:
df.groupby('Transmission Type').MSRP.mean()
#df.groupby('Transmission Type','MSRP').mean()
df.groupby('Transmission Type').agg({'MSRP': 'mean'})
6/37: df.groupby(['Transmission Type', 'Make']).MSRP.mean()
6/38:
# several stats on one column
df.groupby('Transmission Type').agg({'MSRP': ['mean', 'median', 'count']})
6/39: df.groupby('Transmission Type').agg({'MSRP': 'mean', 'Engine HP': 'max'})
6/40:
df.groupby('Transmission Type').agg(
    avg_price=('MSRP', 'mean'),
    n=('MSRP', 'count')
)
6/41: df
6/42: df.groupby(['Make','Transmission Type']).agg({'Engine HP':'max'})
6/43:
df.groupby(['Year','Make']).agg(
    max_horsepower=('Engine HP','max'),
    avg_price=('MSRP','mean')
)
6/44: df
6/45: df.Year.value_counts()
6/46: df.to_dict(orient='records')
6/47:
u = np.array([1,2,3])
v = np.array([4,5,6])

#u.shape
#v.shape

n = u.shape[0]
print(n)
6/48:
def vector_multiplication (u,v):
    assert u.shape[0] == v.shape[0], "Vectors must be the same shape"
    n = u.shape[0] # assigns the total value of the first dimension of the array to n which is the number of elements in the vector

    result = 0.0

    for i in range(n):
        result = result + u[i]*v[i]

    return result

    #return np.dot(u,v)
    # return u*v #Hadamard product

vector_multiplication(u,v)
6/49:
## computing a*b

## a is a 3x4 matrix
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
## b is a 1x3 matrix
b = np.array([10,11,12])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array

result = 0.0

def matrix_vector_multiplication(a,b):

    assert b.shape[1] == a.shape[0]
    n_mat1 = a.shape[0] ## assigns the number of rows in the first matrix
    n_mat2 = b.shape[1] ## assigns the number of columns in second matrix

    for i in range(n_mat1): 
        for j in range(n_mat2):
            result = result + a[i]*b[j]
    return result
6/50:
def matrix_vector_multiply(a,b):

    assert a.shape[1] == b.shape[0]

    num_rows = a.shape[0]
    num_cols = b.shape[1]

    result = np.zeros((num_rows, num_cols))  #needs to align with the size of the matrix multiplication result

    for i in range(num_rows):
        for j in range(num_cols): 
            result [i,j]= result + a[i,j]
6/51:
## computing a*b

## a is a 3x4 matrix
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
## b is a 1x3 matrix
b = np.array([10,11,12])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array

result = 0.0

def matrix_vector_multiplication(a,b):

    assert b.shape[1] == a.shape[0]
    n_mat1 = a.shape[0] ## assigns the number of rows in the first matrix
    n_mat2 = b.shape[1] ## assigns the number of columns in second matrix

    for i in range(n_mat1): 
        for j in range(n_mat2):
            result = result + a[i]*b[j]
    return result

matrix_vector_multiplication(a,b)
6/52:
## computing a*b

## a is a 3x4 matrix
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
## b is a vector
b = np.array([10,11,12,13])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array

n_mat1 = a.shape[0] ## assigns the number of rows in the first matrix
n_mat2 = a.shape[1] ## assigns the number of columns in second matrix

result = np.zeros(n_mat1)

def matrix_vector_multiplication(a,b):

    assert a.shape[1] == b.shape[0]
    

    for i in range(n_mat1): 
        for j in range(n_mat2):
            result = result + a[i]*b[j]
    return result

matrix_vector_multiplication(a,b)
6/53:
## computing a*b

## a is a 3x4 matrix
a = np.array(
    [[1,2,3,4],
     [4,5,6,6],
     [7,8,9,10]
     ])
## b is a vector
b = np.array([10,11,12,13])

#a.shape
a.shape[0] #shows the number of rows in the array
a.shape[1] #shows the number of columns in the array

n_mat1 = a.shape[0] ## assigns the number of rows in the first matrix
n_mat2 = a.shape[1] ## assigns the number of columns in second matrix

result = np.zeros(n_mat1)

def matrix_vector_multiplication(a,b):

    assert a.shape[1] == b.shape[0]
    

    for i in range(n_mat1): 
        for j in range(n_mat2):
            result[i] = result[i] + a[i,j]*b[j]
    return result

matrix_vector_multiplication(a,b)
6/54:
num_rows = U.shape[0]
num_cols = V.shape[1]

result = np.zeros((num_rows,num_cols))

def matrix_matrix_multiplication(a,b):

    assert U.shape[1] = V.shape[0]

    for i in range(num_cols): 
        vi = V[:,1]
        Uvi = matrix_vector_multiplication(U,vi)
        result[:,i] = Uvi
    return result
6/55:
num_rows = U.shape[0]
num_cols = V.shape[1]

result = np.zeros((num_rows,num_cols))

def matrix_matrix_multiplication(a,b):

    assert U.shape[1] == V.shape[0]

    for i in range(num_cols): 
        vi = V[:,1]
        Uvi = matrix_vector_multiplication(U,vi)
        result[:,i] = Uvi
    return result
 9/1:
## Pandas version 
pd.__version__
 9/2:
## Pandas version 
import pandas as pd
pd.__version__
 9/3: wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
 9/4: !wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
 9/5:
!wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
df = pd.read_csv('car_fuel_efficiency_2026.csv')
df.head()
 9/6: df.summary()
 9/7: df.describe()
 9/8: df.fuel_type.describe()
 9/9: df.fuel_efficiency_mpg.max()
9/10: df.horsepower.median()
9/11: df.isnull.sum()
9/12: df.isnull().sum()
9/13:
a = df.horsepower.median()
print(a)
9/14:
a = df.horsepower.median()
b = df.horsepower.mode()
print(a)
9/15:
a = df.horsepower.median()
b = df.horsepower.mode()
print(b)
9/16: b = df.horsepower.mode()
9/17:
b = df.horsepower.mode()
print(b)
10/1:
## Median value of horsepower 
a = df.horsepower.median()
print(a)
10/2:
## Pandas version 
import pandas as pd
pd.__version__
10/3:
!wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
df = pd.read_csv('car_fuel_efficiency_2026.csv')
df.head()
10/4: df.describe()
10/5: df.fuel_type.describe()
10/6: df.fuel_efficiency_mpg.max()
10/7:
## Median value of horsepower 
a = df.horsepower.median()
print(a)
10/8:
b = df.horsepower.mode()
print(b)
10/9: df.isnull().sum()
10/10:
b = df.horsepower.mode()[0]
print(b)
10/11:
## Median value of horsepower 
a = df.horsepower.median()
print(a)
b = df.horsepower.mode()[0]
print(b)
10/12:
## Median value of horsepower 
a = df.horsepower.median()
print(a)
b = df.horsepower.mode()
print(b)
10/13:
## Median value of horsepower 
a = df.horsepower.median()
print(a)
b = df.horsepower.mode()[0]
print(b)
10/14:
## Median value of horsepower 
df_hp = df['horsepower']
a = df_hp.horsepower.median()
print(a)
b = df_hp.horsepower.mode()[0]
print(b)
10/15:
## Median value of horsepower 
df_hp = df['horsepower']
a = df_hp.median()
print(a)
b = df_hp.mode()[0]
print(b)
10/16: df_hp.head()
10/17:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.median()
print(a)

b = df_hp.mode()[0]
print(b)
10/18:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)

b = df_hp.horsepower.mode()[0]
print(b)
10/19: df_hp.head()
10/20:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
df.horsepower.isnull()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/21:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
df.horsepower.describe()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/22:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
df.horsepower.isnull().count()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/23:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
df.horsepower.isnull().sum()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/24:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
df.horsepower.isnull().sum()
df.horsepower.fillna()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/25:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
b = df_hp.horsepower.mode()[0]
print(b)


df.horsepower.isnull().sum()
#df.horsepower.fillna()
#b = df_hp.horsepower.mode()[0]
#print(b)
10/26:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
b = df_hp.horsepower.mode()[0]
print(b)
df.horsepower.isnull().sum()
df.horsepower.fillna(b)
10/27:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
b = df_hp.horsepower.mode()[0]
print(b)
df.horsepower.isnull().sum()
df.horsepower.fillna(b)
c = df_hp.horsepower.mode()[0]
10/28:
## Median value of horsepower 
df_hp['horsepower'] = df['horsepower']
a = df_hp.horsepower.median()
print(a)
b = df_hp.horsepower.mode()[0]
print(b)
df.horsepower.isnull().sum()
df.horsepower.fillna(b)
c = df_hp.horsepower.mode()[0]
print(c)
10/29:
## 7. Sum of weights 
df_asia = df['origin'='Asia']
10/30:
## 7. Sum of weights 
df_asia = df['origin'=='Asia']
10/31:
## 7. Sum of weights 
df_asia = df[df['origin']'=='Asia']
10/32:
## 7. Sum of weights 
df_asia = df[df['origin'] =='Asia']
10/33:
## 7. Sum of weights 
df_asia = df[df['origin'] =='Asia']
df_asia
10/34:
## 7. Sum of weights 
df_asia = df[(df['origin'] =='Asia')]
df_asia
10/35:
## 7. Sum of weights 
df_asia = df[(df['origin'] =='Asia'),df['vehicle_weight']]
df_asia
10/36:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia','vehicle_weight','model_year']
df_asia
10/37:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia', 'vehicle_weight', 'model_year']

df_asia
10/38:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia', []'vehicle_weight', 'model_year']]

df_asia
10/39:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia', []'vehicle_weight', 'model_year']

df_asia
10/40:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia', 'vehicle_weight', 'model_year']

df_asia
10/41:
## 7. Sum of weights 
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]

df_asia
10/42:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
df_asia.head(7)
10/43:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7)
10/44:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7)
x
10/45:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x
10/46:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.transpose()
10/47:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.t
10/48:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]

df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.np.T
10/49:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.
10/50:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
10/51:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.T
10/52:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.np.T
10/53:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy
x_t = x.T
10/54:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
10/55:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
10/56:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t
10/57:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t
XTX
10/58:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
10/59:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/60:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

XTX.inv()
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/61:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

XTX.linalg.inv()
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/62:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/63:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x @ x_t

XTX_inv = np.linalg.inv('XTX')
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/64:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/65:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
XTX_inv * XTX
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/66:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
z = XTX_inv * XTX
z
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
y
10/67:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

w = XTX_inv * x_t * y
10/68:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
10/69:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape()
10/70:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
10/71:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
XTX.shape
XTX_inv.shape
10/72:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

#x_t.shape
XTX.shape
#XTX_inv.shape
10/73:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
XTX.shape
#XTX_inv.shape
10/74:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape
10/75:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv * x_t * y
10/76:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
10/77:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w
10/78:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w[0].sum()
10/79:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w[0,:].sum()
10/80:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w
10/81:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w[0,1]
10/82:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w[:]
10/83:
## 7. Sum of weights 
# iloc = INTEGER location (select by position, like a list) Syntax for both:  df.iloc[ROWS, COLUMNS]
import numpy as np
df_asia = df.loc[df['origin'] =='Asia',['vehicle_weight', 'model_year']]
x = df_asia.head(7).to_numpy()
x_t = x.T
XTX = x_t @ x

XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

x_t.shape
#XTX.shape
#XTX_inv.shape

w = XTX_inv @ x_t @ y
w[:].sum()
14/1:
import pandas as pd
from pathlib import Path
14/2:
import pandas as pd
import numpy as np
from pathlib import Path
14/3: data = https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/data.csv
14/4: data = 'https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/data.csv'
14/5:
data = 'https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/data.csv'
!wget $data
14/6: df = pd.read_csv(data)
14/7: df = pd.read_csv('data.csv')
14/8:
data = 'https://github.com/alexeygrigorev/mlbookcamp-code/blob/ab910c68fbd1d6185e0a4cce8cb7a58bb37ade0c/chapter-02-car-price/data.csv'
!wget $data
14/9: df = pd.read_csv('data.csv')
14/10: pd.read_csv('data.csv')
14/11:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
14/12: pd.read_csv('data.csv')
14/13:
df = pd.read_csv('data.csv')
df
14/14:
df = pd.read_csv('data.csv')
df.head()
14/15:
## Cleanup & Data Preparation

df.columns
14/16:
## Cleanup & Data Preparation

df.columns.str
14/17:
## Cleanup & Data Preparation

df.columns.str.lower()
14/18:
## Cleanup & Data Preparation

df.columns.str.lower().replace(' ','_')
14/19:
## Cleanup & Data Preparation

df.columns.str.lower().str.replace(' ','_')
14/20:
## Cleanup & Data Preparation

df.columns.str.lower().str.replace(' ','_')
df.head()
14/21:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
14/22: df.dtypes
14/23: df.dtypes == 'str'
14/24: df.dtypes[df.dtypes == 'str']
14/25: df.dtypes[df.dtypes == 'str'].index
14/26: list(df.dtypes[df.dtypes == 'str'].index)
14/27: strings = list(df.dtypes[df.dtypes == 'str'].index)
14/28:
strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
14/29: df.head()
15/1:
for col in df.columns: 
    print(col)
15/2:
for col in df.columns(): 
    print(col)
15/3:
import pandas as pd
import numpy as np
from pathlib import Path
15/4:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
15/5:
df = pd.read_csv('data.csv')
df.head()
15/6:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
15/7:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
15/8: df.head()
15/9:
for col in df.columns(): 
    print(col)
15/10:
for col in df.columns: 
    print(col)
15/11:
for col in df.columns: 
    print(col)
    print(df[col].head)
15/12:
for col in df.columns: 
    print(col)
    print(df[col].head())
15/13:
for col in df.columns: 
    print(col)
    print(df[col].head())
    print()
15/14:
for col in df.columns: 
    print(col)
    print(df[col].unique())
    print()
15/15:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print()
15/16:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
15/17:
import matplotlib.pyplot as plt
import seaborn as sns
15/18:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib as inline
15/19:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
15/20: sns.histplot(df.msrp)
15/21: sns.histplot(df.msrp,bins=50)
15/22: sns.histplot(df.msrp,bins=20)
15/23: sns.histplot(df.msrp,bins=10)
15/24: sns.histplot(df.msrp[df.msrp < 100,000],bins=10)
15/25: sns.histplot(df.msrp[df.msrp < 100000],bins=10)
15/26: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
15/27:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = df.msrp
15/28:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = df.msrp
prices
15/29:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = np.log(df.msrp)
prices
15/30:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = np.logp(df.msrp)
prices
15/31:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = np.log1p(df.msrp)
prices
15/32:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

prices = np.log1p(df.msrp)
prices
sns.histplot(prices)
15/33:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
15/34: df.isnull
15/35: df.isnull()
15/36: df.isnull().sum()
17/1:
import pandas as pd
import numpy as np
from pathlib import Path
17/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
17/3:
df = pd.read_csv('data.csv')
df.head()
17/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
17/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
17/6: df.head()
17/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
17/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
17/9: sns.histplot(df.msrp,bins=10)
17/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
17/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
17/12:
## identify missing values in each column
df.isnull().sum()
17/13: len(df)
17/14: len(df)*0.2
17/15: int(len(df)*0.2)
17/16:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = int(len(df)*0.2)
17/17:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val
17/18:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val, n_train, n_test
17/19:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
17/20: df.iloc[[1:4]]
17/21: df.iloc[1:4]
17/22: df[train] = df.iloc[1:4]
17/23: df['train'] = df.iloc[1:4]
17/24: train = df.iloc[1:4]
17/25:
train = df.iloc[1:4]
train
17/26:
df_train = df.iloc[:n_val]
df_val = df.iloc[n_val:n_test]
df_test = df.iloc[n_test:]
17/27:
##df_train = df.iloc[:n_val]
##df_val = df.iloc[n_val:n_test]
##df_test = df.iloc[n_test:]

df.iloc[:n_val]
17/28:
##df_train = df.iloc[:n_val]
##df_val = df.iloc[n_val:n_test]
##df_test = df.iloc[n_test:]

df.iloc[:n_test]
17/29: n_val, n_test, n_train
17/30:
df_val = df.iloc[:n_val]
##df_val = df.iloc[n_val:n_test]
##df_test = df.iloc[n_test:]

df.iloc[:n_test]
17/31:
df_val = df.iloc[:n_val]
##df_test = df.iloc[n_val:n_test]
##df_test = df.iloc[n_test:]

df.iloc[:n_test]
17/32:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:n_test]
df_train = df.iloc[n - n_val - n_test:]

df.iloc[:n_test]
17/33:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:n_test]
df_train = df.iloc[(n - n_val - n_test):]

df.iloc[:n_test]
17/34:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:n_test]
df_train = df.iloc[(n - n_val - n_test):]

df_test.len()
17/35:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:n_test]
df_train = df.iloc[(n - n_val - n_test):]

df_test.len
17/36:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:n_test]
df_train = df.iloc[(n - n_val - n_test):]

len(df_test)
17/37:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:(n_test + n_val)]
df_train = df.iloc[(n - n_val - n_test):]

len(df_test)
17/38:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:(n_test + n_val)]
df_train = df.iloc[(n - n_val - n_test):]

len(df_train)
17/39:
df_val = df.iloc[:n_val]
df_test = df.iloc[n_val:(n_test + n_val)]
##df_train = df.iloc[(n - n_val - n_test):]
df_train = df.iloc[(n_test + n_val):]

len(df_train)
17/40:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[n_train:]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
17/41:
##Shuffling the rows of the data frame

np.arange(n)
17/42:
##Shuffling the rows of the data frame

np.arange(n).shuffle()
17/43:
##Shuffling the rows of the data frame

np.arange(n).shuffle
17/44:
##Shuffling the rows of the data frame

idx = np.arange(n)
17/45:
##Shuffling the rows of the data frame

idx = np.arange(n)
idx
17/46:
##Shuffling the rows of the data frame

idx = np.arange(n)
idx()
17/47:
##Shuffling the rows of the data frame

idx = np.arange(n)
idx
17/48:
##Shuffling the rows of the data frame

idx = np.arange(n)
idx.shuffle
17/49:
##Shuffling the rows of the data frame

idx = np.arange(n)
idx.shuffle()
17/50:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
17/51:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx
17/52:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train]:]
17/53:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train]:]
df_train
17/54:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
df_train
17/55:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]
17/56:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_val
17/57:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_val
df_test
17/58:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_train+ df_val + df_test
17/59:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_train
df_val 
df_test
17/60:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_train
17/61: df_train
17/62: df_test
17/63: df_val
17/64:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[n_train:]]
##df_train = df.iloc[idx[n_train]:] is incorrect, why tho?
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_train
17/65: df_test
17/66: df_val
17/67:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
17/68:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

df_train
17/69: df_test
17/70:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
18/1:
import pandas as pd
import numpy as np
from pathlib import Path
18/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
18/3:
df = pd.read_csv('data.csv')
df.head()
18/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
18/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
18/6: df.head()
18/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
18/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
18/9: sns.histplot(df.msrp,bins=10)
18/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
18/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
18/12:
## identify missing values in each column
df.isnull().sum()
18/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
18/14: n_val, n_test, n_train
18/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
18/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2)
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
18/17: df_train.head()
18/18: df_train.reset_index()
18/19: df_train.reset_index(drop=True)
18/20: df_train = df_train.reset_index(drop=True)
18/21:
df_train = df_train.reset_index(drop=True)
df_train
18/22:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_train
18/23:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_val
18/24:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
18/25: df_train.msrp
18/26: df_train.msrp.values()
18/27: df_train.msrp.values
18/28: np.log1p(df_train.msrp.values)
18/29: y_train = np.log1p(df_train.msrp.values)
18/30:
y_train = np.log1p(df_train.msrp.values)
y_train
18/31:
y_train = np.log1p(df_train.msrp)
y_train
18/32:
y_train = np.log1p(df_train.msrp)
y_val = np.log1p(df_val.msrp)
y_test = np.log1p(df_test.msrp)
18/33: df_train.del['msrp']
18/34: df_train.msrp.del
18/35: df_train
18/36: df_train["msrp"]
18/37: df_train["msrp"].del
18/38:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
18/39: del df_train["msrp"]
18/40:
del df_train["msrp"]
df_train
18/41:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
18/42:
#del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
18/43: df_train
19/1:
import pandas as pd
import numpy as np
from pathlib import Path
19/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
19/3:
df = pd.read_csv('data.csv')
df.head()
19/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
19/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
19/6: df.head()
19/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
19/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
19/9: sns.histplot(df.msrp,bins=10)
19/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
19/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
19/12:
## identify missing values in each column
df.isnull().sum()
19/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
19/14: n_val, n_test, n_train
19/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
19/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
19/17: df_train.head()
19/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
19/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
19/20:
#del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
19/21: df_train
19/22: df.train
19/23: df_train
19/24: df_train.iloc[10]
19/25:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
19/26:
def linear_regression(xi): 
    n = len(xi)

    for i in n: 
        prob = prob + w * xi

        return prob
19/27: linear_regression(xI)
19/28: linear_regression(xi)
19/29:
def linear_regression(xi): 
    n = len(xi)

    for i in range(n): 
        prob = prob + w * xi

        return prob
19/30: linear_regression(xi)
19/31:
def linear_regression(xi): 
    n = len(xi)

    for j in range(n): 
        prob = prob + w[j] * xi[j]

        return prob
19/32: linear_regression(xi)
19/33:
def linear_regression(xi): 
    n = len(xi)

    pred = w0
    for j in range(n): 
        pred = pred + w[j] * xi[j]

        return prob
19/34: linear_regression(xi)
19/35:
def linear_regression(xi): 
    n = len(xi)

    pred = w0
    for j in range(n): 
        pred = pred + w[j] * xi[j]

        return pred
19/36: linear_regression(xi)
19/37:
def linear_regression(xi): 
    n = len(xi)

    pred = w0
    for j in range(n): 
        pred = pred + w[j] * xi[j]

    return pred
19/38: linear_regression(xi)
20/1:
import pandas as pd
import numpy as np
from pathlib import Path
20/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
20/3:
df = pd.read_csv('data.csv')
df.head()
20/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
20/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
20/6: df.head()
20/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
20/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
20/9: sns.histplot(df.msrp,bins=10)
20/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
20/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
20/12:
## identify missing values in each column
df.isnull().sum()
20/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
20/14: n_val, n_test, n_train
20/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
20/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
20/17: df_train.head()
20/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
20/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
20/20:
#del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
20/21: df_train
20/22:
## looking at a specific row
df_train.iloc[10]
20/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
20/24:
## defining the linear regress
def linear_regression(xi): 
    n = len(xi)

    pred = w0
    for j in range(n): 
        pred = pred + w[j] * xi[j]

    return pred
20/25: linear_regression(xi)
20/26:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
20/27:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

n = len(xi)
result = 0

def dot_product (xi,w): 
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result
20/28:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + result
20/29:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + dot_product(xi,w)
20/30:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + dot_product(xi,w)

dot_product (xi,w)
20/31:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + dot_product(xi,w)

dot_product (xi,w)
lin_reg (xi,w)
20/32:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi,w)
20/33: w_new = w0 + w
20/34:
w
#w_new = w0 + w
20/35:
w0
#w_new = w0 + w
20/36:
w
#w_new = w0 + w
20/37:
[w0]
#w_new = w0 + w
20/38:
[w0]
w_new = [w0] + w
20/39:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)



def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi,w): 
    return w0 + dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi,w)
20/40:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)



def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi,w): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi,w)
20/41:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)



def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi,w): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi,w_new)
20/42:
## Linear Regression in a vector form

# g(xi) = w0 + x1 * w1 + x2 * w2 + ..... + xn * wn (Dot Product of two vectors)



def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
20/43:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
20/44:
[w0]
w_new = [w0] + w
20/45:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

[x1, x2, x3, x10]
20/46:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

[x1, x2, x3, x10]
np.array([x1, x2, x3, x10])
20/47:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = [x1, x2, x3, x10]
np.array(Xn)
20/48:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = [x1, x2, x3, x10]
np.array(Xn)

w_new = [w0] + w
20/49:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = [x1, x2, x3, x10]
np.array(Xn)

w_new = [w0] + w

dot_product(Xn,w_new)
20/50:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = [x1, x2, x3, x10]
np.array(Xn)

w_new = [w0] + w

w_new
20/51:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = [x1, x2, x3, x10]
np.array(Xn)

w_new = [w0] + w

Xn @ w_new
20/52:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


Xn @ w_new
20/53:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
21/1:
import pandas as pd
import numpy as np
from pathlib import Path
21/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
21/3:
df = pd.read_csv('data.csv')
df.head()
21/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
21/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
21/6: df.head()
21/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
21/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
21/9: sns.histplot(df.msrp,bins=10)
21/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
21/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
21/12:
## identify missing values in each column
df.isnull().sum()
21/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
21/14: n_val, n_test, n_train
21/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
21/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
21/17: df_train.head()
21/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
21/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
21/20:
#del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
21/21: df_train
21/22:
## looking at a specific row
df_train.iloc[10]
21/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
21/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
21/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
21/26:
[w0]
w_new = [w0] + w
21/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
21/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
21/29: X
21/30: Xn
21/31:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X
21/32:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

y
21/33:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

y.len()
21/34:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

y.count()
21/35:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

len(y)
21/36:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

len(X)
21/37:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

len(X+1)
21/38:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
21/39:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

len(X)
21/40:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
21/41:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_T
21/42:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

w = (X_T * X)^(-1)
21/43:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

w = (X_T * y) / (X_T * X)
21/44:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

w = (X_T * y) / (X_T * X)
21/45:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

np.ones(1)
21/46:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

np.ones(len(X))
21/47:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)

X + np.ones(len(X))
21/48:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
np.linalg.inv(X_T*X)
21/49:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
np.linalg.inv(X_T @ X)
21/50:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
(np.linalg.inv(X_T @ X)) * (X_T @ y)
21/51:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
(np.linalg.inv(X_T @ X)) * (X_T @ y)
21/52:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
w = (np.linalg.inv(X_T @ X)) * (X_T @ y)
21/53:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

w
21/54:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

len(w)
21/55:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

w
21/56: X_T @ X
21/57: X @ X_T
21/58: X_T.dot(X)
21/59:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X

#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/60:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/61:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

X_TX_INV @ X_TX
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/62:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

X_TX @ X_TX_INV
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/63:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

X_TX.dot(X_TX_INV)
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/64:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

X_TX.dot(X_TX_INV).round()
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/65:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
X_TX @ X_TX_INV
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/66:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
X_TX @ X_TX_INV.round()
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/67:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
#w = (np.linalg.inv(X_T @ X)) * (X_T @ y)

#w
21/68:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w = X_TX_INV.dot(X_T).dot(y)

#w
21/69:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w = X_TX_INV.dot(X_T).dot(y)
w

#w
21/70:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w = X_TX_INV.dot(X_T).dot(y)
w
21/71:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

np.ones(len(X))

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w = X_TX_INV.dot(X_T).dot(y)
w
21/72: np.ones(X.shape[0])
21/73:
#np.ones(X.shape[0])
np.ones(len(X))
21/74:
#np.ones(X.shape[0])
ones = np.ones(len(X))
np.column_stack(ones,X)
21/75:
#np.ones(X.shape[0])
ones = np.ones(len(X))
np.column_stack([ones,X])
21/76:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

ones = np.ones(X.shape[0])
X = np.column_stack([ones,X])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w = X_TX_INV.dot(X_T).dot(y)
w
21/77:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

ones = np.ones(X.shape[0])
X = np.column_stack([ones,X])

X_T = np.linalg.matrix_transpose(X)
X_TX = X_T @ X
X_TX_INV = np.linalg.inv(X_TX)

#X_TX.dot(X_TX_INV).round()
(X_TX @ X_TX_INV).round()
w_full = X_TX_INV.dot(X_T).dot(y)
w
21/78:
w_0 = w_full[0:1]
w = w_full[1:]
21/79:
w_0 = w_full[0:1]
w = w_full[1:]

w_0, w
21/80:
w_0 = w_full[0]
w = w_full[1:]

w_0, w
21/81:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

def train_linear_regression(Xn,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full
21/82:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full
21/83:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full

train_linear_regression(X,y)
21/84:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])

def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
22/1:
import pandas as pd
import numpy as np
from pathlib import Path
22/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
22/3:
df = pd.read_csv('data.csv')
df.head()
22/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
22/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
22/6: df.head()
22/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
22/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
22/9: sns.histplot(df.msrp,bins=10)
22/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
22/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
22/12:
## identify missing values in each column
df.isnull().sum()
22/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
22/14: n_val, n_test, n_train
22/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
22/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
22/17: df_train.head()
22/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
22/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
22/20:
#del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
22/21: df_train
22/22:
## looking at a specific row
df_train.iloc[10]
22/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
22/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
22/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
22/26:
[w0]
w_new = [w0] + w
22/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
22/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
22/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
22/30:
w_0 = w_full[0] #bias term
w = w_full[1:] #weights

w_0, w
22/31:
w_0 = w_full[0] #bias term
w = w_full[1:] #weights

w_0, w
22/32: y_train
22/33: X_train
22/34: x_train
22/35: df_train
22/36: df_train.columns
22/37: df_train.columns()
22/38: df_train.columns
22/39: df_train.columns.dtype
22/40: df_train.columns.dtype()
22/41: df_train.dtype()
22/42: df_train.dtype
22/43: df_train.columns.dtype
22/44: dtype(df_train.columns)
22/45: df_train
22/46: df_train.columns
22/47: df_train.columns(dtype)
22/48: df_train.columns.dtype
22/49: df_train.dtypes
22/50:
import pandas as pd
import numpy as np
from pathlib import Path
22/51:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
22/52:
df = pd.read_csv('data.csv')
df.head()
22/53:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
22/54:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
22/55: df.head()
22/56:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
22/57:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
22/58: sns.histplot(df.msrp,bins=10)
22/59: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
22/60:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
22/61:
## identify missing values in each column
df.isnull().sum()
22/62:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
22/63: n_val, n_test, n_train
22/64:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
22/65:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
22/66: df_train.head()
22/67:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
22/68:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
22/69:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
22/70: df_train
22/71:
## looking at a specific row
df_train.iloc[10]
22/72:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
22/73:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
22/74:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
22/75:
[w0]
w_new = [w0] + w
22/76:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
22/77:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
22/78:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
22/79:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
22/80: y_train
22/81:
df_train.dtypes
['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
22/82:
df_train.dtypes
#['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
22/83:
df_train.dtypes
['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
df_train.shape
22/84:
df_train.dtypes
#['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
22/85:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
22/86:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
df_train[base]
22/87:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
22/88:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
22/89:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull
22/90:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull.sum()
22/91:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull.sum
22/92:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum
22/93:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
22/94:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train.fillna(0)
22/95:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train.fillna(0)
X_train.isnull().sum()
22/96:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
22/97: train_linear_regression(X_train,y_train)
22/98:
result = train_linear_regression(X_train,y_train)


w0 = result[0]
weights = result[1:]
w0, weights
22/99: X_train.dot(weights)
22/100: w0,weights = train_linear_regression(X_train,y_train)
22/101: X_train.dot(weights)
22/102: w0 + X_train.dot(weights)
22/103: pred = w0 + X_train.dot(weights)
22/104: sns.histplot(pred,y_train)
22/105:
sns.histplot(pred, color = "red")
sns.histplot(y_train, color = "blue")
22/106:
sns.histplot(pred, color = "red", bin = 50)
sns.histplot(y_train, color = "blue", bin = 50)
22/107:
sns.histplot(pred, color = "red", bins = 50)
sns.histplot(y_train, color = "blue", bins = 50)
22/108:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
22/109:
##def RMSE(Y,Y_train): 
sq_error = (Y - Y_train)^2
22/110:
##def RMSE(Y,Y_train): 
sq_error = (pred - Y_train)^2
22/111:
##def RMSE(Y,Y_train): 
sq_error = (pred - y_train)^2
22/112:
##def RMSE(Y,Y_train): 
pred-y_train
22/113:
##def RMSE(Y,Y_train): 
(pred-y_train)^2
22/114:
##def RMSE(Y,Y_train): 
(pred-y_train) ** 2
22/115:
##def RMSE(Y,Y_train): 
error_sq = (pred-y_train) ** 2
mean_error_sq = error_sq.mean()
22/116:
##def RMSE(Y,Y_train): 
error_sq = (pred-y_train) ** 2
mean_error_sq = error_sq.mean()
mean_error_sq
22/117:
##def RMSE(Y,Y_train): 
error_sq = (pred-y_train) ** 2
mean_error_sq = error_sq.mean()
np.sqrt(mean_error_sq)
22/118:
def RMSE(pred,y_train): 
    error_sq = (pred-y_train) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
22/119:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
23/1:
import pandas as pd
import numpy as np
from pathlib import Path
23/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
23/3:
df = pd.read_csv('data.csv')
df.head()
23/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
23/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
23/6: df.head()
23/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
23/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
23/9: sns.histplot(df.msrp,bins=10)
23/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
23/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
23/12:
## identify missing values in each column
df.isnull().sum()
23/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
23/14: n_val, n_test, n_train
23/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
23/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
23/17: df_train.head()
23/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
23/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
23/20:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
23/21: df_train
23/22:
## looking at a specific row
df_train.iloc[10]
23/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
23/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
23/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
23/26:
[w0]
w_new = [w0] + w
23/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
23/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
23/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
23/30:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
23/31: y_train
23/32:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
23/33: w0,weights = train_linear_regression(X_train,y_train)
23/34: pred = w0 + X_train.dot(weights)
23/35:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
23/36:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
23/37:
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    return df_prep
23/38:
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    X = df_prep.values()
    return X
23/39:
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    X = df_prep.values()
    return X

data_prep(df_val)
23/40:
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
23/41:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
23/42:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(y_train)
23/43:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)
23/44:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)
X_train_pred
23/45:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
23/46:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(X_val,y_val)
23/47:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
24/1:
import pandas as pd
import numpy as np
from pathlib import Path
24/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
24/3:
df = pd.read_csv('data.csv')
df.head()
24/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
24/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
24/6: df.head()
24/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
24/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
24/9: sns.histplot(df.msrp,bins=10)
24/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
24/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
24/12:
## identify missing values in each column
df.isnull().sum()
24/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
24/14: n_val, n_test, n_train
24/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
24/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
24/17: df_train.head()
24/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
24/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
24/20:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
24/21: df_train
24/22:
## looking at a specific row
df_train.iloc[10]
24/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
24/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
24/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
24/26:
[w0]
w_new = [w0] + w
24/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
24/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
24/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
24/30:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
24/31: y_train
24/32:
df_train.dtypes
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
24/33: w0,weights = train_linear_regression(X_train,y_train)
24/34: pred = w0 + X_train.dot(weights)
24/35:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
24/36:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
24/37:
base = ['year','engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/38:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
24/39:
df_train.dtypes
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
24/40:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df_prep = df[base]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/41: df_train
24/42: df_train.year
24/43: df_train.year.min()
24/44: df_train.year.max()
24/45:
df_train.year.max()
age = df_train.year.max() - df_train.year
24/46:
df_train.year.max()
age = df_train.year.max() - df_train.year
age
24/47:
df_train.year.max()
age = df_train.year.max() - df_train.year
age
age.list
24/48:
df_train.year.max()
age = df_train.year.max() - df_train.year
age
age.list()
24/49:
df_train.year.max()
age = df_train.year.max() - df_train.year
age
np.array[age]
24/50:
df_train.year.max()
age = df_train.year.max() - df_train.year
age
24/51:
df_train.year.max()
age = df_train.year.max() - df_train.year
[age]
24/52:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    age = df.year.max() - df.year
    df_prep = df[base,[age]]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/53:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df = df.copy()
    max_year = df.year.max()
    df['age'] = max_year - df.year
    df_prep = df[base,'age']
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/54:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df = df.copy()
    max_year = df.year.max()
    df['age'] = max_year - df.year
    df_prep = df[base,df['age']]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/55:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df = df.copy()
    max_year = df.year.max()
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/56:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']

def data_prep(df): 
    df = df.copy()
    max_year = df.year.max()
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/57:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
24/58:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
24/59:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
26/1:
import pandas as pd
import numpy as np
from pathlib import Path
26/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
26/3:
df = pd.read_csv('data.csv')
df.head()
26/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
26/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
26/6: df.head()
26/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
26/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
26/9: sns.histplot(df.msrp,bins=10)
26/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
26/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
26/12:
## identify missing values in each column
df.isnull().sum()
26/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
26/14: n_val, n_test, n_train
26/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
26/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
26/17: df_train.head()
26/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
26/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
26/20:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
26/21: df_train
26/22:
## looking at a specific row
df_train.iloc[10]
26/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
26/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
26/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
26/26:
[w0]
w_new = [w0] + w
26/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
26/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
26/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
26/30:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
26/31: y_train
26/32:
df_train.dtypes

base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
26/33: w0,weights = train_linear_regression(X_train,y_train)
26/34: pred = w0 + X_train.dot(weights)
26/35:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
26/36:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
26/37:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
26/38:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
26/39:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
26/40: df_train
26/41: df_train.columns()
26/42: df_train.columns
26/43: df_train.dtypes()
26/44: df_train.dtypes
26/45: df_train.number_of_doors
26/46: df_train.number_of_doors == 2
26/47: (df_train.number_of_doors == 2).astype(int)
26/48: (df_train.number_of_doors == 2).astype('int')
26/49: df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
26/50:
df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')
26/51:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train
26/52:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train.del('num_doors_2')
26/53:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train.delete('num_doors_2')
26/54:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train.del[('num_doors_2')]
26/55:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train = df_train.drop(columns='num_doors_2')
26/56:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train = df_train.drop(columns='num_doors_2')
26/57:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train = df_train.drop(columns='num_doors_3')
26/58:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

df_train = df_train.drop(columns='num_doors_4')
26/59:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

#df_train = df_train.drop(columns='num_doors_4')
df_train
26/60: df_train['number_of_doors']
26/61: df_train['number_of_doors'].count
26/62: df_train['number_of_doors'].count()
26/63: df_train['number_of_doors'].types()
26/64: df_train['number_of_doors'].type()
26/65: df_train['number_of_doors'].count()
26/66: df_train['number_of_doors'].count
26/67:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
26/68:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features = features.append(features)
26/69:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features.append(features)
26/70:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features.append(feature)
26/71:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features.append(feature)
26/72:
import pandas as pd
import numpy as np
from pathlib import Path
26/73:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
26/74:
df = pd.read_csv('data.csv')
df.head()
26/75:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
26/76:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
26/77: df.head()
26/78:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
26/79:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
26/80: sns.histplot(df.msrp,bins=10)
26/81: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
26/82:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
26/83:
## identify missing values in each column
df.isnull().sum()
26/84:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
26/85: n_val, n_test, n_train
26/86:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
26/87:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
26/88: df_train.head()
26/89:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
26/90:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
26/91:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
26/92: df_train
26/93:
## looking at a specific row
df_train.iloc[10]
26/94:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
26/95:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
26/96:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
26/97:
[w0]
w_new = [w0] + w
26/98:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
26/99:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
26/100:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
26/101:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
26/102: y_train
26/103:
df_train.dtypes

base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
26/104: w0,weights = train_linear_regression(X_train,y_train)
26/105: pred = w0 + X_train.dot(weights)
26/106:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
26/107:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
26/108:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
26/109:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
26/110:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
26/111: df_train.dtypes
26/112:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

#df_train = df_train.drop(columns='num_doors_4')
df_train
26/113:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features.append(feature)
26/114:
num_doors = [2, 3, 4]

for v in num_doors: 
    num_doors = num_doors.copy()
    features = "num_doors_%s" % v
    df[features] = (df_train.number_of_doors == v).astype('int')
    features.append(feature)
26/115:
num_doors = [2, 3, 4]

for v in [2, 3, 4]:
        feature = 'num_doors_%s' % v
        df[feature] = (df['number_of_doors'] == v).astype(int)
        features.append(feature)
26/116:
num_doors = [2, 3, 4]

for v in [2, 3, 4]:
        feature = 'num_doors_%s' % v
        df[feature] = (df['number_of_doors'] == v).astype(int)
        features.append(feature)
26/117:
import pandas as pd
import numpy as np
from pathlib import Path
26/118:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
26/119:
df = pd.read_csv('data.csv')
df.head()
26/120:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
26/121:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
26/122: df.head()
26/123:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
26/124:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
26/125: sns.histplot(df.msrp,bins=10)
26/126: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
26/127:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
26/128:
## identify missing values in each column
df.isnull().sum()
26/129:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
26/130: n_val, n_test, n_train
26/131:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
26/132:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
26/133: df_train.head()
26/134:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
26/135:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
26/136:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
26/137: df_train
26/138:
## looking at a specific row
df_train.iloc[10]
26/139:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
26/140:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
26/141:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
26/142:
[w0]
w_new = [w0] + w
26/143:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
26/144:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
26/145:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
26/146:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
26/147: y_train
26/148:
df_train.dtypes

base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
26/149: w0,weights = train_linear_regression(X_train,y_train)
26/150: pred = w0 + X_train.dot(weights)
26/151:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
26/152:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
26/153:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
26/154:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
26/155:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
26/156: df_train.dtypes
26/157:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

#df_train = df_train.drop(columns='num_doors_4')
df_train
27/1:
import pandas as pd
import numpy as np
from pathlib import Path
27/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
27/3:
df = pd.read_csv('data.csv')
df.head()
27/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
27/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
27/6: df.head()
27/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
27/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
27/9: sns.histplot(df.msrp,bins=10)
27/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
27/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
27/12:
## identify missing values in each column
df.isnull().sum()
27/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
27/14: n_val, n_test, n_train
27/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
27/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
27/17: df_train.head()
27/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
27/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
27/20:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
27/21: df_train
27/22:
## looking at a specific row
df_train.iloc[10]
27/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
27/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
27/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
27/26:
[w0]
w_new = [w0] + w
27/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
27/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
27/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
27/30:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
27/31: y_train
27/32:
df_train.dtypes

base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
27/33: w0,weights = train_linear_regression(X_train,y_train)
27/34: pred = w0 + X_train.dot(weights)
27/35:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
27/36:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
27/37:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
27/38:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
27/39:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
27/40: df_train.dtypes
27/41:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

#df_train = df_train.drop(columns='num_doors_4')
df_train
27/42: df_train["number_"]
27/43: df_train["number_of_doors"]
27/44: df_train["number_of_doors"].value_counts
27/45: df_train["number_of_doors"].value_counts()
27/46: df_train["number_of_doors"].value_counts(dropna=FALSE)
27/47: df_train["number_of_doors"].value_counts(dropna=False)
27/48: df_train["number_of_doors"] == 2
27/49: (df_train["number_of_doors"] == 2).head()
27/50: (df_train["number_of_doors"] == 2).head(10)
27/51: (df_train["number_of_doors"]).head(10)
27/52: (df_train["number_of_doors"] == 2).sum()
27/53: door_values = [2,3,4]
27/54:
door_values = [2,3,4]

for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
27/55:
door_values = [2,3,4]

for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
return df[features].fillna(0).values
27/56: base
27/57:
door_values = [2,3,4]

features = base.copy()
for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
return df[features].fillna(0).values
27/58:
door_values = [2,3,4]

features = base.copy()
for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
    return df[features].fillna(0).values
27/59:
door_values = [2,3,4]

features = base.copy()
for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
    return df[features].fillna(0).values
27/60:
door_values = [2,3,4]

features = base.copy()
for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
return df[features].fillna(0).values
27/61:
door_values = [2,3,4]

features = base.copy()
for v in door_values: 
    feature = f"num_doors_{v}"
    df[feature] = ((df["number_of_doors"] == v).astype(int))
    features.append(feature)
df[features].fillna(0).values
27/62:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
27/63:
def prepare_X(df):
    df = df.copy()
    features = base.copy()

    df['age'] = 2017 - df.year
    features.append('age')

    for v in [2, 3, 4]:
        feature = f'num_doors_{v}'
        df[feature] = (df['number_of_doors'] == v).astype(int)
        features.append(feature)

    for col, values in categorical.items():
        for v in values:
            feature = f'{col}_{v}'
            df[feature] = (df[col] == v).astype(int)
            features.append(feature)

    return df[features].fillna(0).values
27/64:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical
27/65:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical()
27/66:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical{}
27/67:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical[]
27/68:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical
27/69: df_train
27/70: df_train['number_of_doors🚂']
27/71: df_train['number_of_doors']
27/72: df_train['number_of_doors'] == 2
27/73: (df_train['number_of_doors'] == 2).astype(int)
27/74:
num_doors = [2,3,4]
for v in num_doors:
    df[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
27/75:
num_doors = [2,3,4]
for v in num_doors:
    df[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df_train
27/76:
num_doors = [2,3,4]
for v in num_doors:
    df[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df
27/77:
num_doors = [2,3,4]
for v in num_doors:
    df[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df.drop_column('num_doors_2')
27/78:
num_doors = [2,3,4]
for v in num_doors:
    df[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df
27/79:
df = df.drop(columns='num_doors_2')
df = df.drop(columns='num_doors_3')
df = df.drop(columns='num_doors_4')
df = df.drop(columns='number_doors_2')
df = df.drop(columns='number_doors_3')
df = df.drop(columns='number_doors_4')
27/80:
num_doors = [2,3,4]
for v in num_doors:
    df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df
27/81:
num_doors = [2,3,4]
for v in num_doors:
    df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df_trian
27/82:
num_doors = [2,3,4]
for v in num_doors:
    df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df_train
27/83: df.make()
27/84: df.make
27/85: df.make.list
27/86: df.make.list()
27/87: df.make.value_counts()
27/88: df.make.value_counts().head()
27/89: df.make.value_counts().head().index
27/90: list(df.make.value_counts().head().index)
27/91: make = list(df.make.value_counts().head().index)
27/92: df
27/93: df.columns
27/94: df.columns()
27/95: df.column
27/96: df.columns.sum(0)
27/97: df.columns.sum()
27/98: df.columns.sum
27/99: df.columns.value_counts
27/100: df.columns().value_counts
27/101: df.columns().value_counts()
27/102: df.columns.value_counts()
27/103: df.columns.data_types
27/104: df.columns.data_types()
27/105: df.columns.data_type()
27/106: df.columns().data_type()
27/107: df.columns().data_types()
27/108: df.columns()
27/109: df.columns
27/110: df.columns.dtypes
27/111: df.columns.dtypes()
27/112: df.dtypes
27/113:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]
27/114:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categories = {
    for c in categories: 
      categories[c]  = list(df.make.value_counts().head().index)
}
27/115:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}
    for c in categorical_var: 
      categories[c]  = list(df.make.value_counts().head().index)
27/116:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}

for c in categorical_var: 
    categories[c]  = list(df.make.value_counts().head().index)
27/117:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}

for c in categorical_var: 
    categories[c]  = list(df.make.value_counts().head().index)

categorical_var
27/118:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}

for c in categorical_var: 
    categories[c]  = list(df.make.value_counts().head().index)

categories
27/119:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}

for c in categorical_var: 
    categorical_var[c]  = list(df.make.value_counts().head().index)

categorical_var
27/120:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categorical_var = {}

for c in categorical_var: 
    categories[c]  = list(df.make.value_counts().head().index)

categories
27/121:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categories = {}

for c in categorical_var: 
    categories[c]  = list(df.make.value_counts().head().index)

categories
27/122:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categories = {}

for c in categorical_var: 
    categories[c]  = list(df[c].value_counts().head().index)

categories
27/123:
df.dtypes
categories = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categories = {}

for c in categorical_var: 
    categories[c]  = list(df[c].value_counts().head().index)

categories
27/124:
df.dtypes
categorical_var = ['engine_cylinders', 'vehicle_style', 'engine_fuel_type', 'vehicle_style', 'make' ]

# make = list(df.make.value_counts().head().index)

categories = {}

for c in categorical_var: 
    categories[c]  = list(df[c].value_counts().head().index)

categories
27/125:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    df['age'] = max_year - df.year
    features = base + ['age']

    num_doors = [2,3,4]
    for v in num_doors:
        df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
        features.append(f"number_doors_{v}")

    for c,values in categories.items(): 
        for v in values: 
            feature = f'{col}_{v}'
            df[feature] = (df[col] == v).astype(int)
            features.append(feature)
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
27/126:
base = ['engine_hp', 'engine_cylinders', 'number_of_doors',
        'highway_mpg', 'city_mpg', 'popularity']
max_year = df_train.year.max()

def data_prep(df):
    df = df.copy()
    df['age'] = max_year - df.year
    features = base + ['age']

    for v in [2, 3, 4]:
        feature = f'number_doors_{v}'
        df[feature] = (df.number_of_doors == v).astype(int)
        features.append(feature)

    for col, values in categorical.items():
        for v in values:
            feature = f'{col}_{v}'
            df[feature] = (df[col] == v).astype(int)
            features.append(feature)

    return df[features].fillna(0).values

X_val = data_prep(df_val)
27/127:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
27/128: w0,w
27/129:
def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]
30/1:
import pandas as pd
import numpy as np
from pathlib import Path

data = wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
!curl -O $data
30/2:
import pandas as pd
import numpy as np
from pathlib import Path

data = https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv
!curl -O $data
30/3:
import pandas as pd
import numpy as np
from pathlib import Path

data = `https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv`
!curl -O $data
30/4:
import pandas as pd
import numpy as np
from pathlib import Path

data = `https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv`
!curl -O $data
30/5:
import pandas as pd
import numpy as np
from pathlib import Path

data = `https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv`
!curl -O $data
30/6:
import pandas as pd
import numpy as np
from pathlib import Path

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
30/7: data
30/8:
import pandas as pd
import numpy as np
from pathlib import Path

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('data.csv')
df.head()
30/9:
import pandas as pd
import numpy as np
from pathlib import Path

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('data.csv')
30/10: df.head()
30/11: df.columns()
30/12: df.columns
30/13: df.columns.str.lower()
30/14: df.columns.str.lower().str.replace(" ","_")
30/15: df.columns = df.columns.str.lower().str.replace(" ","_")
30/16:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.columns
30/17:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes
30/18:
df.columns = df.columns.str.lower().str.replace(" ","_")
df[df.dtypes = str]
30/19:
df.columns = df.columns.str.lower().str.replace(" ","_")
df[df.dtypes == str]
30/20:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes == str
30/21:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes = str
30/22:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes == 'str'
30/23:
df.columns = df.columns.str.lower().str.replace(" ","_")
df[df.dtypes == 'str']
30/24:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
30/25:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
list(df.dtypes[df.dtypes == 'str'])
30/26:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'])
30/27:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'])
string_cols
30/28:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
30/29:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for values in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")
30/30:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")
30/31:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")
    df.columns
30/32:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
30/33:
df_exercise = df['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']
30/34: df_exercise = df['engine_displacement', 'horsepower', 'vehicle_weight', 'model_year', 'fuel_efficiency_mpg']
30/35: df_exercise = df['number_of_doors']
30/36: df_exercise = df['number_of_doors','vehicle_size']
30/37: df.dtypes
30/38:
import pandas as pd
import numpy as np
from pathlib import Path

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('data.csv')
30/39: df.head()
30/40:
import pandas as pd
import numpy as np
from pathlib import Path

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
30/41: df.head()
30/42:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
30/43: df.dtypes
30/44:
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
30/45:
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()
30/46:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg']
30/47:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].unique
30/48:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].unique
df['fuel_efficiency_mpg'].nunique
30/49:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].unique()[:5]
df['fuel_efficiency_mpg'].nunique
30/50:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].unique()[:5]
#df['fuel_efficiency_mpg'].nunique
30/51:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].nunique()[:5]
#df['fuel_efficiency_mpg'].nunique
30/52:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df['fuel_efficiency_mpg'].unique()[:5]
#df['fuel_efficiency_mpg'].nunique
30/53:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
30/54:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=10)
30/55:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=50)
30/56:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
30/57:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
31/1:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
32/1:
import pandas as pd
import numpy as np
from pathlib import Path
32/2:
data = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
#!wget $data
!curl -O $data
32/3:
df = pd.read_csv('data.csv')
df.head()
32/4:
## Cleanup & Data Preparation

df.columns = df.columns.str.lower().str.replace(' ','_')
df.head()
32/5:
## cleaning up the values within a single column. 
## first identify the list of all column names that are string. 
## then loop through the values inside that column name to make updates 

strings = list(df.dtypes[df.dtypes == 'str'].index)
for col in strings: 
    df[col] = df[col].str.lower().str.replace(' ','_')
32/6: df.head()
32/7:
for col in df.columns: 
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()
32/8:
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
32/9: sns.histplot(df.msrp,bins=10)
31/2: df.head()
31/3:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
31/4:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.skew()
32/10: sns.histplot(df.msrp[df.msrp < 100000],bins=50)
32/11:
## applying log to all MSRP values will shrink them
## log of 0 is not defined so add +1 to each value to compute the log

price_logs = np.log1p(df.msrp)
price_logs
sns.histplot(price_logs)
32/12:
## identify missing values in each column
df.isnull().sum()
32/13:
n = int(len(df))

n_train = int(len(df)*0.6)
n_val = int(len(df)*0.2)
n_test = n - n_train - n_val

n, n_val+n_train+n_test
32/14: n_val, n_test, n_train
32/15:
# Split the dataset into validation, test, and train sets by row position.
# iloc selects by integer position (0, 1, 2, ...), not by index label.
# Slices are start-inclusive, stop-exclusive, so the three ranges below
# are contiguous and non-overlapping:
#   val   -> positions [0, n_val)
#   test  -> positions [n_val, n_val + n_test)
#   train -> positions [n_val + n_test, end)
# Note: df should be shuffled beforehand (e.g. df.sample(frac=1, random_state=42)),
# otherwise each split just takes rows in their original order.


df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]


len(df_train)
32/16:
##Shuffling the rows of the data frame

idx = np.arange(n)
np.random.seed(2) ##helps make the random shuffling consistent for this notebook
np.random.shuffle(idx)
idx

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train+n_val]]
df_test = df.iloc[idx[n_train+n_val:]]

len(df_train), len(df_val), len(df_test)
32/17: df_train.head()
32/18:
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_test
32/19:
y_train = np.log1p(df_train.msrp.values)
y_val = np.log1p(df_val.msrp.values)
y_test = np.log1p(df_test.msrp.values)
32/20:
del df_train["msrp"]
del df_val["msrp"]
del df_test["msrp"]
32/21: df_train
32/22:
## looking at a specific row
df_train.iloc[10]
32/23:
xi = [453, 11, 86]

w0 = 0
w = [1, 1, 1]
32/24:
## defining the linear regression function 

def linear_regression(xi): 

#the summation function to multiply the weights with each feature and summing them up
    n = len(xi) # finds the length of the vector containing the features

    pred = w0 # initializing the preduction with a zero value
    for j in range(n): #iterating over the whole range for the summation function 
        pred = pred + w[j] * xi[j] #for each positional term in the matrix xi (features) and w(weights), we take a sumproduct

    return pred #returns the final value with the weighted sum

linear_regression(xi)
32/25:
## Linear Regression in vector form — Approach 1: bias term kept separate
#
# g(xi) = w0 + xi1*w1 + xi2*w2 + ... + xin*wn
#       = w0 + (xi · w)          <- bias + dot product of feature and weight vectors
#
# xi : feature vector for one observation, e.g. [xi1, xi2, ..., xin]
# w  : weight vector, one weight per feature, e.g. [w1, w2, ..., wn]
# w0 : bias / intercept, handled separately from the dot product

def dot_product(xi, w):
    # Multiply matching elements and add them up: xi1*w1 + xi2*w2 + ...
    n = len(xi)          # number of features (computed from the input, so it works for any length)
    result = 0           # running total, reset on every call
    
    for j in range(n):
        result = result + w[j] * xi[j]
    return result

def lin_reg(xi, w):
    # Prediction = bias + weighted sum of features.
    # Note: w0 is not a parameter here, so it's read from the global scope.
    # Consider lin_reg(xi, w0, w) to make the dependency explicit.
    return w0 + dot_product(xi, w)

lin_reg(xi, w)
32/26:
[w0]
w_new = [w0] + w
32/27:
### Approach 2: the "bias trick"

#Instead of adding w0 separately, we treat it as the weight for a feature that is always 1:

#g(xi) = w0*1 + w1*xi1 + ... + wn*xin = [1, xi1, ..., xin] · [w0, w1, ..., wn]

#So we prepend 1 to the feature vector and w0 to the weight vector, and the whole
#prediction becomes a single dot product. This is how linear regression is usually
#written in matrix form (X · w), where X has a leading column of 1s.

def dot_product (xi,w): 
    n = len(xi)
    result = 0
    
    for j in range(n): 
        result = result + w_new[j] * xi[j]
    return result

def lin_reg(xi): 
    xi = [1] + xi
    return dot_product(xi,w)

#dot_product (xi,w)
lin_reg (xi)
32/28:
xi = [453, 11, 86]
w0 = 7.17 
w = [0.01, 0.04, 0.002]

x1 = [1, 235, 10, 26]
x2 = [1, 7879, 87, 36]
x3 = [1, 876, 34, 6]
x10 = [1, 453, 22, 86]

Xn = np.array([x1, x2, x3, x10])
w_new = np.array([w0] + w)


dot_product(Xn, w_new)
32/29:
X = np.array([
    [10, 9, 6], [7, 2, 6], [7, 8, 6], [9, 2, 10], [6, 5, 9],
    [8, 9, 8], [9, 4, 8], [3, 4, 7], [1, 3, 4], [4, 8, 10],
    [3, 3, 5], [9, 10, 3], [10, 5, 9], [1, 5, 2], [5, 6, 9]
], dtype=float)
y = np.array([7.1, 16.5, 4.1, 20.0, 10.7, 5.4, 17.0, 5.6,
              3.2, 2.0, 6.7, 2.0, 16.4, -1.9, 8.6])
## y is the target value


def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w_full = X_TX_INV.dot(X_T).dot(y)
    return w_full[0], w_full[1:]

train_linear_regression(X,y)
32/30:
#np.ones(X.shape[0])
#ones = np.ones(len(X))
#np.column_stack([ones,X])
32/31: y_train
32/32:
df_train.dtypes

base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
X_train = df_train[base]
X_train
X_train.isnull().sum()
X_train = X_train.fillna(0)
X_train.isnull().sum()
32/33: w0,weights = train_linear_regression(X_train,y_train)
32/34: pred = w0 + X_train.dot(weights)
32/35:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_train, color = "blue",alpha=0.5, bins = 50)
32/36:
def RMSE(pred,y): 
    error_sq = (pred-y) ** 2
    mean_error_sq = error_sq.mean()
    return np.sqrt(mean_error_sq)

RMSE(pred,y_train)
32/37:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    
    df['age'] = max_year - df.year
    features = base + ['age']
    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
32/38:
X_train = data_prep(df_train)
wo,w = train_linear_regression(X_train,y_train)
X_train_pred = w0 + X_train.dot(w)

X_val = data_prep(df_val)
X_val_pred = w0 + X_val.dot(w)
RMSE(y_val,X_val_pred)
32/39:
sns.histplot(pred, color = "red",alpha=0.5, bins = 50)
sns.histplot(y_val, color = "blue",alpha=0.5, bins = 50)
32/40: df_train.dtypes
32/41:
#df_train['num_doors_2'] = (df_train.number_of_doors == 2).astype('int')
#df_train['num_doors_3'] = (df_train.number_of_doors == 3).astype('int')
#df_train['num_doors_4'] = (df_train.number_of_doors == 4).astype('int')

#df_train = df_train.drop(columns='num_doors_4')
df_train
32/42: df_train["number_of_doors"].value_counts(dropna=False)
32/43: base
32/44:
categorical = {
    'make': ['chevrolet', 'ford', 'volkswagen', 'toyota', 'dodge'],
    'engine_fuel_type': ['regular_unleaded', 'premium_unleaded_(required)',
                         'premium_unleaded_(recommended)', 'flex-fuel_(unleaded/e85)'],
    'transmission_type': ['automatic', 'manual', 'automated_manual'],
    'driven_wheels': ['front_wheel_drive', 'rear_wheel_drive',
                      'all_wheel_drive', 'four_wheel_drive'],
    'market_category': ['crossover', 'flex_fuel', 'luxury', 'luxury,performance', 'hatchback'],
    'vehicle_size': ['compact', 'midsize', 'large'],
    'vehicle_style': ['sedan', '4dr_suv', 'coupe', 'convertible', '4dr_hatchback'],
}
categorical
32/45:
num_doors = [2,3,4]
for v in num_doors:
    df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
df_train
32/46: make = list(df.make.value_counts().head().index)
32/47:
base = ['engine_hp','engine_cylinders','number_of_doors','highway_mpg','city_mpg','popularity']
max_year = df.year.max()

def data_prep(df): 
    df = df.copy()
    df['age'] = max_year - df.year
    features = base + ['age']

    num_doors = [2,3,4]
    for v in num_doors:
        df_train[f"number_doors_{v}"] = (df_train.number_of_doors == v).astype(int)
        features.append(f"number_doors_{v}")

    for v in make: 
        df_train[f"make_{v}"] = (df_train.make == v).astype(int)
        features.append(f"make_{v}")

    df_prep = df[features]
    df_prep = df_prep.fillna(0)
    X = df_prep.values
    return X

data_prep(df_val)
31/5:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
31/6:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=10)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
31/7:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=10000)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
31/8:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
31/9: df_exercise.isnull
31/10: df_exercise.columns.isnull
31/11: df_exercise.isnull
31/12: df_exercise.isnull()
31/13: df_exercise.isnull().sum
31/14: df_exercise.isnull().sum()
31/15: df_exercise.horsepower
31/16: df_exercise.horsepower.describe
31/17: df_exercise.horsepower.describe()
31/18:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]
31/19: df_train
31/20: df_train.isnull.sum()
31/21: df_train.isnull().sum()
31/22:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
31/23:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
31/24: df_train.isnull().sum()
31/25:
df_train.isnull().sum()
df_train.horsepower.mean()
31/26:
df_train.isnull().sum()
df_train.horsepower.mean()
df_train['horsepower'].mean()
31/27:
df_train.isnull().sum()
df_train.horsepower.mean()

df_train_1 = df_train.horsepower.fillna(0)
#df_train_2 =
31/28:
df_train.isnull().sum()
df_train.horsepower.mean()

df_train_1 = df_train.horsepower.fillna(0)
df_train_1.isnull().sum()
#df_train_2 =
31/29:
df_train.isnull().sum()
df_train.horsepower.mean()

df_train_1 = df_train.horsepower.fillna(0)
df_train_1.isnull().sum()
df_train_2 = df_train.horsepower.fillna(df_train.horsepower.mean())
31/30:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]
31/31:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
34/1:
df_train.isnull().sum()
df_train.horsepower.mean()

df_exercise = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
#df_train_2 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/2:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
34/3:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/4: df.head()
34/5:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/6:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/7:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/8:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/9:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
34/10:
df_train.isnull().sum()
df_train.horsepower.mean()

df_exercise = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
#df_train_2 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/11:
df_train.isnull().sum()
df_train.horsepower.mean()

df_exercise = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
df_exercise_1 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/12:
df_train.isnull().sum()
df_train.horsepower.mean()

df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
#df_exercise_1 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/13: df_exercise
34/14:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/15: df.head()
34/16:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/17:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/18:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/19:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/20:
n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]
34/21: df_exercise
34/22:
df_exercise
df_exercise.horsepower.fillna(0)
34/23:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise
34/24:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.sum()
34/25:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull.sum()
34/26:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull()
34/27:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull().sum
34/28:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull().sum()
34/29:
df_exercise
df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull(object='int')
34/30:
df_exercise
df_exercise.horsepower.fillna(0)
34/31:

df_exercise.horsepower.fillna(0)
df_exercise
34/32:

df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull()
34/33:

df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull().sum()
34/34:

df_exercise.horsepower.fillna(0)
df_exercise.horsepower.isnull().sum
34/35:

df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
34/36:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()
34/37:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

df_exercise_wmean = df_exercise
34/38:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

df_exercise_wmean = df_exercise
df_exercise_wmean
34/39:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]

df_exercise_wmean = df_exercise
df_exercise_wmean.horsepower = df_train.horsepower.fillna(df_train.horsepower.mean())
34/40:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/41: df.head()
34/42:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/43:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/44:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/45:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/46:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]

df_exercise_wmean = df_exercise
#df_exercise_wmean.horsepower = df_train.horsepower.fillna(df_train.horsepower.mean())
34/47:

#df_exercise_1 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/48:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]

df_exercise_wmean = df_exercise
df_exercise_wmean
#df_exercise_wmean.horsepower = df_train.horsepower.fillna(df_train.horsepower.mean())
34/49:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]

df_exercise_wmean = df_exercise
df_exercise_wmean.horsepower = df_exercise_wmean.horsepower.fillna(df_train.horsepower.mean())
34/50:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/51: df.head()
34/52:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/53:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/54:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/55:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/56:

df_exercise.horsepower = df_exercise.horsepower.fillna(0)
df_exercise.isnull().sum()

n = len(df_exercise)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df_exercise.iloc[idx[:n_train]]
df_val = df_exercise.iloc[idx[n_train:n_train + n_val]]
df_test = df_exercise.iloc[idx[n_train + n_val:]]

df_exercise_wmean = df_exercise
df_exercise_wmean.horsepower = df_exercise_wmean.horsepower.fillna(df_train.horsepower.mean())
34/57:

#df_exercise_1 = df_train.horsepower.fillna(df_train.horsepower.mean())
34/58:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/59: df.head()
34/60:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/61:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/62:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/63:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/64:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean (computed from real values only)
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
34/65:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
34/66: df_train
34/67: df_train_zero
34/68: df_train_mean
34/69:
def train_linear_regression(X, y):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]
34/70:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

#train_linear_regression(X,y)
34/71: df_train
34/72: df_train.horsepower.values
34/73: df_val.horsepower.values
34/74: df_test.horsepower.values
34/75:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
34/76:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
34/77: df.head()
34/78:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
34/79:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
34/80:
#Q1 - Column with missing values
df_exercise.isnull().sum()
34/81:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
34/82:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
34/83: df_test.horsepower.values
34/84:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values
34/85:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

#train_linear_regression(X,y)
34/86:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values
34/87:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values

y_train_mean
34/88:
## Converting Dataframe into an Array

def prepare_X(df):
    X = df.values
    return X
34/89:
## Converting Dataframe into an Array

def prepare_X(df):
    X = df.values
    return X

X_train_zero = prepare_X(df_train_zero)
34/90:
## Converting Dataframe into an Array

def prepare_X(df):
    X = df.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_zero
34/91: df_train
34/92: df_train.dtypes
34/93:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 
base = {'engine_displacement','num_cylinders','vehicle_weight','acceleration'}

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_zero
35/1:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
35/2: df.head()
35/3:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
35/4:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
35/5:
#Q1 - Column with missing values
df_exercise.isnull().sum()
35/6:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
35/7:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
35/8: df_train.dtypes
35/9:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values
35/10:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 
base = {'engine_displacement','num_cylinders','vehicle_weight','acceleration'}

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_zero
35/11:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 
base = {'engine_displacement','num_cylinders','vehicle_weight','acceleration'}

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_zero
35/12:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_zero
35/13:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X
35/14:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
35/15:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
35/16:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

train_linear_regression(X_train_zero,y_train_zero)
35/17:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
35/18:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)
35/19:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
35/20:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
35/21:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_zero, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
35/22:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
35/23:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
37/1:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
37/2: df.head()
37/3:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
37/4:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
37/5:
#Q1 - Column with missing values
df_exercise.isnull().sum()
37/6:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
37/7:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
37/8: df_train.dtypes
37/9:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values
37/10:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
37/11:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
37/12:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
37/13:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
37/14:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
37/15: df.head()
37/16:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
37/17:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
37/18:
#Q1 - Column with missing values
df_exercise.isnull().sum()
37/19:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
37/20:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
37/21: df_train.dtypes
37/22:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values
37/23:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
37/24:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
37/25:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
37/26:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
37/27:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
37/28: rmse(y_train_mean,y_pred_mean)
37/29:
rmse(y_train_mean,y_pred_mean)
rmse(y_train_zero,y_pred_0)
38/1:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
38/2: df.head()
38/3:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
38/4:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
38/5:
#Q1 - Column with missing values
df_exercise.isnull().sum()
38/6:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
38/7:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'horsepower': 0})
df_val_zero = df_val.fillna({'horsepower': 0})
df_test_zero = df_test.fillna({'horsepower': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'horsepower': hp_mean})
df_val_mean = df_val.fillna({'horsepower': hp_mean})
df_test_mean = df_test.fillna({'horsepower': hp_mean})
38/8: df_train.dtypes
38/9:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.horsepower.values
y_val_zero = df_val_zero.horsepower.values
y_test_zero = df_test_zero.horsepower.values

y_train_mean = df_train_mean.horsepower.values
y_val_mean = df_val_mean.horsepower.values
y_test_mean = df_test_mean.horsepower.values
38/10:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
38/11:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
38/12:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
38/13:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('horsepower')
plt.title('Predictions vs actual distribution')

plt.show()
38/14:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
38/15:
rmse(y_train_mean,y_pred_mean) ##Mean is better
rmse(y_train_zero,y_pred_0)
38/16:
##Training model with a regularized linear regression

def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
38/17:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
38/18:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression_reg(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression_reg(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
38/19:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
38/20:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
score
38/21:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
    score[r] = rmse_reg(y_train_mean,y_pred_reg)
score
38/22:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
    score[r] = round(rmse_reg(y_train_mean,y_pred_reg))
score
38/23:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
    score[r] = round(rmse_reg(y_train_mean,y_pred_reg),2)
score
38/24:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean)
    y_pred_reg = w0 + X_train_mean.dot(w)
    score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
score
38/25:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
score
38/26:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
reg_rmse_score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    reg_rmse_score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
reg_rmse_score
38/27:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'horsepower': 0}),
            'val':   df_val.fillna({'horsepower': 0}),
            'test':  df_test.fillna({'horsepower': 0}),
        },
        'mean': {
            'train': df_train.fillna({'horsepower': hp_mean}),
            'val':   df_val.fillna({'horsepower': hp_mean}),
            'test':  df_test.fillna({'horsepower': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
38/28:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']
    # build X_train, y_train, X_val, y_val from d['train'] and d['val']
    # the same way you did before, then:
    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse_reg(y_val, y_pred)

round(np.std(list(scores.values())), 3)
38/29:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train, y_train = prepare_X_y(d['train'])
    X_val, y_val = prepare_X_y(d['val'])

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse_reg(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
   1:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
   2:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
   3: df.head()
   4:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
   5:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
   6:
#Q1 - Column with missing values
df_exercise.isnull().sum()
   7:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
   8:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
   9: df_train.dtypes
  10:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.fuel_efficiency_mpg.values
y_val_zero = df_val_zero.fuel_efficiency_mpg.values
y_test_zero = df_test_zero.fuel_efficiency_mpg.values

y_train_mean = df_train_mean.fuel_efficiency_mpg.values
y_val_mean = df_val_mean.fuel_efficiency_mpg.values
y_test_mean = df_test_mean.fuel_efficiency_mpg.values
  11:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration','horsepower']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
  12:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  13:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  14:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  15:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
  16:
rmse(y_train_mean,y_pred_mean) ##Mean is better
rmse(y_train_zero,y_pred_0)
  17:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression_reg(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression_reg(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  18:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
reg_rmse_score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    reg_rmse_score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
reg_rmse_score
  19:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'horsepower': 0}),
            'val':   df_val.fillna({'horsepower': 0}),
            'test':  df_test.fillna({'horsepower': 0}),
        },
        'mean': {
            'train': df_train.fillna({'horsepower': hp_mean}),
            'val':   df_val.fillna({'horsepower': hp_mean}),
            'test':  df_test.fillna({'horsepower': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
  20:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train, y_train = prepare_X_y(d['train'])
    X_val, y_val = prepare_X_y(d['val'])

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse_reg(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  21:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  22:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'fuel_efficiency_mpg': 0}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': 0}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': 0}),
        },
        'mean': {
            'train': df_train.fillna({'fuel_efficiency_mpg': hp_mean}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': hp_mean}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
  23:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  24:
scores = {}
for seed in seed_values:
    d = splits[seed]['mean']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  25:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  26:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
  27: df.head()
  28:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
  29:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
  30:
#Q1 - Column with missing values
df_exercise.isnull().sum()
  31:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
  32:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  33: df_train.dtypes
  34:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.fuel_efficiency_mpg.values
y_val_zero = df_val_zero.fuel_efficiency_mpg.values
y_test_zero = df_test_zero.fuel_efficiency_mpg.values

y_train_mean = df_train_mean.fuel_efficiency_mpg.values
y_val_mean = df_val_mean.fuel_efficiency_mpg.values
y_test_mean = df_test_mean.fuel_efficiency_mpg.values
  35:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration','horsepower']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
  36:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  37:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  38:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  39:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
  40:
rmse(y_train_mean,y_pred_mean) ##Mean is better
rmse(y_train_zero,y_pred_0)
  41:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression_reg(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression_reg(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  42:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
reg_rmse_score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    reg_rmse_score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
reg_rmse_score
  43:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'fuel_efficiency_mpg': 0}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': 0}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': 0}),
        },
        'mean': {
            'train': df_train.fillna({'fuel_efficiency_mpg': hp_mean}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': hp_mean}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
  44:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  45:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(9)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  46:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(9)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  47:
df_full_train = pd.concat([df_train_zero, df_val_zero]).reset_index(drop=True)

X_full_train = prepare_X(df_full_train)
y_full_train = df_full_train.fuel_efficiency_mpg.values

X_test = prepare_X(df_test_zero)
y_test = df_test_zero.fuel_efficiency_mpg.values

w0, w = train_linear_regression_reg(X_full_train, y_full_train, r=0.001)
y_pred = w0 + X_test.dot(w)
rmse(y_test, y_pred)
  48:
## Q6 - Final model: train on train + validation, evaluate on test
## Uses seed 9 splits with missing horsepower filled with 0

# Combine the training and validation sets into one larger training set.
# Model choices (fill method, r value) were already made using the validation
# set, so its data can now go toward training the final model.
# reset_index(drop=True) gives the combined dataframe a clean 0..n-1 index
# instead of the shuffled indices carried over from the original split.
df_full_train = pd.concat([df_train_zero, df_val_zero]).reset_index(drop=True)

# Build the feature matrix from the combined data.
# prepare_X selects the columns in `base` and converts them to a NumPy array.
X_full_train = prepare_X(df_full_train)

# Target values: the actual fuel efficiency the model learns to predict.
y_full_train = df_full_train.fuel_efficiency_mpg.values

# Prepare the test set the same way as the training data.
# The test set was not used for training or for any modeling decisions,
# so its score is an unbiased estimate of performance on new cars.
X_test = prepare_X(df_test_zero)          # inputs the model predicts from
y_test = df_test_zero.fuel_efficiency_mpg.values   # true mpg to compare against

# Train the regularized linear regression on the combined data.
# r=0.001 adds a small penalty on large weights (ridge regularization).
# w0 is the bias (intercept); w is the array of weights, one per feature.
w0, w = train_linear_regression_reg(X_full_train, y_full_train, r=0.001)

# Predict mpg for each test car: bias + (features x weights).
y_pred = w0 + X_test.dot(w)

# RMSE: the typical size of a prediction error, in mpg.
# Lower is better.
rmse(y_test, y_pred)
  49:
# Combine the training and validation sets into one larger training set.
# Model choices (fill method, r value) were already made using the validation
# set, so its data can now go toward training the final model.
# reset_index(drop=True) gives the combined dataframe a clean 0..n-1 index
# instead of the shuffled indices carried over from the original split.
df_full_train = pd.concat([df_train_zero, df_val_zero]).reset_index(drop=True)

# Build the feature matrix from the combined data.
# prepare_X selects the columns in `base` and converts them to a NumPy array.
X_full_train = prepare_X(df_full_train)

# Target values: the actual fuel efficiency the model learns to predict.
y_full_train = df_full_train.fuel_efficiency_mpg.values

# Prepare the test set the same way as the training data.
# The test set was not used for training or for any modeling decisions,
# so its score is an unbiased estimate of performance on new cars.
X_test = prepare_X(df_test_zero)          # inputs the model predicts from
y_test = df_test_zero.fuel_efficiency_mpg.values   # true mpg to compare against

# Train the regularized linear regression on the combined data.
# r=0.001 adds a small penalty on large weights (ridge regularization).
# w0 is the bias (intercept); w is the array of weights, one per feature.
w0, w = train_linear_regression_reg(X_full_train, y_full_train, r=0.001)

# Predict mpg for each test car: bias + (features x weights).
y_pred = w0 + X_test.dot(w)

# RMSE: the typical size of a prediction error, in mpg.
# Lower is better.
rmse(y_test, y_pred)
  50:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
  51: df.head()
  52:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
  53:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
  54:
#Q1 - Column with missing values
df_exercise.isnull().sum()
  55:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
  56:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  57: df_train.dtypes
  58:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.fuel_efficiency_mpg.values
y_val_zero = df_val_zero.fuel_efficiency_mpg.values
y_test_zero = df_test_zero.fuel_efficiency_mpg.values

y_train_mean = df_train_mean.fuel_efficiency_mpg.values
y_val_mean = df_val_mean.fuel_efficiency_mpg.values
y_test_mean = df_test_mean.fuel_efficiency_mpg.values
  59:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration','horsepower']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
  60:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  61:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  62:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  63:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
  64:
rmse(y_train_mean,y_pred_mean) ##Mean is better
rmse(y_train_zero,y_pred_0)
  65:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression_reg(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression_reg(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  66:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
reg_rmse_score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    reg_rmse_score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
reg_rmse_score
  67:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'fuel_efficiency_mpg': 0}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': 0}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': 0}),
        },
        'mean': {
            'train': df_train.fillna({'fuel_efficiency_mpg': hp_mean}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': hp_mean}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
  68:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  69:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(9)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  70:
# Combine the training and validation sets into one larger training set.
# Model choices (fill method, r value) were already made using the validation
# set, so its data can now go toward training the final model.
# reset_index(drop=True) gives the combined dataframe a clean 0..n-1 index
# instead of the shuffled indices carried over from the original split.
df_full_train = pd.concat([df_train_zero, df_val_zero]).reset_index(drop=True)

# Build the feature matrix from the combined data.
# prepare_X selects the columns in `base` and converts them to a NumPy array.
X_full_train = prepare_X(df_full_train)

# Target values: the actual fuel efficiency the model learns to predict.
y_full_train = df_full_train.fuel_efficiency_mpg.values

# Prepare the test set the same way as the training data.
# The test set was not used for training or for any modeling decisions,
# so its score is an unbiased estimate of performance on new cars.
X_test = prepare_X(df_test_zero)          # inputs the model predicts from
y_test = df_test_zero.fuel_efficiency_mpg.values   # true mpg to compare against

# Train the regularized linear regression on the combined data.
# r=0.001 adds a small penalty on large weights (ridge regularization).
# w0 is the bias (intercept); w is the array of weights, one per feature.
w0, w = train_linear_regression_reg(X_full_train, y_full_train, r=0.001)

# Predict mpg for each test car: bias + (features x weights).
y_pred = w0 + X_test.dot(w)

# RMSE: the typical size of a prediction error, in mpg.
# Lower is better.
rmse(y_test, y_pred)
  71:
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = 'https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/car_fuel_efficiency_2026.csv'
!curl -O $data
df = pd.read_csv('car_fuel_efficiency_2026.csv')
  72: df.head()
  73:
df.columns = df.columns.str.lower().str.replace(" ","_")
df.dtypes[df.dtypes == 'str']
string_cols = list(df.dtypes[df.dtypes == 'str'].index)
string_cols
for columns in string_cols: 
    df[columns] = df[columns].str.lower().str.replace(" ","_")

df.head()
  74:
## Preparing the Dataset
df_exercise = df[['engine_displacement',
'horsepower',
'vehicle_weight',
'model_year',
'fuel_efficiency_mpg']]
df_exercise.head()

## Exploratory Data Analysis
df_exercise['fuel_efficiency_mpg'].unique()[:5]
#df_exercise['fuel_efficiency_mpg'].nunique
sns.histplot(df_exercise.fuel_efficiency_mpg,bins=100)
## indentifying long tail
sns.histplot(df_exercise.fuel_efficiency_mpg > 35,bins=100)
df_exercise.fuel_efficiency_mpg.describe(percentiles=[.5, .9, .95, .99])
  75:
#Q1 - Column with missing values
df_exercise.isnull().sum()
  76:
#Q2 - What's the median (50% percentile) for variable 'horsepower'?
df_exercise.horsepower.describe()
  77:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(42)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  78: df_train.dtypes
  79:
## VALIDATION FRAMEWORK

y_train_zero = df_train_zero.fuel_efficiency_mpg.values
y_val_zero = df_val_zero.fuel_efficiency_mpg.values
y_test_zero = df_test_zero.fuel_efficiency_mpg.values

y_train_mean = df_train_mean.fuel_efficiency_mpg.values
y_val_mean = df_val_mean.fuel_efficiency_mpg.values
y_test_mean = df_test_mean.fuel_efficiency_mpg.values
  80:
## Converting Dataframe into an Array
## Selecting a primary set of features to include in v1 of the regression model 

base = ['engine_displacement', 'num_cylinders', 'vehicle_weight', 'acceleration','horsepower']

def prepare_X(df):
    df_num = df[base]
    df_num = df_num.fillna(0)
    X = df_num.values
    return X

X_train_zero = prepare_X(df_train_zero)
X_train_mean = prepare_X(df_train_mean)
X_train_zero, X_train_mean
  81:
def train_linear_regression(X,y):
    
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones,X])
    X_T = np.linalg.matrix_transpose(X)
    X_TX = X_T @ X
    X_TX_INV = np.linalg.inv(X_TX)
    #X_TX.dot(X_TX_INV).round()
    (X_TX @ X_TX_INV).round()
    w = X_TX_INV.dot(X_T).dot(y)
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  82:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_zero, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_0, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  83:
plt.figure(figsize=(6, 4))

sns.histplot(y_train_mean, label='target', color='#222222', alpha=0.6, bins=40)
sns.histplot(y_pred_mean, label='prediction', color='#aaaaaa', alpha=0.8, bins=40)

plt.legend()

plt.ylabel('Frequency')
plt.xlabel('fuel_efficiency_mpg')
plt.title('Predictions vs actual distribution')

plt.show()
  84:
## Calculating RMSE
def rmse(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)
  85:
rmse(y_train_mean,y_pred_mean) ##Mean is better
rmse(y_train_zero,y_pred_0)
  86:
##Training model with a regularized linear regression

def train_linear_regression_reg(X, y, r=0.0):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])

    XTX = X.T.dot(X)
    reg = r * np.eye(XTX.shape[0])
    XTX = XTX + reg

    XTX_inv = np.linalg.inv(XTX)
    w = XTX_inv.dot(X.T).dot(y)
    
    return w[0], w[1:]

w0_0, w_0 = train_linear_regression_reg(X_train_zero,y_train_zero)
w0_mean, w_mean = train_linear_regression_reg(X_train_mean,y_train_mean)

y_pred_0 = w0_0 + X_train_zero.dot(w_0)
y_pred_mean = w0_mean + X_train_mean.dot(w_mean)
y_pred_0, y_pred_mean
  87:
def rmse_reg(y, y_pred):
    error = y_pred - y
    mse = (error ** 2).mean()
    return np.sqrt(mse)

r_values = [0, 0.01, 0.1, 1, 5, 10, 100]
reg_rmse_score = {}

for r in r_values: 
    w0, w = train_linear_regression_reg(X_train_mean,y_train_mean,r=r)
    y_pred_reg = w0 + X_train_mean.dot(w)
    reg_rmse_score[r] = round(rmse_reg(y_train_mean,y_pred_reg),4)
reg_rmse_score
  88:
def split_and_fill(df, seed):
    n = len(df)
    n_val = int(n * 0.2)
    n_test = int(n * 0.2)
    n_train = n - n_val - n_test

    np.random.seed(seed)
    idx = np.arange(n)
    np.random.shuffle(idx)

    df_train = df.iloc[idx[:n_train]]
    df_val = df.iloc[idx[n_train:n_train + n_val]]
    df_test = df.iloc[idx[n_train + n_val:]]

    hp_mean = df_train.horsepower.mean()

    return {
        'zero': {
            'train': df_train.fillna({'fuel_efficiency_mpg': 0}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': 0}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': 0}),
        },
        'mean': {
            'train': df_train.fillna({'fuel_efficiency_mpg': hp_mean}),
            'val':   df_val.fillna({'fuel_efficiency_mpg': hp_mean}),
            'test':  df_test.fillna({'fuel_efficiency_mpg': hp_mean}),
        },
    }

seed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
splits = {seed: split_and_fill(df, seed) for seed in seed_values}
  89:
scores = {}
for seed in seed_values:
    d = splits[seed]['zero']

    X_train = prepare_X(d['train'])
    y_train = d['train'].fuel_efficiency_mpg.values
    X_val = prepare_X(d['val'])
    y_val = d['val'].fuel_efficiency_mpg.values

    w0, w = train_linear_regression_reg(X_train, y_train, r=0)
    y_pred = w0 + X_val.dot(w)
    scores[seed] = rmse(y_val, y_pred)

scores, round(np.std(list(scores.values())), 3)
  90:
n = len(df)
n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

np.random.seed(9)
idx = np.arange(n)
np.random.shuffle(idx)

df_train = df.iloc[idx[:n_train]]
df_val = df.iloc[idx[n_train:n_train + n_val]]
df_test = df.iloc[idx[n_train + n_val:]]

# Option 1: fill with 0
df_train_zero = df_train.fillna({'fuel_efficiency_mpg': 0})
df_val_zero = df_val.fillna({'fuel_efficiency_mpg': 0})
df_test_zero = df_test.fillna({'fuel_efficiency_mpg': 0})

# Option 2: fill with the training-set mean
hp_mean = df_train.horsepower.mean()
df_train_mean = df_train.fillna({'fuel_efficiency_mpg': hp_mean})
df_val_mean = df_val.fillna({'fuel_efficiency_mpg': hp_mean})
df_test_mean = df_test.fillna({'fuel_efficiency_mpg': hp_mean})
  91:
# Combine the training and validation sets into one larger training set.
# Model choices (fill method, r value) were already made using the validation
# set, so its data can now go toward training the final model.
# reset_index(drop=True) gives the combined dataframe a clean 0..n-1 index
# instead of the shuffled indices carried over from the original split.
df_full_train = pd.concat([df_train_zero, df_val_zero]).reset_index(drop=True)

# Build the feature matrix from the combined data.
# prepare_X selects the columns in `base` and converts them to a NumPy array.
X_full_train = prepare_X(df_full_train)

# Target values: the actual fuel efficiency the model learns to predict.
y_full_train = df_full_train.fuel_efficiency_mpg.values

# Prepare the test set the same way as the training data.
# The test set was not used for training or for any modeling decisions,
# so its score is an unbiased estimate of performance on new cars.
X_test = prepare_X(df_test_zero)          # inputs the model predicts from
y_test = df_test_zero.fuel_efficiency_mpg.values   # true mpg to compare against

# Train the regularized linear regression on the combined data.
# r=0.001 adds a small penalty on large weights (ridge regularization).
# w0 is the bias (intercept); w is the array of weights, one per feature.
w0, w = train_linear_regression_reg(X_full_train, y_full_train, r=0.001)

# Predict mpg for each test car: bias + (features x weights).
y_pred = w0 + X_test.dot(w)

# RMSE: the typical size of a prediction error, in mpg.
# Lower is better.
rmse(y_test, y_pred)
  92:
import os, socket
print(socket.gethostname(), os.getcwd())
  93: %history -g -f /workspaces/machine-learning-zoomcamp/Week_2/HW2_code_backup.py
