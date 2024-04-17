#  API pacing == 50 messages sent and received per second LIMIT
#  reqMktData -> aggregate real time data streamed sev times per s
#  reqMarketDataType(1) -> top of book live market data
#  reqMarketDataType(2) -> frozen data eg. at close
#  reqMarketDataType(3) -> Delayed Data (For use if there is no live subscription)
#  reqMarketDataType(4) -> Frozen Delayed Data (e.g delayed data for yesterday's close even without live
#  data subscription )
#  reqHistoricalData -> historical data bars through the api as with TWS bar-charts
#  reqTickByTickData -> provides every individual tick on request, a mirror of TWS 'Time and Sales'  windows
#  reqRealTimeBars reqMktDepth reqHistoricalTicks
#  reqHistogramData

import IBKR_Tools.instrument_details as i_details
from ibapi.client import *
from ibapi.wrapper import *


def marketDataPlease(self, orderId: int, contract):
    # regulatory snapshot = incur one time fee
    # empty list as data not being passed on
    self.reqMarketDataType(4)
    self.reqMktData(orderId, contract, "", True, False, [])


def historicDataPlease(self, orderId: int, contract):
    self.reqHistoricalData(orderId, contract, "20221010 15:00:00 US/Eastern", "1 D", "1 hour", "TRADES", False, True, False, [])


class MarketDataRequestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.historic = False

    # auto create new orderId for each request distinct data and order requests
    def nextValidId(self, orderId: int):

        if self.historic:
            contract = i_details.stockContractApple(
                Contract())  # no market data permissions for ISLAND STK needs 'Market Data Connections'
            # contract = i_details.optionsRequestApple(Contract())  # !200 no security definition has been found for the request
            # contract = i_details.futuresRequestDAX(Contract()) # time zone invalid
            print("GETTING HISTORIC DATA")
            historicDataPlease(self, orderId, contract)
        else:
            contract = i_details.stockContractApple(Contract())  # OK Delayed
            # contract = i_details.optionsRequestApple(Contract()) # !200 no security definition has been found for the request
            # contract = i_details.futuresRequestDAX(Contract()) # OK Delayed
            print("GETTING MARKET DATA")
            marketDataPlease(self, orderId, contract)


    def tickPrice(self, reqId, tickType, price, attrib):
        print(
            f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")

    def tickSize(self, reqId, tickType, size):
        print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")

    def historicalData(self, reqId, bar):
        print(f"Historical Data: {bar}")

    def historicalDataEnd(self, reqId, start, end):
        print(f"End of HistoricalData")
        print(f"Start: {start}, End: {end}")


app = MarketDataRequestApp()
app.connect("127.0.0.1", 4002, 1000)
app.run()
