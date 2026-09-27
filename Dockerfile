FROM python:3.14
WORKDIR /usr/local/app

# Copy in the source code
COPY src ./src
EXPOSE 5000

# Install the application dependencies
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir .

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Configure Flask
ENV FLASK_APP=swe40006_portfolio_task_4
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run"]
