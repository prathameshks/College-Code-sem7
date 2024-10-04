import os
import re
from datetime import datetime
import time

# Log sources (simulated for this example)
LOG_SOURCES = {
    'system': 'sys.log',
    'auth': 'auth.log',
    'app': 'app.log'
}
# Event patterns to look for
EVENT_PATTERNS = {
    'failed_login': r'Failed (password|login attempt)',
    'system_error': r'\[ERROR\]',
    'app_crash': r'Application crashed',
    'high_cpu': r'CPU usage detected: \d{2,3}%',
    'disk_space_low': r'Disk usage exceeds \d{2,3}%'
}

class LogCapture:
    def __init__(self, log_dir='captured_logs'):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def capture_logs(self):
        for source, path in LOG_SOURCES.items():
            captured_log = os.path.join(self.log_dir, f'{source}_log.txt')
            # In a real scenario, you'd use 'shutil.copy2(path, captured_log)'
            # For this example, we'll simulate log content
            with open(captured_log, 'w') as f:
                f.write(self.simulate_log_content(source))
        print("Logs captured successfully.")

    def simulate_log_content(self, source):
        # This method simulates log content for demonstration purposes
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if source == 'system':
            return f"{current_time} [INFO] System started\n{current_time} [ERROR] Disk space low\n"
        elif source == 'auth':
            return f"{current_time} [INFO] User login successful\n{current_time} [WARN] Failed login attempt\n"
        elif source == 'app':
            return f"{current_time} [INFO] Application started\n{current_time} [ERROR] Application crashed\n"

class EventCorrelator:
    def __init__(self, log_dir):
        self.log_dir = log_dir

    def correlate_events(self):
        all_events = []
        for source, path in LOG_SOURCES.items():
            captured_log = os.path.join(self.log_dir, f'{source}_log.txt')
            with open(captured_log, 'r') as f:
                content = f.read()
                for event_type, pattern in EVENT_PATTERNS.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        all_events.append({
                            'timestamp': self.extract_timestamp(content[:match.start()]),
                            'source': source,
                            'event_type': event_type,
                            'message': match.group()
                        })

        # Sort events by timestamp
        all_events.sort(key=lambda x: x['timestamp'])

        # Perform basic correlation (e.g., events happening within 5 seconds)
        correlated_events = self.find_correlated_events(all_events)

        return correlated_events

    def extract_timestamp(self, text):
        # Extract the last timestamp found in the text
        matches = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', text)
        return matches[-1] if matches else ''

    def find_correlated_events(self, events, time_window=5):
        correlated = []
        for i, event in enumerate(events):
            related = [event]
            for other_event in events[i+1:]:
                if (datetime.strptime(other_event['timestamp'], '%Y-%m-%d %H:%M:%S') - 
                    datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S')).seconds <= time_window:
                    related.append(other_event)
                else:
                    break
            if len(related) > 1:
                correlated.append(related)
        return correlated

def main():
    log_capture = LogCapture()
    log_capture.capture_logs()

    time.sleep(1)  # Simulate some time passing

    event_correlator = EventCorrelator(log_capture.log_dir)
    correlated_events = event_correlator.correlate_events()

    print("\nCorrelated Events:")
    for event_group in correlated_events:
        print("\nRelated events (within 5 seconds):")
        for event in event_group:
            print(f"  {event['timestamp']} - {event['source']} - {event['event_type']}: {event['message']}")

if __name__ == "__main__":
    main()