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

# SQL Alchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, aliased,sessionmaker
from sqlalchemy import create_engine, func, inspect, MetaData,Table, Column, ForeignKey,and_,or_,text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Create Engine and Pass in MySQL Connection
engine = create_engine("mysql://root:Hema$0724@localhost/used_car_price")
conn = engine.connect()
inspector = inspect(engine)
Session = sessionmaker(bind = engine) #note that's a capital s on Session
session = Session() #lowercase s
metadata = MetaData()
print ('Creating automap base')
Base = automap_base()
print ('setting up automapping')

t_price_predict = Table('price_predict', metadata, autoload=True, autoload_with=engine)

cols= inspector.get_columns('price_predict')
df_cols = pd.DataFrame(cols)
print(df_cols)

# @app.route("/")
# def home():
#     return "Welcome!"


# Create a list to hold our data
pickle_off = open("used_car_sale_price_train_test.pickle","rb")
scaler = pickle.load(pickle_off)
model = pickle.load(pickle_off)
X_ohe = pickle.load(pickle_off)
cat_val = pickle.load(pickle_off)

sel_row = []
@app.route("/api/data")
def data():
    print(sel_row)
    return jsonify(sel_row)
@app.route("/", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        out1=[]
        sel_row = []
        # cost = request.form["cost"]
        lot_time = request.form["lot_time"]
        is_over_age = request.form["is_over_age"]
        mileage = request.form["mileage"]
        vehicle_type = request.form["vehicle_type"]
        is_domestic = request.form["is_domestic"]
        vehicle_age = request.form["vehicle_age"]
        age_group = request.form["age_group"]
        color = request.form["color"]
        make = request.form["make"]
        state = request.form["state"]
        make_model = request.form["make_model"]

        try:
            result = session.execute(t_price_predict.insert().values(lot_time=lot_time, is_over_age=is_over_age, mileage=mileage,
                                                        vehicle_type=vehicle_type,is_domestic=is_domestic, vehicle_age=vehicle_age,
                                                        age_group=age_group,color=color,make=make, state=state,make_model=make_model))
            session.commit()
            print(type(result))
            db_row_id=result.lastrowid
            print(db_row_id)
        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()
        

        form_data = {
            "cost":int(0),
            "lot_time": int(lot_time),
            "is_over_age": is_over_age,
            "mileage": int(mileage),
            "vehicle_type": vehicle_type,
            "is_domestic": is_domestic,
            "vehicle_age": int(vehicle_age),
            "age_group": age_group,
            "color": color,
            "make": make,
            "state": state,
            "make_model": make_model
        }

        sel_row.append(form_data)
    

        ''' pass the data in following format
        val_data_row = [{'cost': 4751, 'lot_time':126 , 'is_over_age': 'YES', 'mileage':77606, 'vehicle_type': 'ECONOMY',\
        'is_domestic': 'Domestic', 'vehicle_age':5 , 'age_group': 'FIVE', 'color': 'BLUE', 'make': 'CHEVROLET', 'state': 'FL',\
        'make_model': 'CHEVROLET.CAVALIER'}]'''
    #     val_data_row = [{'cost': 4751, 'lot_time':126 , 'is_over_age': 'YES', 'mileage':77606, 'vehicle_type': 'ECONOMY',\
    #        'is_domestic': 'Domestic', 'vehicle_age':5 , 'age_group': 'FIVE', 'color': 'BLUE', 'make': 'CHEVROLET', 'state': 'FL',\
    #        'make_model': 'CHEVROLET.CAVALIER'}]

        
        val_data_row = sel_row
        df_val_data_row =pd.DataFrame(val_data_row)
        print(df_val_data_row.head())

        X_val = df_val_data_row.drop(['cost'],axis=1)  
        

        X_val_ohe = X_ohe.transform(X_val[cat_val])
        X_val_final = pd.concat([X_val.drop(cat_val, 1),X_val_ohe], axis=1).reindex()
        X_val_final.head()

        # transform the val dataset
        rescaledValX = scaler.transform(X_val_final)
        val_pred = model.predict(rescaledValX)
        out1= [{'Predicted_Value':int(val_pred) }]
        out1.append(sel_row)
        try:
            session.execute(t_price_predict.update().where(t_price_predict.c.id == db_row_id).values(cost=int(val_pred)))
            
            session.commit()
            
        except SQLAlchemyError as e:
            print(e)
        finally:
            
            session.close()
        # sel_row[0]['cost']=val_pred

       
        # return jsonify(output)

        # return "Thanks for the form data!"
        # print(sel_row)
        
        # return jsonify([{'Predicted Value':int(val_pred) }])

        return render_template("index_final.html", data=out1)


    return render_template("collect_new_data_for_prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
