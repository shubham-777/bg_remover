FROM python:3.8-slim
WORKDIR /bg_remover
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /root/.u2net/
COPY instance/u2net.onnx /root/.u2net/u2net.onnx
EXPOSE 5000
ENV FLASK_ENV=production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:gunicorn_app"]