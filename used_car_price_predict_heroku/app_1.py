# import necessary libraries
from flask import Flask, render_template,jsonify,request
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)



# List of dictionaries
data = [{'Item': 'Item 1',
'cost': 4751,
'lot_time': 126,
'is_over_age': 'YES',
'mileage': 77606,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'BLUE',
'make': 'CHEVROLET',
'state': 'FL',
'make_model': 'CHEVROLET.CAVALIER'},
{'Item': 'Item 2',
'cost': 4274,
'lot_time': 74,
'is_over_age': 'NO',
'mileage': 71542,
'vehicle_type': 'FAMILY.SMALL',
'is_domestic': 'Import',
'vehicle_age': 8,
'age_group': 'SEVEN+',
'color': 'BLACK',
'make': 'NISSAN',
'state': 'CA',
'make_model': 'NISSAN.SENTRA'},
{'Item': 'Item 3',
'cost': 6356,
'lot_time': 21,
'is_over_age': 'NO',
'mileage': 81708,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'GOLD',
'make': 'PONTIAC',
'state': 'VA',
'make_model': 'PONTIAC.GRAND PRIX'},
{'Item': 'Item 4',
'cost': 4509,
'lot_time': 53,
'is_over_age': 'NO',
'mileage': 62224,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 6,
'age_group': 'SIX',
'color': 'PURPLE',
'make': 'CHEVROLET',
'state': 'GA',
'make_model': 'CHEVROLET.LUMINA'},
{'Item': 'Item 5',
'cost': 4658,
'lot_time': 1,
'is_over_age': 'NO',
'mileage': 58265,
'vehicle_type': 'FAMILY.SMALL',
'is_domestic': 'Import',
'vehicle_age': 7,
'age_group': 'SEVEN+',
'color': 'BLACK',
'make': 'TOYOTA',
'state': 'TX',
'make_model': 'TOYOTA.COROLLA'},
{'Item': 'Item 6',
'cost': 3983,
'lot_time': 15,
'is_over_age': 'NO',
'mileage': 92775,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Import',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'BLACK',
'make': 'MAZDA',
'state': 'TX',
'make_model': 'MAZDA.PROTEGE'},
{'Item': 'Item 7',
'cost': 4233,
'lot_time': 79,
'is_over_age': 'NO',
'mileage': 55691,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 4,
'age_group': 'FOUR',
'color': 'GREEN',
'make': 'FORD',
'state': 'TX',
'make_model': 'FORD.ESCORT'},
{'Item': 'Item 8',
'cost': 3934,
'lot_time': 14,
'is_over_age': 'NO',
'mileage': 82070,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 6,
'age_group': 'SIX',
'color': 'BLUE',
'make': 'FORD',
'state': 'NV',
'make_model': 'FORD.CONTOUR'},
{'Item': 'Item 9',
'cost': 6516,
'lot_time': 14,
'is_over_age': 'NO',
'mileage': 45738,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 3,
'age_group': 'ONE-THREE',
'color': 'GOLD',
'make': 'CHEVROLET',
'state': 'TX',
'make_model': 'CHEVROLET.CAVALIER'},
{'Item': 'Item 10',
'cost': 5601,
'lot_time': 82,
'is_over_age': 'NO',
'mileage': 98384,
'vehicle_type': 'LUXURY',
'is_domestic': 'Import',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'WHITE',
'make': 'NISSAN',
'state': 'CA',
'make_model': 'NISSAN.ALTIMA'},
{'Item': 'Item 11',
'cost': 3608,
'lot_time': 5,
'is_over_age': 'NO',
'mileage': 55043,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'RED',
'make': 'PLYMOUTH',
'state': 'TX',
'make_model': 'PLYMOUTH.NEON'},
{'Item': 'Item 12',
'cost': 3791,
'lot_time': 17,
'is_over_age': 'NO',
'mileage': 77265,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Import',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'WHITE',
'make': 'MAZDA',
'state': 'TX',
'make_model': 'MAZDA.PROTEGE'},
{'Item': 'Item 13',
'cost': 5307,
'lot_time': 1,
'is_over_age': 'NO',
'mileage': 65602,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'GOLD',
'make': 'PLYMOUTH',
'state': 'NV',
'make_model': 'PLYMOUTH.BREEZE'},
{'Item': 'Item 14',
'cost': 4879,
'lot_time': 42,
'is_over_age': 'NO',
'mileage': 67815,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 4,
'age_group': 'FOUR',
'color': 'GREEN',
'make': 'FORD',
'state': 'FL',
'make_model': 'FORD.TAURUS'},
{'Item': 'Item 15',
'cost': 5176,
'lot_time': 1,
'is_over_age': 'NO',
'mileage': 80532,
'vehicle_type': 'FAMILY.LARGE',
'is_domestic': 'Domestic',
'vehicle_age': 6,
'age_group': 'SIX',
'color': 'WHITE',
'make': 'PONTIAC',
'state': 'FL',
'make_model': 'PONTIAC.BONNEVILLE'},
{'Item': 'Item 16',
'cost': 4338,
'lot_time': 13,
'is_over_age': 'NO',
'mileage': 98381,
'vehicle_type': 'LUXURY',
'is_domestic': 'Import',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'WHITE',
'make': 'NISSAN',
'state': 'TX',
'make_model': 'NISSAN.ALTIMA'},
{'Item': 'Item 17',
'cost': 2686,
'lot_time': 83,
'is_over_age': 'NO',
'mileage': 94381,
'vehicle_type': 'FAMILY.SMALL',
'is_domestic': 'Domestic',
'vehicle_age': 9,
'age_group': 'SEVEN+',
'color': 'RED',
'make': 'PONTIAC',
'state': 'VA',
'make_model': 'PONTIAC.GRAND AM'},
{'Item': 'Item 18',
'cost': 4623,
'lot_time': 14,
'is_over_age': 'NO',
'mileage': 53975,
'vehicle_type': 'FAMILY.SMALL',
'is_domestic': 'Domestic',
'vehicle_age': 4,
'age_group': 'FOUR',
'color': 'RED',
'make': 'CHEVROLET',
'state': 'NM',
'make_model': 'CHEVROLET.CAVALIER'},
{'Item': 'Item 19',
'cost': 5750,
'lot_time': 26,
'is_over_age': 'NO',
'mileage': 81570,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 3,
'age_group': 'ONE-THREE',
'color': 'BLUE',
'make': 'OLDSMOBILE',
'state': 'TX',
'make_model': 'OLDSMOBILE.ALERO'},
{'Item': 'Item 20',
'cost': 4966,
'lot_time': 19,
'is_over_age': 'NO',
'mileage': 58344,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 3,
'age_group': 'ONE-THREE',
'color': 'WHITE',
'make': 'CHEVROLET',
'state': 'TX',
'make_model': 'CHEVROLET.MALIBU'},
{'Item': 'Item 21',
'cost': 5595,
'lot_time': 6,
'is_over_age': 'NO',
'mileage': 49718,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Import',
'vehicle_age': 3,
'age_group': 'ONE-THREE',
'color': 'GOLD',
'make': 'MAZDA',
'state': 'GA',
'make_model': 'MAZDA.PROTEGE'},
{'Item': 'Item 22',
'cost': 3906,
'lot_time': 44,
'is_over_age': 'NO',
'mileage': 89301,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Import',
'vehicle_age': 7,
'age_group': 'SEVEN+',
'color': 'BLUE',
'make': 'MITSUBISHI',
'state': 'NV',
'make_model': 'MITSUBISHI.MIRAGE'},
{'Item': 'Item 23',
'cost': 7659,
'lot_time': 121,
'is_over_age': 'YES',
'mileage': 53148,
'vehicle_type': 'FAMILY.LARGE',
'is_domestic': 'Domestic',
'vehicle_age': 6,
'age_group': 'SIX',
'color': 'SILVER',
'make': 'OLDSMOBILE',
'state': 'TX',
'make_model': 'OLDSMOBILE.AURORA'},
{'Item': 'Item 24',
'cost': 3519,
'lot_time': 2,
'is_over_age': 'NO',
'mileage': 98287,
'vehicle_type': 'LUXURY',
'is_domestic': 'Import',
'vehicle_age': 7,
'age_group': 'SEVEN+',
'color': 'GOLD',
'make': 'NISSAN',
'state': 'TX',
'make_model': 'NISSAN.ALTIMA'},
{'Item': 'Item 25',
'cost': 5061,
'lot_time': 39,
'is_over_age': 'NO',
'mileage': 71391,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'GOLD',
'make': 'OLDSMOBILE',
'state': 'TX',
'make_model': 'OLDSMOBILE.CUTLASS'},
{'Item': 'Item 26',
'cost': 3888,
'lot_time': 83,
'is_over_age': 'NO',
'mileage': 63111,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 7,
'age_group': 'SEVEN+',
'color': 'WHITE',
'make': 'OLDSMOBILE',
'state': 'NV',
'make_model': 'OLDSMOBILE.CIERA'},
{'Item': 'Item 27',
'cost': 3793,
'lot_time': 23,
'is_over_age': 'NO',
'mileage': 48016,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Import',
'vehicle_age': 5,
'age_group': 'FIVE',
'color': 'BLUE',
'make': 'GEO',
'state': 'CA',
'make_model': 'GEO.METRO'},
{'Item': 'Item 28',
'cost': 5061,
'lot_time': 60,
'is_over_age': 'NO',
'mileage': 72985,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 4,
'age_group': 'FOUR',
'color': 'WHITE',
'make': 'FORD',
'state': 'VA',
'make_model': 'FORD.ESCORT'},
{'Item': 'Item 29',
'cost': 4857,
'lot_time': 8,
'is_over_age': 'NO',
'mileage': 93040,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Domestic',
'vehicle_age': 8,
'age_group': 'SEVEN+',
'color': 'SILVER',
'make': 'CADILLAC',
'state': 'AZ',
'make_model': 'CADILLAC.DEVILLE'},
{'Item': 'Item 30',
'cost': 3361,
'lot_time': 46,
'is_over_age': 'NO',
'mileage': 70751,
'vehicle_type': 'ECONOMY',
'is_domestic': 'Domestic',
'vehicle_age': 8,
'age_group': 'SEVEN+',
'color': 'WHITE',
'make': 'BUICK',
'state': 'VA',
'make_model': 'BUICK.SKYLARK'},
{'Item': 'Item 31',
'cost': 4068,
'lot_time': 59,
'is_over_age': 'NO',
'mileage': 61770,
'vehicle_type': 'FAMILY.MEDIUM',
'is_domestic': 'Import',
'vehicle_age': 7,
'age_group': 'SEVEN+',
'color': 'PURPLE',
'make': 'NISSAN',
'state': 'AZ',
'make_model': 'NISSAN.SENTRA'}]

