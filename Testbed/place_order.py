import IBKR_Tools.instrument_details as i_details
from ibapi.client import *
from ibapi.wrapper import *


class PlaceSimpleOrderApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    # this callback nextValidId is called when api calls function reqIds  in EClient class, or when  initial 4
    # interaction is complete
    def nextValidId(self, orderId: int):
        print("NExtValidID")
        my_contract = i_details.stockContractApple(Contract())
        self.reqContractDetails(orderId, my_contract)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(f"Contract details: {contractDetails.contract}")
        print(contractDetails.contract)

        my_order = Order()
        my_order.orderId = reqId
        my_order.action = "BUY"
        my_order.tif = "GTC"  # Day order is default
        my_order.orderType = "MKT"
        my_order.totalQuantity = 10

        self.placeOrder(reqId, contractDetails.contract, my_order)
        self.disconnect()


app = PlaceSimpleOrderApp()
app.connect("127.0.0.1", 4002, 1000)
app.run()
