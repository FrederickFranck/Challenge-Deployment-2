# Deployment challenge - Steam analytics

## Description

The goal of this challenge was to visualise a scrapped data from Steam. The data was scraped from the [Steam Store](https://store.steampowered.com/) and provided as a [JSON file](./project/data/database.json).

Another requirement was to use an SQL database to store the data. And to deploy both the visualisation app and the database


## Data 

The first step was to analyze what data was available in the JSON file. After I had to decide what data would be useful for the visualisation & should be stored in the database. I decided to use the following data:
- The Games and their most important data:
    - Name
    - Price
    - Description
    - Developer
- Game Categories
- Game genres 
- Supported platforms
- Supported languages
- Positive and negative reviews



## DataBase

Then I designed the following database diagram:

The SQLquery for the database is [here](/database/SteamDB.sql)


![](/rsc/database.png)
 

For this project I chose to use a [MariaDB](https://mariadb.org/) database. The database is hosted on Google Cloud Platform and is accessible from the internet.
I chose to use a MariaDB database because it is a relational database and is easy to use.
![](/rsc/mariadb.png)


## Parser

After constructing the database I needed to clean up the data and convert it to the correct format to be stored in the database. All the code for the parser is in the [parser.py](./project/parser.py) file. The code to insert the data into the database is in the [insert.py](./project/insert.py) file. 

This will turn the games into Game objects and insert them into the database while also inserting the genres & categories.

For the insert to work you need to create a *project/dbcredentials.toml* file and supply the correct credentials.


```toml  
#project/dbcredential.toml

title = "Database credentials"

['DB']
username = 'username'
password = 'password'
ipaddress = 'database-ip-address'
port = 3306
dbname = 'steamdb'

```

## Visualisation

The visualisation [app.py](./project/app.py) was made in [streamlit](https://streamlit.io/) because i havent had a lot of experience with it and wanted to learn it.
Its hosted in a Docker container on AWS.

### App

If you are not to late a demo might still be running at http://35.180.66.140:8501/


First you have to option to filter on multiple genres & categories.
![](/rsc/website1.png)

After you have narrowed down the games you can select the game and it will display the game's information.:

- All of the supported Platforms
- All of the game's genres
- All of the game's categories
- The game's positive and negative reviews

![](/rsc/website2.png)

## Deployment

As mentioned the database is hosted on Google Cloud Platform, its a Ubuntu Linux Server with MariaDB installed & Configured.

The visualisation app is hosted on AWS as a Docker container and is accessible from the internet [here](http://35.180.66.140:8501/).

### Local

You can deploy this yourself on a local machine.
To do this you need to first setup a mariadb server. for example in a docker container
```bash
docker pull mariadb

docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=steamdb -e MYSQL_USER=username -e MYSQL_PASSWORD=password mariadb
```

Then you need to create the database using the [sql scipt](/database/SteamDB.sql) & a user on the database. After that you need to update the database credentials in the *project/dbcredentials.toml* file. Now you can insert the data.
```bash
pip install -r project/requirements.txt
python ./project/insert.py
```

When you've done all this you can build and deploy the app.

```bash
docker build . -t steamdb-app
docker run -d -p 8501:8501 --name steamapp steamdb-app
```


## Future Development

### Languages

As you might have noticed I included the supported languages in the database. But they are not used in the visualisation. This is because I would need more time to parse the data to make sure it gets inserted correctly into the database.

### Scrapping

Right now I only used the provided data. But this gives me only a snapshot of the data. I would like to get more data from the Steam Store. Not only would this give me more data & new daa but it would also give me the option to create timelines for the data.

### Machine Learning

I would like to be able to create a machine learning model to predict which kind of game is most likely to be played by a user based on their previously played games.