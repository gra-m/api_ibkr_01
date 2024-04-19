class PrintUtils:
    print_call_count = 0

    @classmethod
    def increment(cls):
        cls.print_call_count += 1

    @classmethod
    def print_scanner_data_to_console(cls, reqId, rank, contract_details, distance, benchmark, projection, legsStr):
        cls.increment()
        print(
            f'(********************{cls.print_call_count}.scannerData Start**********************'
            f'ReqId: {reqId}\nRank: {rank}\nContractDetails: {contract_details}\nDistance: {distance}\nBenchmark: '
            f'{benchmark}\nProjection: {projection}\nLegsStr: {legsStr}')

    @classmethod
    def print_scanner_data_end(cls):
        cls.increment()
        print(
            f'>>>>>>>>>>>>>>>>>>>>>>>{cls.print_call_count}.scannerData End<<<<<<<<<<<<<<<<<<<<<<<<'
        )
