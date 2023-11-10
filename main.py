from create import insert
from read import read 
from update import update
from delete import delete

obj = insert()
objread = read()
objupdate= update()
objdelete=delete()


print("----------bank management System---------------")
print("for inserting the data press 1:")
print("for Reading the data press 2:")
print("for updating the data press 3:")
print("for deleting the data press 4:")

opr=int(input("please enter your operation:"))

def myopr():
    print("------for personal_details press 1-------")
    print("------for bank_details press 2-----------")
    print("------for transaction_details press 3----")
    print("------for account_details press 4--------")
    vr=int(input("please select your table:"))
    if vr==1:
        return 'personal_details'
    elif vr==2:
        return 'bank_details'
    elif vr==3:
        return 'transaction_details'
    elif vr==4:
        return 'account_details'
    
if opr ==1:
    h=myopr()
    if h=='personal_details':
        cid=int(input("please enter customer id:"))
        fname=input("please enter customer first name:")
        lname=input("please enter customer last name:")
        addr=(input("please enter customer address:"))
        pn=int(input("please enter customer phone number:"))
        an=input("please enter customer aadhar number:")
        pan=input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)

    elif h=="bank_details":
        acn=int(input("please enter account number:"))
        cid=int(input("please enter customerid:"))
        ifsc=input("please enter ifsc code:")
        actype=input("please eneter account type:")
        obj.bank_details(acn,cid,ifsc,actype)

    elif h=="transaction_details":
        trnsid=int(input("please enter your transaction id:"))
        sacc=int(input("please enter sender accout:"))
        racc=int(input("please enter receiver account:"))
        amt=int(input("please enter amount:"))
        method=input("please enter payment method:")
        obj.transaction_details(trnsid,sacc,racc,amt,method)

    elif h=="account_details":
        acn=int(input("please enter account number"))
        trnsid= int(input("please enter transaction id:"))
        amt=int(input("please enter amount:"))
        clsngbal=int(input("please enter the closing balance:"))
        obj.account_details(acn,trnsid,amt,clsngbal) 

if opr==2:   # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)

if opr==3:
    j=myopr()
    cusid=int(input("please enter customer id for fetching data"))
    colname=input("please enter column name:")
    newval=input("please enter new values:")   #500  #'jhon'
    objupdate.myupdate(j,colname,newval,cusid)
    
if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to delete the data: "))
    objdelete.specific_del(k,cusid)    






