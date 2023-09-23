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
### [TCD001] Checks Dynamic Speed (True)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declare the spd variable of type float.</p></p>
<p><b>Steps:</b> <p>Step 1. Assign the value of 2.123 to the spd variable.</p><p>Step 2. Insert a call to the function CheckSpeed(spd).</p><p>Step 3. Checks if the returned value from the CheckSpeed functin is equals to 1.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The speed value is saved on the spd variable.</p><p>Step 2. The CheckSpeed function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the CheckSpeed function being equals to 1.</p><p>

### [TCD002] Checks Dynamic Speed (False)
<p><b>Pre-Conditions:</b> <p>Configured C environment with the Unity test framework.</p><p>Declare the spd variable of type float.</p></p>
<p><b>Steps:</b> <p>Step 1. Assign the value of 6.123 to the spd variable.</p><p>Step 2. Insert a call to the function CheckSpeed(spd).</p><p>Step 3. Checks if the returned value from the CheckSpeed functin is equals to 0.</p></p>
<p></p><b>Expected results:</b><p>Step 1. The speed value is saved on the spd variable.</p><p>Step 2. The CheckSpeed function is called with no problems.</p><p>Step 3. The test passes due to the returned value by the CheckSpeed function being equals to 0.</p><p>

## Hardware Test Suit
TCH001 -
## Power Test Suit
TCP001 -
## Safety Test Suit
TCS001 -
## Warnings Test Suit
TCW001 -
## Wellbeing Test Suit
TCWB001 - 
