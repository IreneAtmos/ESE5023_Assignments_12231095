from itertools import product

def find_expression(target):
    valid_expressions = []

    # Generate all possible combinations of + and - operators
    for operators in product('+- ', repeat=7):
        
        # Loop through all combinations and evaluate expressions
        for begin in ['1','1+','1-']:
            expression = begin
            num_str = '2'
            for op, num in zip(operators, range(3, 10)):
                if op == ' ':
                    num_str += str(num)
                else:
                    expression += num_str
                    expression += op
                    num_str = str(num)
            expression += num_str
            
            # Evaluate the expression
            result = eval(expression)

            # Check if the result matches the target
            if result == target:
                valid_expressions.append(expression)
    
    for valid_expression in valid_expressions:
        print(valid_expression + '=' + str(target))

# Example usage:
find_expression(50)


def count_expression(target):
    count = 0
    valid_expressions = []

    # Generate all possible combinations of + and - operators
    for operators in product('+- ', repeat=7):
        
        # Loop through all combinations and evaluate expressions
        for begin in ['1','1+','1-']:
            expression = begin
            num_str = '2'
            for op, num in zip(operators, range(3, 11)):
                if op == ' ':
                    num_str += str(num)
                else:
                    expression += num_str
                    expression += op
                    num_str = str(num)
            expression += num_str
            
            # Evaluate the expression
            result = eval(expression)


            # Check if the result matches the target
            if result == target:
                valid_expressions.append(expression)
                count += 1
                
    return count

# Example usage:
count_expression(50)


Total_solutions = []
Total_numubers = []

for i in range(1,101):
    count = count_expression(i)
    Total_solutions.append(count)
    Total_numubers.append(str(i)+'-'+str(count))

print(Total_solutions,'\n')
print(Total_numubers)

sol_max = max(Total_solutions)
num_max = Total_solutions.index(sol_max)+1
print('Number',num_max,'yields the maximum of Total_solutions: ',sol_max)

sol_min = min(Total_solutions)
num_min = Total_solutions.index(sol_min)+1
print('Number',num_min,'yields the minimum of Total_solutions: ',sol_min)


import matplotlib.pyplot as plt

# choose data
x = range(1,101)
y = Total_solutions

# plot
fig, ax = plt.subplots(figsize=(6,2))

ax.plot(x, y, linewidth=1.5)
ax.set_xlabel('The target numbers')
ax.set_ylabel('The total solutions')

plt.show()