import time
import datetime
import winsound

def set_alarm(alarm_time):
    """Set and wait for alarm"""
    try:
        # Parse time in HH:MM format
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")
        print("Waiting for alarm... (Press Ctrl+C to cancel)\n")
        
        while True:
            current_time = datetime.datetime.now()# Check if current time matches alarm time
            if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
                print("\n ALARM! WAKE UP! \n")
                # Play alarm sound
                for _ in range(5):
                    winsound.Beep(1000, 500)
                    time.sleep(0.3)
                
                print("Alarm triggered!")
                break
            
            time.sleep(1)
    
    except ValueError:
        print("Invalid format! Use HH:MM (e.g., 14:30)")
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled.")

if __name__ == "__main__":
    time_input = input("Enter alarm time (HH:MM, e.g., 14:30): ").strip()
    set_alarm(time_input)