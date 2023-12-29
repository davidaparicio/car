
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

## Testing

### Best Practices

* Isolation: Each test should be isolated and independent of others. Tests should not rely on the state left by previous tests.
* Coverage: Aim for high test coverage, but remember that 100% coverage does not guarantee bug-free code.
* Mocking: Use mocking (e.g., unittest.mock) to simulate behaviors of complex dependencies or external services.
* Continuous Integration: Integrate testing into your CI/CD pipeline to ensure tests are run automatically.

### Advanced Testing

For more complex applications, consider using additional tools like pytest for a more feature-rich testing experience, and Flask-Testing for additional Flask-specific testing utilities.

Testing in Flask, as in any framework, is a vast topic, and these guidelines provide a starting point. As your application grows, your testing strategies will likely need to evolve to match its complexity and requirements.


## Contribute

Works on my machine - and yours ! Spin up pre-configured, standardized dev environments of this repository, by clicking on the button below.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#/https://github.com/davidaparicio/gokvs)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

- open [issues] (https://github.com/davidaparicio/car/issues)
- send [pull requests] (http://help.github.com/send-pull-requests)
- contact [David Aparicio] (https://github.com/davidaparicio)

## License
Licensed under the MIT License, Version 2.0 (the "License"). You may not use this file except in compliance with the License.
You may obtain a copy of the License [here](https://choosealicense.com/licenses/mit/).

If needed some help,  there are a ["Licenses 101" by FOSSA](https://fossa.com/blog/open-source-licenses-101-mit-license/), a [Snyk explanation](https://snyk.io/learn/what-is-mit-license/)
of MIT license and a [French conference talk](https://www.youtube.com/watch?v=8WwTe0vLhgc) by [Jean-Michael Legait](https://twitter.com/jmlegait) about licenses.


[//]: # (https://www.makeareadme.com/)

---

README Template Version: 1.0
Last Updated: 29/12/23
