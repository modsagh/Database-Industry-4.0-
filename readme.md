# <center>![logo](fig/loga_MoDS.jpg) Laboratory Database in Industry 4.0</center>

![EU_logo](fig/log_eu.jpg) 


## Introduction

The aim of this laboratory is to familiarize participants with database management systems ([DBMS](https://en.wikipedia.org/wiki/Database#Database_management_system)) and the basic principles of their use in Industry 4.0. In these classes, we will use [SQLite](https://www.sqlite.org/index.html)




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



## Exercises 1:

1. Create database in SQLite with two tables


## Introdaction to SQLAlchemy

The purpose of these part of workshop is to familiarize participants with the basic techniques of working with [SQLAlchemy](https://www.sqlalchemy.org/).

The scope of this classes:
- connection to a database (especially remote database),
- explore of database structure using ORM,
- creating simple select in ORM,
- using query results in a program,
- adding where clause to query.


SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

Object Relational Mapper (ORM) is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.


## Connection SQLAlchemy with database

To connection a database with a program with the basic version we need to use the following script:

```python
from sqlalchemy import create_engine

db_string = "database_type://user:password@database_url:port/database_name"

db = create_engine(db_string)
```
where:
- *databae_type* is the name of database driver, more details you can read [here](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls),
- *user* - name of user in database,
- *password* - password to database,
- *database_url* - url address to database,
- *port* - port to database connection,
- *database_name* - name of database.  

*[create_engine](https://docs.sqlalchemy.org/en/13/core/connections.html)* is just interface to connection database with program. To install this library use command:

```
pip install sqlalchemy
```
or
```
python -m pip install sqlalchemy
```


## Explore database structure
Because the database structure is not always known to the programmer for various reasons, most often due to lack of documentation. In this case, it's worth knowing that we can use SQL query to explore database structure.

Of course, SQLAlchemy has the function to read this data:

```python
from sqlalchemy import create_engine, MetaData, Table

print(db.table_names())

metadata = MetaData()

table = Table(table_name, metadata , autoload=True, autoload_with=db)

print(repr(table))

print(table.columns.keys())
``` 
In this sript *table_name* is the string with table name in database.

## SQLAlchemy query

The basic select in SQLAlchemy has form:

```python
stmt = 'select * from table'

# Execute the statement and fetch the results
results = db.execute(stmt).fetchall()

# Print results
print(results)
```
Function *execute* make a request to a database and *fetchall* method get our results from an executed query. But in this case we don't use ORM propertis. More correctly is use structur:

```python
from sqlalchemy import select

stmt = select([table])

# Print the SQL query string
print(stmt)

# Execute the statement and fetch with limit the results 
results = db.execute(stmt).fetchmany(size=10)
print(results)
```
In this case, the ORM system creates a query based on information in object *table*.

### Read result from query
The variable *results* can be read as follows:

1. Print  n row of the results:

```python
print(results[n])
```
2. Print the first column of a n row by accessing it by its index:

```python
print(first_row[:][n])
```
3. Print the column by name of the a n row by using its name

```python
print(results[n][name])
```

### Adding constraint to query
 Adding a restriction to a query involves entering the *where* function as follows:
 ```python
stmt = select([table])

# Add a where clause to filter the results
stmt = stmt.where(table.columns.column_name == 10)

# Execute the query to retrieve all the data returned: results
results = db.execute(stmt).fetchall()

# Loop over the results and print the column_name_1 and column_name_2
for result in results:
    print(result.column_name_1, result.column_name_2)

 ```
## Measurement collection system simulator

The main task of database systems is to collect data for easy processing and analysis. In this part of the workshop, we will present a measurement simulator that we will use in further exercises.

The simulator used in these workshops is very simple and consists of scripts:
```
- GenericSensor.py
- Client.py
```

GenericSensor.py script is used to run a multi-threaded program that simulates various sensors and their measurements. To run it, enter in the command line:

```
python GenericSensor.py
```
After successful activation, information about the created sensors will be displayed on the command line, for example:
```
name: temperature_1,
        serial_number: 2NixMVxg,
        ip_address: localhost,
        port:58080,
        unit:C,
        lon:19,
        lat:22
name: temperature_2,
        serial_number: 2VWFjDQW,
        ip_address: localhost,
        port:58081,
        unit:C,
        lon:19,
        lat:21
...
```

Client.py script is used to read data from sensors. Before starting it, enter the appropriate ports in the __SensorConnection__ from the message above. For example:

```python
if __name__ == '__main__':
    temp_1 = SensorConnection(port= 58080)
    temp_2 = SensorConnection(port= 58081)
```
and enter in the console:
```
python Client.py
```

to start client.

## Creating database in SQLAlchemy 

This part described the process of creating a table in a database with SQLAlchemy based on [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) methodology.

### Assumptions

Suppose we want to create tables

- Authors

| id 	| name      	| surname       	| born_date  	|
|:--:	|:-----------:	|:---------------:	|:------------:	|
| 1  	| William   	| Shakespeare   	| 26.04.1564 	|
| 2  	| Albert    	| Camus         	| 7.11.1913  	|

- Books

| id 	| id_author 	| original_title 	| publication_date 	| original_language 	|
|:--:	|:---------:	|:--------------:	|:----------------:	|:-----------------:	|
|  1 	|     1     	|     Hamlet     	|       1603       	|      english      	|
|  2 	|     1     	|    King Lear   	|       1606       	|      english      	|
|  3 	|     2     	|    La Peste    	|       1947       	|       french      	|

### Prepare the environment
To correct working of this process we need create connection to database and 

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_string = "sqlite:///path_to_file/db_name"

engine = create_engine(db_string)

Base = declarative_base()



```

Nowadays when we using the orm technique we need describing the database tables using class. This process has name [Declarative System](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/index.html). In SQLAlchemy we use this functionality by API [declarative](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html).

Line *Base = declarative_base()* run automatically process of mapping existing tables in a database to class and give us tools to declare new tables schema.  

### Creating tables structure

To declaration new table schema we need to add tools to mapping variable types from the database to Python: 
```python
from sqlalchemy import Column, Integer, String, Date
```

Now we can describe *authors* table:

```python
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    born_date = Column(Date)

    def __repr__(self):
        return "<authors(id='{0}', name={1}, surname={2}, born_date={3})>".format(
            self.id, self.name, self.surnamey, self.born_date)
```

To correct work *declarative_base* mechanizm we must set **\_\_tablename\_\_** attribute. Database server use **__tablename__** as table name. 
In column **name** and **surname** we use *String(50)* to make constraint to string length storage in the database. *primary_key=True* define Primary Key of this table. Columns name used on the database server are identical like class attributes name in Python. 
This procedure is equivalent of SQL code:
```sql
CREATE TABLE public.authors
(
    id integer NOT NULL DEFAULT nextval('authors_id_seq'::regclass),
    name character varying(50),
    surname character varying(50),
    born_date date,
    CONSTRAINT authors_pkey PRIMARY KEY (id)
)
```
Function *\_\_repr\_\_* is decorator to string formatting after query results.


Let's assume that we want now create new table *books*, where we connect books with the author. For that, we need to create the relation between table *authors* and *books* by Foreign Key in table *books*.

On the begining 

```python
from sqlalchemy import ForeignKey

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('authors.id'))
    original_title = Column(String, nullable = False)
    publication_date = Column(Integer, nullable = False)
    original_language = Column(String(), nullable = False)
```

It is exampel of basic relation. For more options and type relationship between two tabels look on [link](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html).  

To create full schema of table in database we use script:
```python
Base.metadata.create_all(engine)
```
If we want create only one table we can use formula:

```python
Book.__table__.create(engine)
```

### Insert data to database
To insert new data to the table we use this script:

```python
newAuthor = Author(name = 'William'
    		surname = 'Shakespeare'
    		born_date = '26.04.1564')

engine.add(newAuthor)   
engine.commit()
```

#### The alternative method of a table schema declaration
Of course, the table creation method presented in the previous section is not the only one. We can describe the table using object *Table* and create a schema of this table by function *create*.

***Example:***

```python
from sqlalchemy import Table, MetaData
USER = Table('users', MetaData(bind=engine), Column('id', Integer, primary_key = True), Column('name', String(20)))
USER.create(engine)
```

If we want to check if a given structure already exists in the database, we can use the following script:

```python
from sqlalchemy_utils import database_exists, create_database

if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()
    Base.metadata.create_all(engine)

```
## Exercise 2.
1. Suggest a database schema for the data from the measurement simulator
2. Implement your structure in script 


### Supplementary materials:

- [SQLite](https://www.sqlite.org/index.html)

- [Uncle Google](https://google.pl) i [auntie Wikipedia](https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna)


![EU_logo](fig/log_eu.jpg)


