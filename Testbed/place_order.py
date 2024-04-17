import IBKR_Tools.instrument_details as i_details
from ibapi.client import *
from ibapi.wrapper import *


def increment(self):
    self.callBackCounter += 1  # used to track callbacks ten in all



class PlaceSimpleOrderApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.callBackCounter = 1

    # this callback nextValidId is called when api calls function reqIds  in EClient class, or when  initial 4
    # interaction is complete
    def nextValidId(self, orderId: int):
        print(f"nextValidId call = {self.callBackCounter}")
        my_contract = i_details.stockContractApple(Contract())
        increment(self)
        self.reqContractDetails(orderId, my_contract)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(f"""contractDetails call = {self.callBackCounter}
        Contract details: {contractDetails.contract}""")
        increment(self)

        my_order = Order()
        my_order.orderId = reqId  # EDIT submitted order? Swap this to actual returned orderId
        my_order.action = "SELL"
        my_order.tif = "GTC"  # Day order is default
        my_order.orderType = "LMT"
        my_order.lmtPrice = 160.99
        my_order.totalQuantity = 10

        # Edit submitted order? Swap reqId with actual returned orderId
        self.placeOrder(reqId, contractDetails.contract, my_order)

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

    # will callback for every separate necesssary execution:
    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"""
        
        ******{self.callBackCounter}_EXEC_DETAILS******
        execDetails. reqId: {reqId},
        contract: {contract},
        execution: {execution}
""")
        # self.disconnect()


app = PlaceSimpleOrderApp()
app.connect("127.0.0.1", 4002, 1000)
app.run()
