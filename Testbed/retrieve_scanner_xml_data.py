from IBKR_Tools import file_utils as fu
from Testbed.IBKR_Tools import constants
from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class GetScannerDataApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        self.reqScannerParameters()

    def scannerParameters(self, scanner_params_xml_data: str):
        output_file_path = constants.FILE_PATH

        fu.FileUtils.writeToFile(output_file_path, scanner_params_xml_data)
        fu.FileUtils.confirmData(output_file_path)

        self.disconnect()


scannerDataApp = GetScannerDataApp()
scannerDataApp.connect(constants.LOCALHOST_IP, constants.IB_GATEWAY_PORT, constants.DEFAULT_CLIENT_ID)
scannerDataApp.run()
