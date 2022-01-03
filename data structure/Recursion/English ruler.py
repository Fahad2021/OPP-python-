def draw_line(thick_length,thick_lebel=""):
    line='-'*thick_length
    if thick_lebel:
        line +=''+thick_lebel
    print(line)
def draw_interval(centa_length):
    if centa_length>0:
        draw_interval(centa_length-1)
        draw_line(centa_length)
        draw_interval(centa_length-1)
def draw_ruler(num_inches,major_length):
    draw_line(major_length,"0")
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(j))
draw_interval(3)
# draw_ruler(1,2)