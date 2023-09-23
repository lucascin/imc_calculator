# Start/Stop System Test Suites Documentation

The Start/Stop system has 6 test suites that aim to test specific parts of the system. 
In this document, the suites and their respective test cases will be listed identified with tags for each tested part.
Every Test Case is identified with the 'TC' tag followed by a letter that identifies for which suite it belongs. Below there is a table with the letters from each suite identified. After the table, there will be listed the TC's with their identifiers.

| Suite Name | Suite Letter |
|----------------------|----------------------|
| Dynamics Test Suite  | D  | 
| Hardware Test Suite  | H  | 
| Power Test Suite  | P  | 
| Safety Test Suite  | S  | 
| Warnings Test Suite  | W  | 
| Wellbeing Test Suite  | WB  | 

## Dynamics Test Suit
### [TCD001] Dynamic Speed Check (True)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared spd variable of type float.</p></p>
<p><b>Steps:</b> <p>Step 1. Assign the value of 2.123 to the spd variable.</p><p>Step 2. Insert a call to the function checkSpeed().</p><p>Step 3. Checks if the returned value from the checkSpeed functin is equal to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The speed value is saved on the spd variable.</p><p>Step 2. The checkSpeed function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkSpeed function is equal to 1.</p><p>

### [TCD002] Dynamic Speed Check (False)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared spd variable of type float.</p></p>
<p><b>Steps:</b> <p>Step 1. Assign the value of 6.123 to the spd variable.</p><p>Step 2. Insert a call to the function CheckSpeed().</p><p>Step 3. Checks if the returned value from the CheckSpeed functin is equal to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The speed value is saved on the spd variable.</p><p>Step 2. The CheckSpeed function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the CheckSpeed function being equal to 0.</p><p>

### [TCD003] Check Brake (True)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared time_test variable of type short int.</p><p>Declared t variable of type unsigned char.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the time_test variable with the 0 value.</p><p>Step 2. Insert a call to the function checkBrake() passing the t parameter and the time_test respectively.</p><p>Step 3. Checks if the returned value from the checkBrake function is equal to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The time in the beginning of the test execution is saved on the time_test variable.</p><p>Step 2. The CheckBrake function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkBrake function is equal to 0.</p><p>

### [TCD004] Check Brake (True 2)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared time_test variable of type short int.</p><p>Declared t variable of type unsigned char.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the time_test variable with the 10 value.</p><p>Step 2. Insert a call to the function checkBrake() passing the t parameter and the time_test respectively.</p><p>Step 3. Checks if the returned value from the checkBrake function is equal to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The time in the beginning of the test execution is saved on the time_test variable.</p><p>Step 2. The CheckBrake function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkBrake function is equal to 0.</p><p>

### [TCD005] Check Brake (False)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared time_test variable of type short int.</p><p>Declared f variable of type unsigned char.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the time_test variable with the 0 value.</p><p>Step 2. Insert a call to the function checkBrake() passing the f parameter and the time_test respectively.</p><p>Step 3. Checks if the returned value from the checkBrake function is equal to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The time in the beginning of the test execution is saved on the time_test variable.</p><p>Step 2. The CheckBrake function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkBrake function being equal to 0.</p><p>

### [TCD006] Check Brake (False 2)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declared time_test variable of type short int.</p><p>Declared f variable of type unsigned char.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the time_test variable with the 10 value.</p><p>Step 2. Insert a call to the function checkBrake() passing the f parameter and the time_test respectively.</p><p>Step 3. Checks if the returned value from the checkBrake function is equal to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The time in the beginning of the test execution is saved on the time_test variable.</p><p>Step 2. The CheckBrake function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkBrake function is equal to 0.</p><p>
  
## Hardware Test Suit
### [TCH001] Check Hardware (True)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize all the sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state) with the 1 value.</p><p>Step 2. Insert a call to the function checkHardware()</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with the value 1.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>

### [TCH002] Check Hardware (True 2)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) and the air_cond_sensor_state with the 1 value and 0 to the remaining sensors (hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH003] Check Hardware (True 3)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) and the seatbelt_sensor_state with the 1 value and 0 to the remaining sensors (hood_sensor_state, trunk_sensor_state, door_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH004] Check Hardware (True 4)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) and the door_sensor_state with the 1 value and 0 to the remaining sensors (hood_sensor_state, trunk_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH005] Check Hardware (True 5)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) and the trunk_sensor_state with the 1 value and 0 to the remaining sensors (hood_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH006] Check Hardware (True 6)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) and the hood_sensor_state with the 1 value and 0 to the remaining sensors (trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH007] Check Hardware (True 7)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state), the hood_sensor_state and the air_cond_sensor_state with the 1 value and 0 to the remaining sensors (trunk_sensor_state, door_sensor_state, seatbelt_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>

### [TCH008] Check Hardware (True 8)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state), the hood_sensor_state and the seatbelt_sensor_state with the 1 value and 0 to the remaining sensors (trunk_sensor_state, door_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>

### [TCH009] Check Hardware (True 9)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state), the hood_sensor_state and the door_sensor_state with the 1 value and 0 to the remaining sensors (trunk_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH010] Check Hardware (True 10)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the mandatory sensors state variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state), the hood_sensor_state and the trunk_sensor_state with the 1 value and 0 to the remaining sensors (door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH011] Check Hardware (True 11)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the door_sensor_state and seatbelt_sensor_state variables with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH012] Check Hardware (True 12)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the door_sensor_state and air_cond_sensor_state variables with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, seatbelt_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH013] Check Hardware (True 13)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the seatbelt_sensor_state and air_cond_sensor_state variables with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH014] Check Hardware (True 14)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the seatbelt_sensor_state variable with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>

### [TCH015] Check Hardware (True 15)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the air_cond_sensor_state variable with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 1.</p><p>
  
### [TCH016] Check Hardware (False)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the speed_sensor_state variable with the 0 value and 1 to the remaining sensors (brake_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>
  
### [TCH017] Check Hardware (False 2)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the brake_sensor_state variable with the 0 value and 1 to the remaining sensors (speed_sensor_state, eng_temp_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>
  
### [TCH018] Check Hardware (False 3)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the eng_temp_sensor_state variable with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, battery_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>

### [TCH019] Check Hardware (False 4)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize the battery_sensor_state variable with the 0 value and 1 to the remaining sensors (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>
  
### [TCH020] Check Hardware (False 5)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize mandatory sensors variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) with the 1 value and 0 to the remaining sensors (hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>
  
### [TCH021] Check Hardware (False 6)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p></p>
<p><b>Steps:</b> <p>Step 1. Initialize mandatory sensors variables (speed_sensor_state, brake_sensor_state, eng_temp_sensor_state, battery_sensor_state) with the 0 value and 1 to the remaining sensors (hood_sensor_state, trunk_sensor_state, door_sensor_state, seatbelt_sensor_state, air_cond_sensor_state).</p><p>Step 2. Insert a call to the function checkHardware().</p><p>Step 3. Checks if the returned value from the checkHardware function is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The sensor state variables are stored with their respective detailed values.</p><p>Step 2. The CheckHardware function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the checkHardware function is equal to 0.</p><p>

## Power Test Suit
TCP001 -
## Safety Test Suit
TCS001 -
## Warnings Test Suit
TCW001 -
## Wellbeing Test Suit
TCWB001 - 
