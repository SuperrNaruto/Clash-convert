FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
COPY clash-converter-api/requirements.txt ./clash-converter-api/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r clash-converter-api/requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "clash-converter-api/src/main.py"]
