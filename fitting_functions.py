#linear line
def linear (m,x,b):
    return m*x+b
#gives unit for slope
def slope_units (x_unit, y_unit):
    return y_unit+'/'+x_unit
#calls other functions to give full equation
def print_equations (m, b, x_unit, y_unit):
    print('The equation of the line is: y=',round(m,4),slope_units(x_unit, y_unit),'x+',round(b,4),y_unit)
    
    
