CREATE DATABASE used_car_price;

USE used_car_price;

CREATE TABLE price_predict (
id INT AUTO_INCREMENT NOT NULL,
lot_time int not null,
is_over_age VARCHAR(30) NOT NULL,
mileage int not null,
vehicle_type VARCHAR(100) NOT NULL,
is_domestic VARCHAR(30) NOT NULL,
vehicle_age int NOT NULL,
age_group VARCHAR(30) NOT NULL,
color VARCHAR(30) NOT NULL,
make VARCHAR(100) NOT NULL,
state VARCHAR(10) NOT NULL,
make_model VARCHAR(100) NOT NULL,
cost int ,
  PRIMARY KEY (id)
);

SET SQL_SAFE_UPDATES = 0;
delete from price_predict;
commit;
select * from price_predict;