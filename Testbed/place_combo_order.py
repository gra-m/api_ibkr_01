from ibapi.client import *
from ibapi.contract import ComboLeg
from ibapi.tag_value import TagValue
from ibapi.wrapper import *


def increment(self):
    self.callBackCounter += 1  # used to track callbacks ten in all


class PlaceComboOrderApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.callBackCounter = 1
        print("self created")

    def nextValidId(self, orderId: int):
        print(f"nextValidId call = {self.callBackCounter}")
        my_contract = Contract()
        my_contract.symbol = "AAPL,TSLA"
        my_contract.secType = "BAG"  # 321 Error validating request bQ BAG is not supported for contract data request
        my_contract.exchange = "SMART"
        my_contract.currency = "USD"

        leg1 = ComboLeg()
        leg1.conId = 76792991
        leg1.ratio = 1
        leg1.action = "BUY"
        leg1.exchange = "SMART"

        leg2 = ComboLeg()
        leg2.conId = 265598
        leg2.ratio = 1
        leg2.action = "SELL"
        leg2.exchange = "SMART"

        my_contract.comboLegs = []
        my_contract.comboLegs.append(leg1)
        my_contract.comboLegs.append(leg2)
        self.reqContractDetails(orderId, my_contract)

        my_order = Order()
        my_order.orderId = orderId
        my_order.action = "BUY"
        my_order.orderType = "LMT"
        my_order.lmtPrice = 200
        my_order.totalQuantity = 10
        my_order.tif = "GTC"
        my_order.smartComboRoutingParams = []
        my_order.smartComboRoutingParams.append(TagValue('NonGuaranteed', '1'))

        increment(self)
        self.placeOrder(orderId, my_contract, my_order)

    #   def contractDetails(self, reqId: int, contractDetails: ContractDetails):
    # print(f"""contractDetails call = {self.callBackCounter}
    # Contract details: {contractDetails.contract}""")
    # increment(self)

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

    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"""
        
        ******{self.callBackCounter}_EXEC_DETAILS******
        execDetails. reqId: {reqId},
        contract: {contract},
        execution: {execution}
""")
        # self.disconnect()


app = PlaceComboOrderApp()
app.connect("127.0.0.1", 4002, 1000)
app.run()
