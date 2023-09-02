from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Ejecucion en terminal: python -m flask --app Backend run

# Cargar el modelo previamente entrenado
load_model = joblib.load('model_bayes2.pkl')


@app.route("/")
def hello_word():
    return "<p>Hello, World!</p>"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    prediccion = prediction(data)
    return jsonify({'prediction': prediccion.tolist()})


columns = [
    'tip_naci', 'mes_movi', 'dia_movi', 'via_tran', 'mot_viam',
    'AMER_SAMOA', 'ANGUILLA', 'ARUBA', 'BELARUS', 'BENIN', 'BULGARIA',
    'BURKINA_FASO', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA',
    'CAPE_VERDE', 'CAYMAN_IS', 'CENT_AFR_REP', 'CHAD', 'CHILE',
    'CHINA', 'COLOMBIA', 'CONGO', 'COSTA_RICA', 'COTE_DIVOIRE',
    'CROATIA', 'CUBA', 'CYPRUS', 'CZECH_REP', 'DENMARK', 'DJIBOUTI',
    'DOMINICA', 'DOMINICAN_RP', 'D_RP_CONGO', 'EGYPT', 'EL_SALVADOR',
    'EQ_GUINEA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND_IS', 'FIJI', 'FINLAND',
    'FRANCE', 'FR_GUIANA', 'FR_POLYNESIA', 'GABON', 'GAMBIA', 'GEORGIA',
    'GERMANY', 'GHANA', 'GREECE', 'GRENADA', 'GUADELOUPE', 'GUATEMALA',
    'GUINEA', 'GUINEABISSAU', 'GUYANA', 'HAITI', 'HONDURAS', 'HONGKONG_SAR',
    'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND',
    'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
    'KIRIBATI', 'KOREA_NORTE', 'KOREA_SUR', 'KUWAIT', 'KYRGYZTAN', 'LATVIA',
    'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEN', 'LITHUANIA',
    'LUXEMBOURG', 'MADAGASCAR', 'MALASIA', 'MALAWI', 'MALDIVES', 'MALI',
    'MALTA', 'MARSHALL_IS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS',
    'MEXICO', 'MICRONESIA', 'MONACO', 'MONGOLIA', 'MOROCCO', 'MOZAMBIQUE',
    'MYANMAR', 'NAMIBIA', 'NEPAL', 'NETHERLANDS', 'NEW_ZEALAND', 'NICARAGUA',
    'NIGER', 'NIGERIA', 'NORWAY', 'OMAN', 'PAKISTAN', 'PANAMA', 'PAPUA_NGUIN',
    'PARAGUAY', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'PUERTO_RICO',
    'QATAR', 'REP_MOLDOVA', 'ROMANIA', 'RUSSIAN_FED', 'RWANDA', 'SAMOA',
    'SAN_MARINO', 'SAUDI_ARABIA', 'SENEGAL', 'SEYCHELLES', 'SIERRA_LEONA',
    'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOMALIA', 'SOUTH_AFRICA', 'SPAIN',
    'SRI_LANKA', 'ST_KITTS_NEV', 'ST_LUCIA', 'ST_VINCENT_G', 'SUDAN',
    'SURINAME', 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN',
    'TAJIKISTAN', 'TANZANIA', 'TFYROM', 'THAILAND', 'TOGO', 'TRINIDAD_TBG',
    'TUNISIA', 'TURKEY', 'TURKS_CAICOS', 'UGANDA', 'UK', 'UKRAINE',
    'UNTD_ARAB_EM', 'URUGUAY', 'USA', 'USVIRGIN_IS', 'UZBEKISTAN', 'VANUATU',
    'VENEZUELA', 'VIET_NAM', 'YEMEN', 'ZAMBIA', 'ZIMBABWE'
]


def prediction(info):
    mi_diccionario = {}

    for columna in columns:
        if columna == "mot_viam":
            continue
        if columna in info:
            mi_diccionario[columna] = info[columna]
        else:
            mi_diccionario[columna] = 0

    df = pd.DataFrame([mi_diccionario])

    input_data = df.to_numpy()

    return load_model.predict(input_data)
