import firebase_admin
from firebase_admin import credentials, firestore


class WebScraperCAddToDatabase:

    def __init__(self):

        cred = credentials.Certificate('./keyToDatabase.json')
        # needed to initialize the SDK DO NOT remove
        default_app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_document(self, data):

        self.name = data[0]
        self.ticker = data[1]
        self.price = data[2]
        self.real_date = data[3]
        self.real_time = data[4]
        self.scrape_date = data[5]
        self.scrape_time = data[6]
        self.time_delta = data[7]

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

        self.add_newest()

    def add_newest(self):
        doc_ref = self.db.collection(u'Firmy/'+self.name+"/Newest").document("newest")
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

    def add_error(self):
        doc_ref = self.db.collection(u'Firmy/' + self.name + "/Error").document()
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
"""
"""
CDR_DATA = ["AMBRA", "CDR", 251, "12/11/2019", "15:21", "12/12/2019", "15:49", 28]

webScraperC = WebScraperCAddToDatabase()
webScraperC.add_document(CDR_DATA)
"""