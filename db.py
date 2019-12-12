import sqlite3

conn = sqlite3.connect('battery.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE BATTERY
         (CHARGE_STATUS TEXT,
         CHARGE_LEVEL TEXT,
         CURRENT TEXT,
         REMAINING_CAP TEXT,
         VOLTAGE TEXT,
         HEALTH_LEVEL TEXT,
         CURRENT_AV TEXT,
         BATTERY_POWER TEXT,
         CELL_TEMP TEXT);''')

print("Table created successfully");

conn.close()