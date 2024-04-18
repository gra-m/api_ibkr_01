# import IBKR_Tools.instrument_details as i_details
from threading import Timer

from ibapi.client import *
from ibapi.contract import Contract
from ibapi.wrapper import *


# import time # see above

def increment(self):
    self.callCounter += 1  # used to track calls


class AccountInfoApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.callCounter = 0

    def error(self, reqId, errorCode, errorString, advancedOrderReject=""):
        print(f"""
        ****{self.callCounter}_ERROR****
        Error: {reqId},  {errorCode}, {errorString}
        """)
        increment(self)

    def nextValidId(self, orderId):
        self.start()

    def updatePortfolio(self, contract: Contract, position: float, marketPrice: float, marketValue: float,
                        averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
        print(f"""
        ****{self.callCounter}_UPDATE_PORTFOLIO****
        UpdatePortfolio. Symbol: {contract.symbol},
        SecType: {contract.secType},
        Exchange: {contract.exchange},
        Position: {position},
        MarketPrice: {marketPrice},
        MarketValue: {marketValue}, 
        AverageCost: {averageCost}, 
        UnrealizedPNL:{unrealizedPNL}, 
        RealizedPNL: {realizedPNL}, 
        AccountName: {accountName}""")
        increment(self)

    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        print(f"""
        ****{self.callCounter}_UPDATE_ACCOUNT_VALUE****
        UpdateAccountValue. Key: {key},
        Value: {val}, 
        Currency: {currency},
        AccountName: {accountName}""")

    def updateAccountTime(self, timestamp: str):
        print(f"""
        ****{self.callCounter}_UPDATE_ACCOUNT_TIME****
        UpdateAccountTime. Time: {timestamp}
        """)

    def accountDownloadEnd(self, accountName: str):
        print(f"""
        ****{self.callCounter}_ACCOUNT_DOWNLOAD_END****
        AccountDownloadEnd. Account: {accountName}
        """)

    def start(self):
        #   Account number can be omitted when using reqAccountUpdates with single account structure
        self.reqAccountUpdates(True, "")

    def stop(self):
        self.reqAccountUpdates(False, "")
        self.done = True
        self.disconnect()


def main():
    app = AccountInfoApp()
    app.connect("127.0.0.1", 4002, 1000)
    # time.sleep(10) replaced with the below:
    Timer(5, app.stop).start()
    app.run()


# outside main loop, call to "name main idiom" to automatically run main method:

if __name__ == "__main__":
    main()
