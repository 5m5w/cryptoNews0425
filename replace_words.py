import re

replace_words = {'比特幣':' #比特幣 ', '以太幣':' #以太幣 ','以太坊':' #以太坊 ','昇級':'升級','製度':'制度','鍊':'鏈','智能':'智慧','渠道':'管道','匝道':'管道', 'SEC':' #SEC ', 'Bankless': ' @BanklessHQ ','Coinbase':' @coinbase ', 'Kraken':' @Krakenfx ','Bitcoin':' #Bitcoin ','Ethereum':' #Ethereum ' ,'arbitrum':' #arbitrum ', 'optimism':' #optimism ', 'ETH':' $ETH ', 'BTC':' $BTC ','arb':' $arb ', 'BNB':' $BNB ','XRP':' $BNB ', 'ADA':' $ADA ', 'MATIC':' $MATIC ', 'DOGE':' $DOGE ', 'SOL':' $SOL ','DOT': ' $DOT ','USDC': ' $USDC ','USDT':' $USDT ','DAI':' $DAI ' ,'BUSC':' $BUSD ', 'PEPE':' $PEPE '}

def replacement_func(p):
    for word, replacement in replace_words.items():
        pattern = re.compile(word)
        result = pattern.sub(replacement, p)
        p = result
    return result