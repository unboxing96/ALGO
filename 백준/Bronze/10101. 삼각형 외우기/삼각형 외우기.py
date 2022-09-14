def tri(a, b, c):

    if a == b == c:
        return "Equilateral"
    
    elif a + b + c == 180 and (a == b or b == c or a == c):
        return "Isosceles"
    
    elif a + b + c == 180 and (a != b != c):
        return "Scalene"
    
    else:
        return "Error"
    
x = int(input())
y = int(input())
z = int(input())

print(tri(x, y, z))