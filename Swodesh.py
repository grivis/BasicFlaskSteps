from flask import Flask
from flask import url_for, render_template, request, redirect
import pickle

app = Flask(__name__)

swlst = ['грудь','сердце','печень','пить','кушать','кусать','видеть','слышать','знать','спать','умирать',
         'убивать','плавать', 'летать','гулять','приходить','лежать','сидеть','стоять', 'дать']

@app.route('/')
def form():
    swdic = {}
    if request.args:
        swdic['name'] = request.args['name']
        swdic['language'] = request.args['language']
        swdic[swlst[0]] = request.args['wrd0']
        swdic[swlst[1]] = request.args['wrd1']
        swdic[swlst[2]] = request.args['wrd2']
        swdic[swlst[3]] = request.args['wrd3']
        swdic[swlst[4]] = request.args['wrd4']
        swdic[swlst[5]] = request.args['wrd5']
        swdic[swlst[6]] = request.args['wrd6']
        swdic[swlst[7]] = request.args['wrd7']
        swdic[swlst[8]] = request.args['wrd8']
        swdic[swlst[9]] = request.args['wrd9']
        swdic[swlst[10]] = request.args['wrd10']
        swdic[swlst[11]] = request.args['wrd11']
        swdic[swlst[12]] = request.args['wrd12']
        swdic[swlst[13]] = request.args['wrd13']
        swdic[swlst[14]] = request.args['wrd14']
        swdic[swlst[15]] = request.args['wrd15']
        swdic[swlst[16]] = request.args['wrd16']
        swdic[swlst[17]] = request.args['wrd17']
        swdic[swlst[18]] = request.args['wrd18']
        swdic[swlst[19]] = request.args['wrd19']
        f = open('swadesh.dic', 'wb')
        pickle.dump(swdic, f)
        f.close()
        return render_template('thanks.html')
    return render_template('swform.html', sw0=swlst[0], sw1=swlst[1],sw2=swlst[2],sw3=swlst[3],sw4=swlst[4],
                           sw5=swlst[5],sw6=swlst[6],sw7=swlst[7],sw8=swlst[8],sw9=swlst[9],sw10=swlst[10],
                           sw11=swlst[11],sw12=swlst[12],sw13=swlst[13],sw14=swlst[14],
                           sw15=swlst[15], sw16=swlst[16], sw17=swlst[17], sw18=swlst[18], sw19=swlst[19])


if __name__ == '__main__':
    app.run(debug=True)