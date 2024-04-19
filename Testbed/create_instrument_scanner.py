from IBKR_Tools import print_utils as pu
from Testbed.IBKR_Tools import constants
from ibapi.client import EClient
from ibapi.scanner import ScannerSubscription
from ibapi.tag_value import *
from ibapi.wrapper import EWrapper


class CreateInstrumentScanner(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        sub = ScannerSubscription()

        sub.instrument = "STK"
        sub.locationCode = "STK.US.MAJOR"
        sub.scanCode = "TOP_PERC_GAIN"

        scan_options = []
        filter_options = [
            TagValue("volumeAbove", "10000"),
            TagValue("marketCapBelow1e6", "1000"),
            TagValue("priceAbove", '1')
        ]

        self.reqScannerSubscription(orderId, sub, scan_options, filter_options)

    def scannerData(self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        pu.PrintUtils.print_scanner_data_to_console(reqId, rank, contractDetails, distance, benchmark, projection,
                                                    legsStr)

    def scannerDataEnd(self, reqId):
        pu.PrintUtils.print_scanner_data_end()
        self.cancelScannerSubscription(reqId)
        self.disconnect()


scannerApp = CreateInstrumentScanner()
scannerApp.connect(constants.LOCALHOST_IP, constants.IB_GATEWAY_PORT, constants.DEFAULT_CLIENT_ID)
scannerApp.run()
