import flask
import pandas as pd
import joblib
from lexia import predalt



app = flask.Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        Pelabuhan = flask.request.form['Pelabuhan']
        COVID1 = flask.request.form['COVID_kemarin']
        COVID2 = flask.request.form['COVID_lusa']
        Sosial = flask.request.form['Sosial']
        normal = flask.request.form['normal']

        # rate of covid-19 case change
        COVID = (int(COVID1)-int(COVID2))/int(COVID2)

        dict_test = {'Pelabuhan':Pelabuhan, 'Positivity_rate_val':[COVID],'Sosial':Sosial, 'Retail_recreation':[int(normal)]}

        pred_ = predalt(dict_test)
        print(pred_)

        return flask.render_template('main.html', original_input={'Lokasi Pelabuhan':Pelabuhan, ', Jumlah kasus COVID-19 Lusa':int(COVID2),
                                        ', Jumlah kasus COVID-19 Kemarin':int(COVID1), ', Pembatasan Darurat':Sosial},
                                     result=pred_)


if __name__ == '__main__':
    app.run(debug=True, port=8000)