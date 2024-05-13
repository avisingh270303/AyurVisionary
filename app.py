from distutils.log import debug
import pickle
from flask import Flask , render_template, request
from sklearn.metrics import accuracy_score

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/heart')
def heart():
    return render_template('heartform.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetesform.html')

@app.route('/heartform', methods=['GET','POST'])
def heartform():
    model=pickle.load(open('model.pkl','rb'))
    age = float(request.form.get('age'))
    sex = float(request.form.get('gender'))
    cp = float(request.form.get('chestPain'))
    trestbps = float(request.form.get('trestbps'))
    chol = float(request.form.get('chol'))
    fbs = float(request.form.get('fastingSugar'))
    restecg = float(request.form.get('restecg'))
    thalach = float(request.form.get('thalach'))
    exeng = float(request.form.get('exerciseAngina'))
    oldpeak = float(request.form.get('STDepression'))
    slope = float(request.form.get('slope'))
    ca = float(request.form.get('ca'))
    thal = float(request.form.get('thal'))
    pre = model.predict([[(age),(sex),(cp),(trestbps),(chol),(fbs),(restecg),(thalach),(exeng),(oldpeak),(slope),(ca),(thal)]])
    
    # pre = model.predict([[1,20,15,13,46,78,97,55,84,66,3,12,153]])
    output = round(pre[0],0)
    return render_template('result.html',out=output)

@app.route('/diabetesform', methods=['GET','POST'])
def diabetesform():
    model=pickle.load(open('modelD.pkl','rb'))
    pregnancies = float(request.form.get('pregnancies'))
    glucose = float(request.form.get('glucose'))
    bloodPressure = float(request.form.get('bloodPressure'))
    skinThickness = float(request.form.get('skinThickness'))
    insulin = float(request.form.get('insulin'))
    bmi = float(request.form.get('bmi'))
    diabetesPedigree = float(request.form.get('diabetesPedigree'))
    age = float(request.form.get('age'))
    # print((pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age))
    pre=model.predict([[(pregnancies),(glucose),(bloodPressure),(skinThickness),(insulin),(bmi),(diabetesPedigree),(age)]])
    # pre = model.predict([[1,23,24,15,26,79,48,75]])
    # accu = accuracy_score(pre[0],0)
    output=round(pre[0],0)
    return render_template('result.html',out=output)

@app.route('/parkinson')
def parkinson():
    return render_template('parkinsonform.html')

@app.route('/parkinsonsform', methods=['GET','POST'])
def parkinsonsform():
    model = pickle.load(open('modelP.pkl','rb'))
    prediction=model.predict([[
float(request.form.get('MDVPFo')),
float(request.form.get('MDVPFhi')),
float(request.form.get('MDVPFlo')),
float(request.form.get('MDVPJitter')),
float(request.form.get('MDVPJitterAbs')),
float(request.form.get('MDVPRAP')),
float(request.form.get('MDVPPPQ')),
float(request.form.get('JitterDDP')),
float(request.form.get('MDVPShimmer')),
float(request.form.get('MDVPShimmerdB')),
float(request.form.get('ShimmerAPQ3')),
float(request.form.get('ShimmerAPQ5')),
float(request.form.get('MDVPAPQ')),
float(request.form.get('ShimmerDDA')),
float(request.form.get('NHR')),
float(request.form.get('HNR')),
float(request.form.get('RPDE')),
float(request.form.get('DFA')),
float(request.form.get('spread1')),
float(request.form.get('spread2')),
float(request.form.get('D2')),
float(request.form.get('PPE'))]])
    output=round(prediction[0],2)
    return render_template('result.html', out=output)

if __name__ == '__main__':
    app.run(debug=True)