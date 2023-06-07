# 1.Exerise
g = lambda x,y: x+y
print(g(2,3))

# 2.Exercise
k = lambda x,y,z: x//y+z
print(k(10,4,2))

# 3. Exercise
max = lambda a, b : a if (a>b) else b
print(max(1,2))

# 4.Exercise
ages = [12,87,32,4,12,56,40]
adults = list(filter(lambda age: age > 18,ages))
print(adults)

# 5.Exercise
lambda_cube = lambda x: x*x*x

print("cube :",lambda_cube(3))