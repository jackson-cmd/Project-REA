import psutil
import subprocess
import csv
import time

# Filename for the CSV output
output_csv = "cpu_usage.csv"


# Function to get current CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


# Function to run the Node.js script with a 5-second timeout
def run_node_script():
    # Start the Node.js script using subprocess.Popen
    process = subprocess.Popen(["node", "pp.js"])  # Ensure the script name is correct
    try:
        # Wait for the process to complete, with a timeout of 5 seconds
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        # If the process does not complete within the timeout, kill it
        process.kill()
        print("Node.js script was terminated after 5 seconds")
    return


# Open a CSV file to write
with open(output_csv, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Before Running Node", "After Running Node"])

    # Loop to repeat the process 1000 times (adjusted to 10 for this example)
    for _ in range(1000):
        # Get CPU usage before running the script
        cpu_before = get_cpu_usage()

        # Run the Node.js script
        run_node_script()

        # Get CPU usage after running the script
        cpu_after = get_cpu_usage()

        # Write the results to the CSV file
        writer.writerow([cpu_before, cpu_after])

        # Optional: sleep to avoid overloading the CPU in quick succession
        time.sleep(1)  # Sleep for 1 second

print("Process completed and data has been written to", output_csv)
