import decimal
import time

def calculate_pi(digits, output_file):
    decimal.getcontext().prec = digits + 2  # Set precision
    pi = decimal.Decimal(0)
    start_time = time.time()  # Record start time
    with open(output_file, 'w') as file:
        for k in range(digits):
            pi += (decimal.Decimal(1)/(16**k)) * (
                decimal.Decimal(4)/(8*k+1) - decimal.Decimal(2)/(8*k+4) - decimal.Decimal(1)/(8*k+5) - decimal.Decimal(1)/(8*k+6)
            )
        file.write("\nPi: {}\n".format(pi))  # Write pi to file
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        file.write("\nExecution time: {} seconds\n".format(execution_time)+"\n")  # Write execution time to file
    return pi, execution_time

# Example usage:
digits = 1000
output_file = '1Kpi_digits.txt'
pi, execution_time = calculate_pi(digits, output_file)
print("Final result:", pi)
print("Execution time:", execution_time, "seconds")
