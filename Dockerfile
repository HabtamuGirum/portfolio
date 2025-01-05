# Dockerfile

# 1. Use the official Python image
FROM python:3.11

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory
WORKDIR /app

# 4. Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Copy the Django project files
COPY . /app/


# 7. Expose the port (default Django port)
EXPOSE 8000

# 8. Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
