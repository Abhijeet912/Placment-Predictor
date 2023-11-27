from flask import Flask,request,render_templete
import pickle

#unpickle the model
file=open('campusplacementpredictor.pkl','rb')
rf=pickle.load(file)
file.close()


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        mydict=request.form
        gender=int(mydict['gender'])
        spec=int(mydict['spec'])
        tech=int(mydict['tech'])
        work=int(mydict['work'])
        ssc=float(mydict['ssc'])
        hsc=float(mydict['hsc'])
        dsc=float(mydict['dsc'])
        mba=float(mydict['mba'])
        inputfeatures=[[gender,spec,tech,work,ssc,hsc,dsc,mba]]
            