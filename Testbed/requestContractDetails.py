from ibapi.client import *
from ibapi.wrapper import *
import time
import instrument_details


class TestApp01(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def contractDetails(self, reqId, contractDetails):
        #print(f"contractDetails: {contractDetails.longName}")
        instrument_details.printInstrumentDetails(contractDetails)

    def contractDetailsEnd(self, reqId):
        print("End of contract Details")                      


def main():
    app = TestApp01()

    app.connect("127.0.0.1", 4002, 1000)
    mycontract = Contract()
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"
    mycontract.primaryExchange = "ISLAND"  # nasdaq exchange known as this disambiguation

    time.sleep(3)  # because computer runs code quicker than socket can be built

    app.reqContractDetails(1, mycontract)
    app.run()  # EWrapper run loop


# outside main loop, call to "name main idiom" to automatically run main method:

if __name__ == "__main__":
    main()