pickle_off = open("used_car_sale_price_train_test.pickle","rb")
scaler = pickle.load(pickle_off)
model = pickle.load(pickle_off)
X_ohe = pickle.load(pickle_off)
cat_val = pickle.load(pickle_off)

sel_row=[]
# create route that renders index.html template
@app.route("/", methods=["GET", "POST"])
def index():
               
        if request.method == "POST":
                item = request.form["item"]
                print(item)
                for d in range(0,len(data)):
                        if data[d]['Item']==item:
                                sel_row.append(data[d])
                
        return render_template("index.html", data=data)
# @app.route("/inputdata")
def data1():
    print(sel_row)
    return render_template("index_1.html", data=sel_row)
#     return jsonify(sel_row)


@app.route("/predict")
def predict():
    ''' pass the data in following format
    val_data_row = [{'cost': 4751, 'lot_time':126 , 'is_over_age': 'YES', 'mileage':77606, 'vehicle_type': 'ECONOMY',\
       'is_domestic': 'Domestic', 'vehicle_age':5 , 'age_group': 'FIVE', 'color': 'BLUE', 'make': 'CHEVROLET', 'state': 'FL',\
       'make_model': 'CHEVROLET.CAVALIER'}]'''
#     val_data_row = [{'cost': 4751, 'lot_time':126 , 'is_over_age': 'YES', 'mileage':77606, 'vehicle_type': 'ECONOMY',\
#        'is_domestic': 'Domestic', 'vehicle_age':5 , 'age_group': 'FIVE', 'color': 'BLUE', 'make': 'CHEVROLET', 'state': 'FL',\
#        'make_model': 'CHEVROLET.CAVALIER'}]

    del sel_row[0]['Item']
    val_data_row = sel_row
    df_val_data_row =pd.DataFrame(val_data_row)
    df_val_data_row.head()

    X_val = df_val_data_row.drop(['cost'],axis=1)  
    y_val = df_val_data_row['cost']

    X_val_ohe = X_ohe.transform(X_val[cat_val])
    X_val_final = pd.concat([X_val.drop(cat_val, 1),X_val_ohe], axis=1).reindex()
    X_val_final.head()

    # transform the val dataset
    rescaledValX = scaler.transform(X_val_final)
    val_pred = model.predict(rescaledValX)
#     print(mean_squared_error(y_val, val_pred))
#     MSE = mean_squared_error(y_val, val_pred)
#     r2 = model.score(rescaledValX, y_val)

#     print(f"MSE: {MSE}, R2: {r2}")

    perc_accu=(1-((val_pred-y_val)/val_pred))*100
#     print(f'Percentage Accuracy: {perc_accu}')
#     pd.DataFrame(zip(rescaledValX, y_val,val_pred)).head(200)
#     print(f'one hot encoded features:{rescaledValX}')
#     print(f'Actual Value (not from train or test set (separate data from val data):{y_val}')
#     print(f'Predicted Value from Model:{val_pred}')
#     sns.barplot(x=['actual','predicted'], y=[y_val,val_pred[0]])
    output={}
    output['Percentage Accuracy']= int(perc_accu)
    output['Actual Value (not from train or test set (separate data from val data)']=int(y_val)
    output['Predicted Value from Model:']=int(val_pred)
    return jsonify(output)
if __name__ == "__main__":
    app.run(debug=True)
