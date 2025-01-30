# PASKAL'S TRIANGLE

 def generate_pascals_triangle(a):
    triangle = [[1]]

    for i in range(1, a):
        row = [1]  
        for j in range(1, i):
        
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1]))) 

    for row in triangle:
        row_string = " ".join(map(str, row))
        print(row_string.center(max_width))

a = 5 
pascals_triangle = generate_pascals_triangle(a)
print_pascals_triangle(pascals_triangle)