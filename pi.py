import decimal
import time
from tqdm import tqdm

def calculate_pi(digits, output_file):
    decimal.getcontext().prec = digits + 2  # Set precision
    pi = decimal.Decimal(0)
    start_time = time.time()
    
    with open(output_file, 'w') as file, tqdm(total=digits, desc='Calculating Pi') as pbar:
        for k in range(digits):
            pi += (decimal.Decimal(1)/(16**k)) * (
                decimal.Decimal(4)/(8*k+1) - decimal.Decimal(2)/(8*k+4) - decimal.Decimal(1)/(8*k+5) - decimal.Decimal(1)/(8*k+6)
            )
            pbar.update(1)  # Update progress bar
        
        file.write("\nPi: {}\n".format(pi))  # Write pi to file
        end_time = time.time()
        execution_time = end_time - start_time
        file.write("Execution time: {} seconds\n".format(execution_time))  # Write execution time to file

    return pi

# Example usage:
digits = 100_000
output_file = '100Kpi_digits.txt'

pi = calculate_pi(digits, output_file)

print("Final result:", pi)
print("Calculation complete.")
