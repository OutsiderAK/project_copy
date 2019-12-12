import firebase_admin
from firebase_admin import credentials, firestore


class WebScraperCAddToDatabase:

    def __init__(self, price_dict):
        self.name = price_dict["name"]
        self.ticker = price_dict["ticker"]
        self.price = price_dict["price"]
        self.real_date = price_dict["real_date"]
        self.real_time = price_dict["real_time"]
        self.scrape_date = price_dict["scrape_date"]
        self.scrape_time = price_dict["scrape_time"]
        self.time_delta = price_dict["time_delta"]

        cred = credentials.Certificate('./keyToDatabase.json')
        # needed to initialize the SDK DO NOT remove
        default_app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_document(self):

        doc_ref = self.db.collection(u'Firmy/'+self.name+"/Price").document()
        doc_ref.set({
            u'name': self.name,
            u'ticker': self.ticker,
            u'price': self.price,
            u'real_date': self.real_date,
            u'real_time': self.real_time,
            u'scrape_date': self.scrape_date,
            u'scrape_time': self.scrape_time,
            u'time_delta': self.time_delta,
        })

"""
CDR_DATA = {"name": "CDPROJEKT",
            "ticker": "CDR",
            "price": 251,
            "real_date": "12/11/2019",
            "real_time": "15:21",
            "scrape_date": "12/12/2019",
            "scrape_time": "15:49",
            "time_delta": 28}

webScraperC = WebScraperCAddToDatabase(CDR_DATA)
webScraperC.add_document()
"""