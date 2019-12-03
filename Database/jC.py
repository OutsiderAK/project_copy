import datetime

import firebase_admin
from firebase_admin import credentials, firestore


class AddCompanyToDB(object):

    def __init__(self, name):
        self.name = name

        cred = credentials.Certificate('./keyToDatabase.json')
        defaultApp = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        #self.addDoc()

    def addDoc(self):

        doc_ref = self.db.collection(u'Firmy/'+self.name+"/Price").document()
        doc_ref.set({
            u'mate': "2019.12.3",
            u'fine': "13:01",
        })

        print("Company added successfully\n")

    def read(self):
        users_ref = self.db.collection(u'Firmy/'+str(self.name)+"/Price")
        docs = users_ref.stream()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

    def compoundRead(self):

        x = datetime.datetime(2020, 12, 11, 9, 55)
        price_ref = self.db.collection(u'Firmy/'+str(self.name)+"/Price")
        #query_ref = price_ref.where(u'x', u'<', datetime.datetime.utcnow()).stream()

        query_ref = price_ref.where(u'date', u'==', "2019.12.2").where(u'time', u'==', "10:02").stream()
        for doc in query_ref:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))




#s = AddCompanyToDB("CDR").compoundRead()
#s = AddCompanyToDB("CDR").read()
s = AddCompanyToDB("CDR")
s.addDoc()