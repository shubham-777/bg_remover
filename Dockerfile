FROM python:3.8-slim AS build
WORKDIR /bg_remover
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache
COPY . .

FROM python:3.8-slim
WORKDIR /bg_remover
COPY --from=build /usr/local /usr/local
COPY --from=build /bg_remover /bg_remover

RUN mkdir -p /root/.u2net/ && \
    cp instance/u2net.onnx /root/.u2net/u2net.onnx
ENV FLASK_ENV=production
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} main:gunicorn_app"]
