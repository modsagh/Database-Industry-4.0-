# <center> Laboratory 1 - DBMS and clients</center>



## Introduction



The aim of this laboratory is to familiarize participants with database management systems ([DBMS](https://en.wikipedia.org/wiki/Database#Database_management_system)) and the basic principles of their use.



In these classes, we will use:

- [SQLite](https://www.sqlite.org/index.html)

- [MySQL](https://www.mysql.com/)

- [PostgreSQL](https://www.postgresql.org/)



## SQLite



SQLite is a database engine, written in the C language. It is not a standalone DBMS, it is a library that software developers embed in their apps. As such, it belongs to the family of embedded databases. It is the most widely deployed database engine, as it is used by several of the top web browsers, operating systems, mobile phones, and other embedded systems. 



For SQLite, the most similar application to classical DBMS is ‘’DB Browser for SQLite’’. This program can be downloaded [here](https://sqlitebrowser.org/dl/).





### Create database



1. Instal and open DB Browser for SQLite.  

![SQLite start view](fig/sqlite_start.png)

2. In left right corner click option *New Database* or go *File> Create New Database*

3. In dialog window set your database name and confirm clicked button *Save*



### Create table

After save your new database in tab *Database Structure* you can create new table in your database. To do that you need:

1. In *Database Structure* click *Create table*

2. In dialog window set table name\

3. Go to *Fields* and click *Add*

4. In created row set name and data type



## MySQL


MySQL is an open-source relational database management system. To easy management this database, most developers use PHPMyAdmin. 


At AGH, we have the option to create your own database at [panel.agh.edu.pl](https://panel.agh.edu.pl/main.php)

### Create database
1. Login in [panel.agh.edu.pl](https://panel.agh.edu.pl/main.php)
2. Go to section *MySQL* and click in *Utwórz nową bazę danych*
3. You can read your login and password in table *Twoje bazy MySQL*

### Create table
1. Log in to the AGH [phpMyAdmin](https://mysql.agh.edu.pl/phpMyAdmin) interface
2. From left sidebar select your database name
3. Go to tab *Struktura* set name your table and number of columns
4. Click *Wykonaj*
5. In created row set name and data type 


## PostgreSQL
PostgreSQL also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It is the default database for macOS Server and is also available for Windows, Linux, FreeBSD, and OpenBSD.

[pgAdmin](https://www.pgadmin.org/) is an open source program for managing and work with the PostgreSQL database. Currently the program is marked as pgAdmin 4. It is the next, fourth branch of the program development written in Python.


### Set pgAdmin connection to server
1. Open pgAdmin
2. Go to Object>Create>Server ...
3. In dialog windows tab General set server name
3. Go to tab Connection
4. Set Host name, port, Maintenance database (database_name), Username and Password
5. Save your settings  


## Exercises:

1. Create database in SQLite with two tables

2. Create database in AGH MySQL server and create example table 

3. Configure connection to PostgreSQL with properties:

	- url: pgsql-196447.vipserv.org:5432

	- login: wbauer_adb

	- password: adb2020

	- database_name: wbauer_adb





Supplementary materials:

- [SQLite](https://www.sqlite.org/index.html)

- [MySQL](https://www.mysql.com/)

- [PostgreSQL](https://www.postgresql.org/)

- [Uncle Google](https://google.pl) i [auntie Wikipedia](https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna)





