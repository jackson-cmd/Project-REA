import psutil
import time
import platform
import os


def get_cpu_usage():
    """Retrieve the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def alert_user(message):
    """Display an alert box on different platforms."""
    if platform.system() == "Windows":
        import ctypes

        ctypes.windll.user32.MessageBoxW(0, message, "CPU Alert", 1)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"osascript -e 'display alert \"{message}\"'")
    else:  # Assuming Linux
        os.system(f'notify-send "CPU Alert" "{message}"')


def monitor_cpu(threshold_percentage):
    """Monitor CPU usage and alert when exceeding the defined threshold."""
    baseline_usage = get_cpu_usage()
    threshold = baseline_usage * (1 + threshold_percentage / 100)

    print(f"Baseline CPU Usage: {baseline_usage}%")
    print(f"Set Alert Threshold: {threshold}%")

    while True:
        current_usage = get_cpu_usage()
        if current_usage > threshold:
            alert_message = f"Alert: CPU usage exceeded the threshold! Current Usage: {current_usage}%"
            alert_user(alert_message)
        time.sleep(5)  # Check every 5 seconds


if __name__ == "__main__":
    threshold_input = float(
        input("Enter the threshold percentage (e.g., 20 for 20%): ")
    )
    monitor_cpu(threshold_input)
