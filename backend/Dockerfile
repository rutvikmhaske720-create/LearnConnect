# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /back_app

# Copy app files
COPY / /back_app/

# Install dependencies
RUN pip install -r requirements.txt

# Run Gunicorn with Uvicorn workers
CMD ["gunicorn", "app_main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]