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

CMD ["flask", "--app", "swe40006_portfolio_task_4", "run", "--host", "0.0.0.0", "--port", "5000"]
