from IBKR_Tools import confirmation_tools
from Testbed.IBKR_Tools import _constants
from ibapi.client import *
from ibapi.wrapper import *


class GetScannerDataApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        self.reqScannerParameters()

    def scannerParameters(self, xml: str):
        save_to_directory = _constants.TIMESTAMPED_IBKR_SCANNER_XML
        open(save_to_directory, 'w').write(xml)
        confirmation_tools.confirm_data(_constants.TIMESTAMPED_IBKR_SCANNER_XML)
        self.disconnect()


app = GetScannerDataApp()
app.connect(_constants.LOCAL, _constants.IB_GATEWAY_PORT, _constants.GENERAL_CLIENT_ID)
app.run()
