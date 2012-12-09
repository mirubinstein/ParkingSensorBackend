This directory contains the four main items for the backend, including:
1. BaseStation: Installed on a TelosB, which acts as the basestation for the transponders and the magnetometers.
2. Oscilloscope: Contains the python file needed to run on the server in order to read from the basestation and write the readings to an XML file, which is read by the frontend.
3. OscilloscopeMag: Installed on a MicaZ, works with the magnetometer sensor and sends the readings to the basestation.
4. OscilloscopeTrans: Installed on a TelosB, works as the transponder to send a unique identifier to the basestation to identify the car being used.

The install / how to run information is in each of the folders for each application.
