
# Price Alert App

This project is a Flask-based web application designed for managing financial alerts. Users can log in, view, filter,create price alerts and delete alerts. The application integrates with a MongoDB database for storing user data and alerts. The project is containerized using Docker, making it easy to deploy and run.


## Features

- User Authentication: Secure login functionality using JWT tokens.

- View Alerts: Display a list of all alerts with options to filter by symbol and status
- Create Alerts: Users can create new alerts by specifying the symbol, price, and other details.
- Delete Alerts: Functionality to delete alerts directly from the user interface.

- Filter Alerts: Users can filter alerts based on the symbol and status to view specific alerts.

## Installation

Clone the project and navigate to the project directory:

```bash
  git clone
  cd backend
```
Installation all packages
```bash
  pip install -r requirements.txt
```
Run the App
```bash
python app.py
```

Using Docker

```bash
docker-compose up --build
```
    
## Acknowledgements

- Flask: A micro web framework for Python.
- MongoDB: A NoSQL database used for storing alert and user data.
- Docker: A platform for developing, shipping, and running applications in containers.
.

