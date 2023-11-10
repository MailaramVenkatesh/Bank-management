#installed library mysql-connector-pyhton
import mysql.connector

#creating connection

class insert:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="venky.m8688",
                database="bank"
            )
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur=self.conn.cursor()   # creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}','{pn}','{an}','{pan}')")
        self.conn.commit()

    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("----------------------bank details successfully saved:----------------------") 

    def transaction_details(self,trnsid,sacc,racc,amt,method):
        cur=self.conn.cursor() 
        cur.execute(f"insert into transaction_details values({trnsid},{sacc},{racc},{amt},'{method}')")
        self.conn.commit() 
        print("---------transaction details has been saved successfully--------")
        
    def account_details(self,acn,trnsid,amt,clsngbal):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({acn},{trnsid},{amt},{clsngbal})")
        self.conn.commit()
        print("-------account details has been saved successfully------")
        



