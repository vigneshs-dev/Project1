# Use a base image with Python 3.10 or higher
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install pip and other dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Run migrations to create the SQLite database
RUN python manage.py migrate

# Expose the port your app runs on (default is 8000 for Django)
EXPOSE 8000

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
