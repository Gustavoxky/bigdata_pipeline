FROM bitnami/spark:latest

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

WORKDIR /app

# Copiar os arquivos necessários para dentro do contêiner
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY src /app/src
