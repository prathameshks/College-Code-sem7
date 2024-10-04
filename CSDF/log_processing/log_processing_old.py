import subprocess
import schedule
import time
import re

# Configuration
LOG_FILE_PATH = 'system_logs.log'

# Function to run a system command and return its output
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e}")
        return ""

# Function to capture system logs
def capture_system_logs():
    commands = {
        'dmesg': 'dmesg --since "1 minute ago"',  # Capture kernel messages from the last minute
        'journalctl': 'journalctl --since "1 minute ago" --no-pager',  # Capture systemd logs from the last minute
        'syslog': 'tail -n 100 /var/log/syslog'  # Capture the last 100 lines of syslog
    }

    with open(LOG_FILE_PATH, 'a') as log_file:
        for name, cmd in commands.items():
            output = run_command(cmd)
            log_file.write(f"--- {name.upper()} ---\n")
            log_file.write(output + "\n\n")

    print("System logs captured.")

# Function to perform event correlation (basic example)
def correlate_events():
    try:
        with open(LOG_FILE_PATH, 'r') as log_file:
            logs = log_file.read()
            
            # Example correlation: Detecting frequent "error" occurrences
            errors = re.findall(r'error', logs, re.IGNORECASE)
            if len(errors) > 5:
                print("Event Correlation: High number of errors detected.")

            # Example correlation: Detecting suspicious login attempts
            login_attempts = re.findall(r'Failed password for', logs)
            if len(login_attempts) > 3:
                print("Event Correlation: Multiple failed login attempts detected.")
            
    except Exception as e:
        print(f"Error correlating events: {e}")

def main():
    # Schedule tasks
    schedule.every(1).minute.do(capture_system_logs)  # Capture system logs every minute
    schedule.every(5).minutes.do(correlate_events)    # Correlate events every 5 minutes

    print("Starting system log capturing and event correlation...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

