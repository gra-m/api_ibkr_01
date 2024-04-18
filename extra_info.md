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

### An API Contract object

can be defined in multiple ways to specify the same instrument in IB's database AND must match a single financial
instrument that is tradable at IB to use with functions such as placeOrder or reqMktData.

### If a very large amount of historical data is requested from the API,

data may be throttled and returned more slowly as more requests are made. Correct.

### The last available bid/ask values after market close:

can be returned by first switching to a different data mode with reqMarketDataType.

### True or False: It is important to note that for both live and historical market data, your account must have an active market data subscription for the relevant account. You can subscribe to these market data subscriptions in client portal.

True

### Interactive Brokers TWS API has a pacing limitation of ___ messages per second.

50

### True or False: Like TWS, if we do not have any market data subscriptions, we are able to use reqMktData request to receive delayed data.

True

## PLACING ORDERS

### Before attempting to place a new order type in the API, it is recommended to:

Try to find the exact combination of security type, order type, and order attributes in the documentation AND First try
the order in a paper account if possible.

### Orders placed through TWS, the API, or IBKR mobile usually have different commissions:

False

### An API client receives status and execution updates about orders:

Placed from the same API client ID automatically AND from all orders automatically if it is set as the Master Client ID

### To modify an open order placed from TWS:

The order can be modified from the API using the modifyOrder function

### What is the limit on the number of function calls (including orders) per second from the API?

50 outgoing messages/second.

# COMPLEX ORDERS

### Which secType indicates that I am using a combo order to the system?

BAG

### Where can I view my open orders and executions in TWS Desktop?

Activity Panel 



