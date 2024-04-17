def printInstrumentDetails(contractDetails):

# Note this is not printing Options data when option contract is passed
# used in requestContractDetails.py
    print(f"""
    CONTRACT DETAILS for conId: {contractDetails.contract.conId}
    
    NOTE: You can now use: 
    mycontract = Contract()
    mycontract.conId = {contractDetails.contract.conId}
    for ongoing reference.
    
    {str("marketName:====================")[:30].center(50)} 
    {contractDetails.marketName}
    {str("minTick:====================")[:30].center(50)} 
    {contractDetails.minTick}
    {str("orderTypes:====================")[:30].center(50)} 
    {contractDetails.orderTypes}
    {str("validExchanges:====================")[:30].center(50)} 
    {contractDetails.validExchanges}
    {str("priceMagnifier:====================")[:30].center(50)} 
    {contractDetails.priceMagnifier}
    {str("underConId:====================")[:30].center(50)} 
    {contractDetails.underConId}
    {str("longName:====================")[:30].center(50)} 
    {contractDetails.longName}
    {str("contractMonth:====================")[:30].center(50)} 
    {contractDetails.contractMonth}
    {str("industry:====================")[:30].center(50)} 
    {contractDetails.industry}
    {str("category:====================")[:30].center(50)} 
    {contractDetails.category}
    {str("subcategory:====================")[:30].center(50)} 
    {contractDetails.subcategory}
    {str("timeZoneId:====================")[:30].center(50)} 
    {contractDetails.timeZoneId}
    {str("tradingHours:====================")[:30].center(50)} 
    {contractDetails.tradingHours}
    {str("liquidHours:====================")[:30].center(50)} 
    {contractDetails.liquidHours}
    {str("evRule:====================")[:30].center(50)} 
    {contractDetails.evRule}
    {str("evMultiplier:====================")[:30].center(50)} 
    {contractDetails.evMultiplier}
    {str("aggGroup:====================")[:30].center(50)} 
    {contractDetails.aggGroup}
    {str("underSymbol:====================")[:30].center(50)} 
    {contractDetails.underSymbol}
    {str("underSecType:====================")[:30].center(50)} 
    {contractDetails.underSecType}
    {str("marketRuleIds:====================")[:30].center(50)} 
    {contractDetails.marketRuleIds}
    {str("secIdList:====================")[:30].center(50)} 
    {contractDetails.secIdList}
    {str("realExpirationDate:====================")[:30].center(50)} 
    {contractDetails.realExpirationDate}
    {str("lastTradeTime:====================")[:30].center(50)} 
    {contractDetails.lastTradeTime}
    {str("stockType:====================")[:30].center(50)} 
    {contractDetails.stockType}
    {str("minSize:====================")[:30].center(50)} 
    {contractDetails.minSize}
    {str("sizeIncrement:====================")[:30].center(50)} 
    {contractDetails.sizeIncrement}
    {str("suggestedSizeIncrement:====================")[:30].center(50)} 
    {contractDetails.suggestedSizeIncrement}
    {str("BOND-cusip:=====BOND===============")[:30].center(50)} 
    {contractDetails.cusip}
    {str("ratings:=====BOND===============")[:30].center(50)} 
    {contractDetails.ratings}
    {str("descAppend:=====BOND===============")[:30].center(50)} 
    {contractDetails.descAppend}
    {str("bondType:=====BOND===============")[:30].center(50)} 
    {contractDetails.bondType}
    {str("couponType:=====BOND===============")[:30].center(50)} 
    {contractDetails.couponType}
    {str("callable:=====BOND===============")[:30].center(50)} 
    {contractDetails.callable}
    {str("putable:=====BOND===============")[:30].center(50)} 
    {contractDetails.putable}
    {str("coupon:=====BOND===============")[:30].center(50)} 
    {contractDetails.coupon}
    {str("convertible:=====BOND===============")[:30].center(50)} 
    {contractDetails.convertible}
    {str("maturity:=====BOND===============")[:30].center(50)} 
    {contractDetails.maturity}
    {str("issueDate:=====BOND===============")[:30].center(50)} 
    {contractDetails.issueDate}
    {str("nextOptionDate:=====BOND===============")[:30].center(50)} 
    {contractDetails.nextOptionDate}
    {str("nextOptionType:=====BOND===============")[:30].center(50)} 
    {contractDetails.nextOptionType}
    {str("nextOptionPartial:====BOND===============")[:30].center(50)} 
    {contractDetails.nextOptionPartial}
    {str("notes:=====BOND===============")[:30].center(50)} 
    {contractDetails.notes}
    """)

# todo add options print function


def stockContractApple(contract):
    mycontract = contract
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"
    # mycontract.primaryExchange = "ISLAND"  # nasdaq exchange known as this (disambiguation)

    return mycontract


def optionsRequestApple(contract):
    mycontract = contract
    mycontract.symbol = "AAPL"
    mycontract.secType = "OPT"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"
    # https://www.nasdaq.com/market-activity/stocks/aapl/option-chain
    mycontract.right = "C"  # call
    mycontract.lastTradeDateOrContractMonth = "20240412"     # no exact expiration date
    mycontract.strike = "155"  # strike price
   
    return mycontract


def futuresRequestDAX(contract):
    mycontract = contract
    
    mycontract.symbol = "DAX" # DAX DAX-mini and DAX-micro futures
    mycontract.secType = "FUT"
    mycontract.exchange = "EUREX"
    mycontract.currency = "EUR"
    mycontract.lastTradeDateOrContractMonth = "202406"
    mycontract.multiplier = 1   # specify only one future
    
    return mycontract