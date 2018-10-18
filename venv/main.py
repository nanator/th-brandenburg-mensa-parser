#Author: Allan Fodi

rom mensa_parser import MensaParser
from datetime import datetime

def main():
    url = "https://www.studentenwerk-potsdam.de/essen/unsere-mensen-cafeterien/detailinfos/?tx_typoscriptrendering%5Bcontext%5D=%7B%22record%22%3A%22pages_66%22%2C%22path%22%3A%22tt_content.list.20.ddfmensa_ddfmensajson%22%7D&tx_ddfmensa_ddfmensajson%5Bmensa%5D=38&cHash=0843fa029901bdfc0e76d8f31eee7f56"
    mparser = MensaParser(url)
    angebot = mparser.get_offer_for_date(datetime.now())

    for x,y in angebot.items():
        print(x + ": " + y)

    print(mparser.is_open())

if __name__ == "__main__":
    main()