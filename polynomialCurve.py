
#library importation
import numpy as np
import matplotlib.pyplot as plt

# in this function i collect the data from the user
def collect_data(variable_name):
    data = []
    #for showing that the data's are ended use 'E' to close the arry
    print(f"Enter the values for {variable_name} (enter 'E' to finish):")
    while True:
        value = input(f"Enter {variable_name} value: ")
        if value.upper() == 'E':  # Stop input if 'E' is entered
            break
        try:
            # Replace commas with dots to handle the decimal separator issue ()
            value = value.replace(',', '.')
            data.append(float(value))
        except ValueError:
            print("Please enter a valid number.")
    return np.array(data)

# Ask the user for the names of the data arrays
x_name = input("Enter the name of the data (e.g., 'speed'): ")
y_name = input("Enter the name of the data (e.g., 'MW'): ")

# create the data arrays according to the names that are entered by user
x = collect_data(x_name)
y = collect_data(y_name)

# Check if the lengths of the x and y arrays are the same since they must be equal
if len(x) != len(y):
    print("Error: x and y arrays must have the same length.")
else:
    # 4th degree polynomial trendline fitting 
    polynomial_coefficients = np.polyfit(x, y, 4)

    # polynomial equation function
    polynomial = np.poly1d(polynomial_coefficients)

    # plot of the trendline
    x_graph = np.linspace(min(x), max(x), 100)
    y_graph = polynomial(x_graph)

    plt.plot(x, y, 'bo', label=f'{x_name} vs {y_name}')
    plt.plot(x_graph, y_graph, 'r-', label='4th degree polynomial trendline')

    # display the polynomial equation at the top (outside the plot area)
    equation_text = f"y = {polynomial_coefficients[0]:.4f}x⁴ + {polynomial_coefficients[1]:.4f}x³ + {polynomial_coefficients[2]:.4f}x² + {polynomial_coefficients[3]:.4f}x + {polynomial_coefficients[4]:.4f}"
    plt.figtext(0.5, 0.95, equation_text, ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    # labels of the graph 
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.show()
      
    # Output the polynomial coefficients
    print("Polynomial Coefficients:", polynomial_coefficients)





