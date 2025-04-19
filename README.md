
# Mercedes-Find - SAE Design Challenge 2025

This project utilizes Mercedes-Benz's car configurator API to showcase models for customers to view. 

Built on Python 3, Flask, and HTML. Utilized Postman to simulate API calls. 

API Website: https://developer.mercedes-benz.com/

MercedesMe account required to call API. Secret key needed. 

## Features

- Dynamic list updates based off of user selection
- Model display



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MERCEDES_API_KEY`



## API Reference

#### Get all classes

```http
  GET https://api.mercedes-benz.com/configurator/v2/markets/en_DE/classes
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `x-api-key` | `string` | **Required**. Your API key |
| `accept` | `string` | **Required**. application/json |

#### Get all models

```http
  GET https://api.mercedes-benz.com/configurator/v2/markets/en_DE/models
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `x-api-key` | `string` | **Required**. Your API key |
| `accept` | `string` | **Required**. application/json |



## Run Locally

Clone the project

```bash
  git clone https://github.com/tristanaujong/SAEDesignChallenge25FINAL
```

Go to the project directory

```bash
  cd my-project
```

Create .venv folder

```bash
  py -m venv .venv
```

Activate virtual environment

```bash
  .venv\Scripts\activate
```

Install dependencies

```bash
  pip install flask
  pip install requests
  pip install python-dotenv                                                        
```

Start the server

```bash
  py main.py
```


## Demo

https://youtu.be/hxQFF62wul0
## Figma

Figma: https://www.figma.com/design/kB4XKsmo1AVq1IO9SC7qie/Mercedes-Find?node-id=0-1&t=6FwHlWErcde1SSFG-1


## Lessons Learned

Doing this design challenge enabled me to learn a lot about API's. In this project I was able to demonstrate simple "GET" API calls and recieve Mercedes-Benz json data over car information in return. I also learned about response codes and what they mean to the user. This was my first time experimenting with API's hands on, and it made things click in my head on how websites and certain attributes work on the internet. 

One problem I ran into was running out of API calls. Mercedes-Benz limits your calls to 150 per project, so I ran out pretty quickly after constantly testing. This was solved by making a new project on my MercedesMe account and regenerating a new key. I also learned that you have to restart your environment for the new API key to take place.

Postman was very helpful for me to see exactly what a certain API request returned. The Mercedes-Benz car configurator API has a lot of layers, and while reading the documentation was helpful on its own, Postman enabled me to see certain requests in real-time along with ensuring my API key was working. 


## Roadmap

- Add styling and iron out API call structure

- Show model specifications

- Allow for quick customizing of colors and 360 view

- Add full build customizer

