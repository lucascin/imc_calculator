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


| ID | Title | Pre-Conditions | Steps |
|--------|-----------|--------------|----------------------------|
| TCD001 | Checks Dynamic Speed (True) | Configured C environment with the Unity test framework. | <p style="margin-bottom: 0 !important"><b>Step 1.</b> Assign the value of 2.123 to the spd variable.</p><p style="margin-bottom: 0 !important"><b>Step 2.</b> Insert a call to the function CheckSpeed(spd).</p><p style="margin-bottom: 0 !important"><b>Step 3.</b> Checks if the returned value from the CheckSpeed function is equals to 1.</p> |


| ID | Title | Pre-Conditions | 
|--------|-----------|--------------|
| TCD002 | Checks Dynamic Speed (False) | Configured C environment with the Unity test framework. | 
<p><b>Step 1.</b> Assign the value of 6.123 to the spd variable.</p>
<p></p><b>Step 2.</b> Insert a call to the function CheckSpeed(spd).</p>
<p></p><b>Step 3.</b> Checks if the returned value from the CheckSpeed function is equals to 0.</p>

<table border="1">
  <tr>
    <th>ID</th>
    <th>Title</th>
    <th>Pre-Conditions</th>
  </tr>
  <tr>
    <td>TCD001</td>
    <td>Checks Dynamic Speed True</td>
    <td>C Environment configured with Unity test framework</td>
  </tr>
  <tr>
    <th colspan="3">Steps</th>
  </tr>
  <tr>
    <td>Step 1.</td>
    <td>Assign the value of 2.123 to the spd variable.</td>
    <td>Variable saved</td>
  </tr>
  <tr>
    <td>Step 2.</td>
    <td>Insert a call to the function CheckSpeed(spd).</td>
    <td>Function works fine</td>
  </tr>
  <tr>
    <td>Step 3.</td>
    <td>Checks if the returned value from the CheckSpeed function is equals to 1.</td>
    <td>Returned the correct value</td>
  </tr>
  <tr>
    <th colspan="3">Expected Results</th>
  </tr>
</table>

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
