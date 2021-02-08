FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

# Packages needed for the python packages compilation
RUN apk add --update curl
RUN apk add --update gcc
RUN apk add build-base
RUN apk add alpine-sdk
# ODBC Package
RUN apk add unixodbc-dev

# Download & install SQL Server OJDBC Driver
RUN mkdir /tmp/sql_server_driver/
RUN curl https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.7.1.1-1_amd64.apk > /tmp/sql_server_driver/msodbcsql17_17.7.1.1-1_amd64.apk
RUN apk add --allow-untrusted /tmp/sql_server_driver/msodbcsql17_17.7.1.1-1_amd64.apk

# Install the Python packages
COPY ./requirements.txt ./requirements.txt
RUN pip install --prefer-binary -r ./requirements.txt

# Copy the code to the conatainer
COPY ./app /app
WORKDIR /

# DB connecntion details
# This is basic you should use Docker secret or any diffrent method to invoke env variables
ENV DB_SERVER_URL=YOUR.SERVER.NAME
ENV DB_PORT=1433
ENV DB_NAME=DATABASE-NAME
ENV DB_USER=DATABASE-USERNAME
ENV DB_PASSWORD=DATABASE-PASSWORD

# API Port
EXPOSE 80
# DB Port 
EXPOSE 1433

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]

