# QnA Platform API

Welcome to the QnA Platform API repository! This API is designed to allow developers to create and manage a Q&A platform with ease. This repository includes everything needed to build and host a SQL server with a website connected to allow users to upload questions and make custom quizzes.

## Getting Started

To get started with the API, you will need to clone this repository and have access to a SQL server. You will also need to install the necessary dependencies listed in the `requirements.txt` file.

### Configuration

Before running the API, you will need to configure the database connection string in the `appsettings.json` file. Replace the `ConnectionStrings:DefaultConnection` value with the connection string for your SQL server.

### API Documentation

The API documentation can be found in the `docs` folder of this repository. The documentation contains information about the API endpoints, request parameters, and response formats.

### API Endpoints

The API provides the following endpoints:

- `/questions`: Allows you to create, retrieve, update, and delete questions.
- `/quizzes`: Allows you to create, retrieve, and delete quizzes.

### Website

The website is located in the `web` folder of this repository. The website allows users to upload questions and make custom quizzes. To use the website, you will need to run the API and navigate to `http://localhost:5000` in your web browser.

## Contributing

We welcome contributions to the QnA Platform API! If you would like to contribute, please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
