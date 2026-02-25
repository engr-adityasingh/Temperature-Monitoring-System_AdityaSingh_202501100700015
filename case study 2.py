import random
import time

# Accept min and max temperature limits
min_temp = int(input("Enter minimum temperature limit: "))
max_temp = int(input("Enter maximum temperature limit: "))

print("\n--- Temperature Monitoring Started ---\n")

while True:
    # Generate random temperature value
    current_temp = random.randint(min_temp - 10, max_temp + 10)
    
    # Compare with limits and display appropriate message
    if current_temp < min_temp:
        print(f"Temperature: {current_temp}°C → BELOW minimum limit!")
    elif current_temp > max_temp:
        print(f"Temperature: {current_temp}°C → ABOVE maximum limit!")
    else:
        print(f"Temperature: {current_temp}°C → Within safe range")
    
    # Wait for 2 seconds before next reading
    time.sleep(2)
