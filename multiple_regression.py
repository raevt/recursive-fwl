"""
    Rae Adimer

    Estimates a multiple regression using a series of partialed-out linear regressions. Returns estimated model and R-squared.

    This is far from efficient, but it works. I've tested it out to 5 independent variables, running the same regressions in Stata and receiving the same results.

    Be sure that the data is in a .csv, and:
     - the first row is the names of the variables
     - the first column is the dependent variable
     - there are no missing observations
"""


def input_data(filename):
    # Gets data from specified file, returns dictionary and list of variables
    with open(filename, 'r') as file:
        line_counter = 0
        for line in file:
            if line_counter == 0:
                vars = line.strip().split(',')
                data = {}
                for n in vars:
                    data[n] = []
            else:
                nums = line.strip().split(',')
                for i in range(len(nums)):
                    data[vars[i]].append(float(nums[i]))
            line_counter += 1
    
    # convert to tuples
    data2 = {}
    for i in data:
        data2[i] = tuple(data[i])

    return data2, vars


def simple_linear_regression(y, x):
    # Estimates a simple linear regression, returns the estimated coefficient, intercept, and residuals

    # generate y and x means
    y_sum = 0
    for i in y:
        y_sum += i
    y_mean = y_sum / len(y)
    x_sum = 0
    for i in x:
        x_sum += i
    x_mean = x_sum / len(x)

    # coefficient
    numerator = 0
    denominator = 0
    for i in range(len(y)):
        numerator += (y[i] - y_mean) * (x[i] - x_mean)
    for i in x:
        denominator += (i - x_mean) ** 2
    coefficient = numerator / denominator

    # intercept
    intercept = y_mean - (coefficient * x_mean)

    # estimate model, make list of residuals
    y_hats = []
    for i in range(len(y)):
        y_hats.append((coefficient * x[i]) + intercept)
    residuals = []
    for idx in range(len(y)):
        residuals.append(y[idx] - y_hats[idx])

    return coefficient, intercept, residuals

def generate_new_vars(variables):
    # Generates k new variable lists of k-1 variables, i.e., the regressions to run in partialing out a multiple regression.
    new_vars_list = []
    for i in range(1, len(variables)):
        new_vars = [variables[i]] + (variables[1:i] + variables[i+1:])
        new_vars_list.append(new_vars)
    return new_vars_list

def multiple_regression(data_dict, variables):
    # Recursively estimates multiple regressions through partialing out
    coefficients = []
    means_list = means(data_dict)
    y_key = variables[0]

    if len(variables) == 2:
        coeff, interc, residu = simple_linear_regression(data_dict[variables[0]], data_dict[variables[1]])
        coefficients.append(coeff)
        return coefficients, interc, residu
    
    else:
        new_vars_list = generate_new_vars(variables)
        coefficients = []

        # This is the fun recursive bit
        for n in new_vars_list:
           n_coefficients, n_intercept, n_residuals = multiple_regression(data_dict.copy(), n.copy())
           s_coefficient, s_intercept, s_residuals = simple_linear_regression(data_dict[y_key], n_residuals)
           coefficients.append(s_coefficient)
        
        # Intercept calculation
        intercept = means_list[0]
        for n in range(len(coefficients)):
            intercept -= (coefficients[n] * means_list[n + 1])
        
        # generate model
        y_hats = []
        for i in range(len(data_dict[y_key])):
            y_to_add = intercept
            for n in range(len(coefficients)):
                y_to_add += coefficients[n] * data_dict[variables[n + 1]][i]
            y_hats.append(y_to_add)
        
        # get list of residuals
        residuals = []
        for i in range(len(y_hats)):
            residuals.append(data_dict[variables[0]][i] - y_hats[i])
        # return statement
        return coefficients, intercept, residuals

def means(data_dict):
    # Gets means of all items in data_dict, returns them
    means = []
    for n in data_dict:
        sum = 0
        for i in data_dict[n]:
            sum += i
        means.append(sum / len(data_dict[n]))
    return means

def output(data_dict, variables, coefficients, intercept, residuals):
    # Formats and prints output, including calculating r-squared

    # Variables information
    print("Variables: ", end="")
    for i in variables:
        if i == variables[-1]:
            print(i)
        else:
            print(i, end=", ")
    print(f"Dependent variables: 1 ({variables[0]})\nIndependent variables: {len(variables)-1}\nObservations: {len(data_dict[variables[0]])}")

    # Estimated model
    print(f"{variables[0]} = ", end="")
    for n in range(len(variables)-1):
        print(f"{coefficients[n]:.4f}{variables[n+1]} + ", end="")
    print(f"{intercept:.4f}")
    
    # Calculate and output r-squared
    SSR = 0
    for i in residuals:
        SSR += i ** 2
    y_sum = 0
    for i in data_dict[variables[0]]:
        y_sum += i
    y_mean = y_sum / len(data_dict[variables[0]])
    SST = 0
    for i in data_dict[variables[0]]:
        SST += (i - y_mean) ** 2
    print(f"R squared: {1 - (SSR / SST):.4f}")

def main():
    # handle file input
    filename = str(input("Enter the name of your file: "))
    try:
        data_dict, variables = input_data(filename)
    except:
        print("There was a problem with opening or parsing the file.")
        return
    
    # run regression
    coefficients, intercept, residuals = multiple_regression(data_dict, variables)
    
    # output results
    output(data_dict, variables, coefficients, intercept, residuals)
    
if __name__ == "__main__":
    main()