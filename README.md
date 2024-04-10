# headintheclouds YouTube - Flask CRUD API with Docker Compose

Welcome to the headintheclouds repository! Here, we provide a hands-on exercise to learn Docker Compose with variables using real-world examples. In this repository, you will find Python Flask CRUD API code along with Dockerfile, Docker Compose configuration, .env file, and requirements.txt.

### Purpose
The purpose of this repository is to offer a practical way for developers to understand Docker Compose and its usage with variables. By following along with our YouTube tutorial series, you can dive into Docker Compose while building a Flask CRUD API. This approach makes learning fun and interactive, helping our community to grow and strengthen their Docker skills.

### Contents
- app.py: Contains the Python Flask CRUD API code.
- .env: Environment variables file for configuring the Flask application.
- requirements.txt: File containing Python dependencies required for the Flask application.
- Dockerfile: Dockerfile to build the Flask application image.
- docker-compose.yml: Docker Compose configuration file to set up services for the Flask application and any associated services.

### Getting Started
To get started, make sure you have Docker and Docker Compose installed on your system. Then, follow these steps:

Clone this repository to your local machine.
Navigate to the repository directory.
Customize the .env file according to your preferences or keep the default settings.
Build the Docker images and start the services using Docker Compose:
```bash
docker compose up --build flask_app
```

## Testing the Flask CRUD API

Once the services are up and running, you can access the Flask CRUD API from your web browser or a REST client. For more advanced testing and management of the API, we recommend using tools like [Postman](https://www.postman.com/) and [TablePlus](https://tableplus.com/).

### Using Postman

[Postman](https://www.postman.com/) is a powerful API testing tool that allows you to send HTTP requests and view responses in a user-friendly interface. You can use Postman to test all CRUD operations of the Flask API endpoints. Here's how to get started:

1. Download and install Postman from the [official website](https://www.postman.com/).
2. Import the provided Postman collection for this API.
3. Configure the endpoints in the collection with the appropriate base URL.
4. Send requests to the endpoints to test the API functionalities.

### Using TablePlus

[TablePlus](https://tableplus.com/) is a modern, native database management tool that provides a clean user interface for managing databases. You can use TablePlus to interact with the database associated with the Flask CRUD API. Here's how to get started:

1. Download and install TablePlus from the [official website](https://tableplus.com/).
2. Connect TablePlus to the database used by the Flask CRUD API (specified in the `.env` file).
3. Explore the database schema, view data, and perform CRUD operations directly from the TablePlus interface.

Feel free to explore these tools to gain a deeper understanding of how the Flask CRUD API works and to facilitate testing and development.

## Contributing
We welcome contributions from the community to improve this repository and make learning Docker Compose more accessible. If you have any ideas, bug fixes, or improvements, feel free to open an issue or pull request.

## Support
For any questions or assistance regarding this repository, you can reach out to us through our YouTube channel or by opening an issue here on GitHub.

## License
This repository is licensed under the MIT License. Feel free to use and modify the code according to your needs.

Let's learn together and grow our community!

Happy Dockerizing! 🚀 


