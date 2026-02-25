# Temperature-Monitoring-System_AdityaSingh_202501100700015

 Problem Statement
- Build a Python program to simulate an IoT system that monitors temperature.
- Accept minimum and maximum temperature limits from the user.
- Generate random temperature values at 2-second intervals to mimic sensor readings.
- Compare each reading with the limits and display appropriate messages:
- Below minimum limit → Warning ❄️
- Above maximum limit → Warning 🔥
- Within safe range → Normal ✅

 Approach
- Input Handling:
- Prompt the user to enter minimum and maximum temperature limits.
- Random Simulation:
- Use Python’s random.randint() to generate temperature values.
- Extend the range slightly beyond the limits to simulate realistic fluctuations.
- Comparison Logic:
- If current_temp < min_temp → Display "BELOW minimum limit".
- If current_temp > max_temp → Display "ABOVE maximum limit".
- Else → Display "Within safe range".
- Loop & Delay:
- Use an infinite loop (while True) to continuously generate readings.
- Add a time.sleep(2) delay to simulate real-time monitoring.

 Sample Output 
Enter minimum temperature limit: 20
Enter maximum temperature limit: 30

--- Temperature Monitoring Started ---

Temperature: 18°C → BELOW minimum limit! 
Temperature: 25°C → Within safe range 
Temperature: 33°C → ABOVE maximum limit! 
Temperature: 22°C → Within safe range 
Temperature: 19°C → BELOW minimum limit! 
