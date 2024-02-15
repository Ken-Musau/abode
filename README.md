# Abode Database

Abode Database is a Flask application for managing real estate properties and houses within estates. It provides a simple API for performing CRUD operations on estates and houses.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ken-Musau/abode-database.git
    ```

2. Navigate to the project directory:

    ```bash
    cd abode-database
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the Flask application:

    Edit the `app.py` file to configure the Flask application according to your preferences. You can set the database URI, tracking modifications, and other settings.

2. Initialize the database:

    Run the following command to apply database migrations:

    ```bash
    flask db upgrade
    ```

3. Run the application:

    Start the Flask application by running:

    ```bash
    python app.py
    ```

4. Access the API:

    Open a web browser or use tools like Postman to access the API endpoints. By default, the application runs on port 5555. Visit `http://localhost:5555/` to see the welcome message.

## API Endpoints

- `GET /estates`: Retrieve all estates.
- `POST /estates`: Create a new estate.
- `PUT /estates/<estate_id>`: Update an existing estate.
- `DELETE /estates/<estate_id>`: Delete an estate.
- `GET /houses`: Retrieve all houses.
- `POST /houses`: Create a new house.
- `PUT /houses/<house_id>`: Update an existing house.
- `DELETE /houses/<house_id>`: Delete a house.

## Dependencies

- Flask: Web framework for Python.
- Flask-Migrate: Database migrations for Flask applications.
- Flask-SQLAlchemy: SQLAlchemy integration for Flask.
- SQLAlchemy: SQL toolkit and ORM for Python.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for any enhancements or fixes you'd like to see.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
