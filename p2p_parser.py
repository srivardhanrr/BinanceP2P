import requests
import argparse
import json
import sys
import webbrowser


def parser_error(errmsg):
    print("\tEjemplo: \r\npython " + sys.argv[0] + " -p 3000 -m ARS -t SELL [[Usa -h para sabr como usar los parametros]]")
    print("Error: " + errmsg)
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -p 3000 -m INR -t SELL")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-c', '--cantidad', help="Cantidad a vender", required=False, default= "10000")
    parser.add_argument('-f', '--fiat', help='Moneda que quieras obtener (Por defecto: ARS)', required=False, default="INR")
    parser.add_argument('-t', '--tipo', help='Tipo de operacion BUY/SELL (Por defecto: SELL)', required=False, default="SELL")
    return parser.parse_args()


def peticion(fiat, type, quantity):
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    data = {
        "asset": "USDT",
        "countries": [],
        "fiat": fiat,
        "merchantCheck": True,
        "page": 1,
        "payTypes": [],
        "proMerchantAds": False,
        "publisherType": None ,
        "rows": 20,
        "tradeType": type,
        "transAmount":  quantity

    }
    r = requests.post(url, headers=headers, json=data)
    r = json.loads(r.text)
    return r


def print_all_methods(methods):
    all_the_methods = ""
    for i in methods:
        all_the_methods += i+' - '
    return all_the_methods


def processor_petition(r):
    list_of_merchants = []
    for i in r['data']:
        merchant = []
        methods = []
        merchant.append(i['adv']['price'])
        for k in i['adv']['tradeMethods']:
            methods.append(k['tradeMethodName'])
        merchant.append(methods)
        merchant.append(i['advertiser']['nickName'])
        merchant.append(i['advertiser']['userNo'])
        merchant.append(i['adv']['minSingleTransAmount'])
        list_of_merchants.append(merchant)

    print("MERCHANTS")
    for i in range(len(list_of_merchants)):
        print(f"{i+1}. Price ${list_of_merchants[i][0]}. Limit: {list_of_merchants[i][4]}    Merchants: {list_of_merchants[i][2]}.   Payment Methods: {print_all_methods(list_of_merchants[i][1])}")
    print()
    try:
        choice = int(input("Enter the number (ENTER to exit) : "))-1
        webbrowser.open("https://p2p.binance.com/es/advertiserDetail?advertiserNo="+list_of_merchants[choice][3], new=2, autoraise=True)
    except:
        return


def executor():
    arguments = parse_args()
    fiat = arguments.fiat
    type = arguments.tipo
    quantity = arguments.cantidad
    all_the_merchants = peticion(fiat, type, quantity)
    processor_petition(all_the_merchants)


if __name__ == "__main__":
    executor()
