# A litte python container 
FROM python:3.11-slim

# working app inside the container  
WORKDIR /app

# copy the requirements file into the continer 
COPY requirements.txt .

# install the requirements 
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest off the files (inclode counter-service.py)
COPY . .

# expose the app port 
EXPOSE 80
# Run the py script.
CMD ["python3", "counter-service.py"]
