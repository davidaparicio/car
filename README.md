
# CAR - Calculatrice Astreinte/Repos

## On-Call Rest Period Calculator

This Flask application helps manage on-call schedules by calculating rest periods between on-call sessions and regular office hours. It ensures compliance with rest policies, such as the 11-hour daily rest and the 35-hour weekend rest window.

## Features

- Calculate if an 11-hour daily rest period is respected between two workdays.
- For on-calls during the weekend, calculate if a 35-hour rest window is observed before the start of the office hours.
- Dynamic addition of multiple on-call end times.
- User-friendly interface with date and time pickers.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
```bash
git clone
```
2. Navigate to the project directory:
```bash
cd car
```
3. Create a virtual environment:
```bash
pip install -r requirements.txt
```

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
5. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

To run the application:

1. Activate the virtual environment (if not already activated).
2. Start the Flask server:
```bash
python app.py
```
3. Open a web browser and navigate to `http://127.0.0.1:5000/`.


## Development

This project uses Flask, a micro web framework for Python.

## Contribution

To contribute to the project:

- Create a new branch for your feature or fix.
- Write and test your code.
- Submit a pull request for review.

## Production deployment

To deploy your Flask application in a production environment, you should use a production-grade WSGI (Web Server Gateway Interface) server. Common choices for WSGI servers include Gunicorn, uWSGI, and Apache with mod_wsgi. Here's a brief overview of how to use Gunicorn, as it's one of the more popular choices:

### Using Gunicorn

Install Gunicorn: If you haven't already installed Gunicorn, you can do so using pip:

```bash
pip install gunicorn
```

Run the Application with Gunicorn: Instead of running your app with Flask's development server, you use Gunicorn. For example:

```bash
gunicorn -w 4 your_application:app
```

In this command:
* -w 4 specifies that Gunicorn should use 4 worker processes. You can adjust this number based on your server's CPU cores and the expected workload.
* your_application is the name of your Python file without the .py extension (e.g., for app.py, it would be app).
* app is the Flask application instance within your Python file.

Additional Configuration: Depending on your needs, you might also want to configure logging, bind to a specific IP and port, manage SSL/TLS settings, etc. Gunicorn's documentation provides details on these configurations.

### Other Deployment Considerations

* Reverse Proxy: In a production setup, it's common to place a reverse proxy like Nginx in front of your WSGI server. This can provide additional benefits like load balancing, SSL termination, and serving static files efficiently.
* Environment Variables: Make sure to separate your development and production configurations. Environment variables can be used to manage this.
* Security: Ensure that your production environment is secure. This includes using HTTPS, keeping software up-to-date, securing sensitive data, etc.
* Monitoring and Logging: Implement monitoring and logging to keep track of your application's health and performance.

### Deployment on Cloud Platforms

If you're planning to deploy on cloud platforms like AWS, Google Cloud, or Heroku, they often provide their own tools and services for deploying Python web applications, which can further simplify the process.

Remember, moving to production requires careful planning, especially around security and performance. Make sure to test your deployment thoroughly in a staging environment before going live.

## License

[Specify the license here or state that it's unlicensed.]

## Contact

For any questions or contributions, please reach out to [Your Name or Contact Information].

---

README Template Version: 1.0
Last Updated: [Date]
