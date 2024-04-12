#### Streaming Data info:
https://interactivebrokers.github.io/tws-api/top_data.html
#### Historical Data
https://interactivebrokers.github.io/tws-api/historical_data.html

#### CustomTkinter

https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/complex_example.py
https://customtkinter.tomschimansky.com/documentation/

### Connect() is unsuccessful and error: 'No connection could be made because the target machine actively refused it 127.0.0.1:7496' is received. Possible reasons are:
TWS is running but the setting 'Enable ActiveX and Socket Clients' is not checked and TWS was launched in a paper session so its default socket port is 7497 instead of 7496. Correct.

### Running multiple instances of TWS and/or IB Gateway on the same computer requires:
A different username for each instance of a running trading application (TWS/IB Gateway/WebTrader/Client Portal/IBKR mobile) and A different socket port for each instance of TWS/IB Gateway. Correct.

### What is the function of the run() loop in the Python API?
The run loop removes messages from the queue and calls the associated callback functions. Correct.

### How many threads are in the Python sample Program.py?
Two: One thread for sending outgoing messages and processing messages in the queue, and one for filling the queue with messages from the socket. Correct.
### Orders can be placed immediately after calling connect().
No, a brief pause is often necessary, the end of which is best indicated by other callback functions which are automatically invoked. Correct.