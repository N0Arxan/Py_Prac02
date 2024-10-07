x = int(input("ensert point x : "))
y = int(input("ensert point y : "))

points = [x,y]
points.sort(key=lambda x: abs(x-0))
    

print(points[0])