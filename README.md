# Sentrycs-pythonWebApp
This Flask app is a simple web application running behind nginx+tls in Docker Compose that interacts with a MySQL database to manage and retrieve product data.

The app uses the mysql.connector library to interact with the MySQL database.
 It converts the retrieved data from the database into JSON format and returns it to the client.


To set up and run a multi-container application using Docker Compose based on Jenkins, 
please ensure Docker and Docker Compose are installed on your Jenkins build agent or server.


.env file in the app folder contains all database configuration

.env file under the main directory contains PASSWORD for connecting MySQL 



How to test it:

#hello world
curl --insecure https://localhost


#This route is used to create database tables. It connects to the MySQL database (specified by host, user, password, and database name) and uses a cursor to execute SQL statements for creating tables.
curl --insecure https://localhost/initdb
curl --insecure https://localhost/init_tables


#"/products" endpoint of your Flask web application, you will receive a JSON response containing the list of products from the "tblProduct" table in your MySQL database.
curl --insecure https://localhost/products


#enter to mysql
docker exec -ti mysql-flask-app-container mysql -u root -p


#select a database and select all rows and columns from the "tblProduct" table in the database 
use ProductManagement
select * from tblProduct;


#Insert two rows of data into the "tblProduct" table, with specific values for the "name" and "description" columns.
INSERT INTO tblProduct(name, description) VALUES
('Dell XPS desktop', 'V7'),
('sony playstation', 'V5');


curl --insecure https://localhost/products
