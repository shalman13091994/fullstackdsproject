FROM python:3.8-slim-buster
WORKDIR /service

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gnupg \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Microsoft ODBC Driver 17 for SQL Server (if needed)
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    echo "deb [arch=amd64] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

COPY requirements.txt .
COPY . /service
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "./Api/manage.py", "runserver", "0.0.0.0:8081"] 

# same port to be used in the aws 