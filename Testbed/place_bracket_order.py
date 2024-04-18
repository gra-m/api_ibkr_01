# import IBKR_Tools.instrument_details as i_details
from ibapi.client import *
from ibapi.wrapper import *


# from ibapi.contract import ComboLeg
# from ibapi.tag_value import TagValue


def increment(self):
    self.callBackCounter += 1  # used to track callbacks ten in all


class PlaceBracketOrderApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.callBackCounter = 1

    # this callback nextValidId is called when api calls function reqIds  in EClient class, or when  initial 4
    # interaction is complete
    def nextValidId(self, orderId: int):
        print(f"nextValidId call = {self.callBackCounter}")
        increment(self)
        my_contract = Contract()
        my_contract.symbol = "AAPL"
        my_contract.secType = "STK"
        my_contract.exchange = "SMART"
        my_contract.currency = "USD"

        parent = Order()
        parent.orderId = orderId
        parent.orderType = "LMT"
        parent.lmtPrice = 140.00
        parent.action = "BUY"
        parent.totalQuantity = 10
        parent.transmit = False  # False == do not send! More to come!

        profit_taker = Order()
        profit_taker.parentId = parent.orderId
        profit_taker.orderId = parent.orderId + 1
        profit_taker.action = "SELL"
        profit_taker.orderType = "LMT"
        profit_taker.lmtPrice = 156.20
        profit_taker.totalQuantity = 10
        profit_taker.transmit = False  # False More to come!

        stop_loss = Order()
        stop_loss.parentId = parent.orderId
        stop_loss.orderId = parent.orderId + 2
        stop_loss.ocaType = "STP"
        stop_loss.auxPrice = 136.98
        stop_loss.action = "SELL"
        stop_loss.totalQuantity = 10
        stop_loss.transmit = True  # Transmit True at last order stage orderId + 2

        # Place orders:
        self.placeOrder(parent.orderId, my_contract, parent)
        self.placeOrder(profit_taker.orderId, my_contract, profit_taker)
        self.placeOrder(stop_loss.orderId, my_contract, stop_loss)

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order,
                  orderState: OrderState):
        print(f"""
        *********{self.callBackCounter}_ORDER_OPENED**********
        openOrder. orderId: {orderId},
        contract: {contract},
        order: {order}""")
        increment(self)

    def orderStatus(self, orderId: OrderId, status: str, filled: float, remaining: float, avgFillPrice: float, permId:
    int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print(f"""
        
        ******{self.callBackCounter}_ORDER_STATUS******
        orderStatus. orderId: {orderId},
        status: {status},
        filled: {filled},
        remaining: {remaining},
        avgFillPrice: {avgFillPrice},
        lastFillPrice: {lastFillPrice}
        permId: {permId},
        parentId: {parentId},
        clientId: {clientId},
        whyHeld: {whyHeld},
        mktCapPrice: {mktCapPrice}""")
        increment(self)

    # will callback for every separate necessary execution:
    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"""
        
        ******{self.callBackCounter}_EXEC_DETAILS******
        execDetails. reqId: {reqId},
        contract: {contract},
        execution: {execution}
""")
        # self.disconnect()


app = PlaceBracketOrderApp()
app.connect("127.0.0.1", 4002, 1000)
app.run()
