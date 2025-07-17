FROM apache/superset:latest

ENV SUPERSET_HOME=/app/superset_home

USER root

COPY requirements.txt .
RUN pip install -r requirements.txt

# Ensure directories exist for config/logs
RUN mkdir -p /app/superset_home

# Copy superset config
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

COPY init_superset.sh /app/init_superset.sh
RUN chmod +x /app/init_superset.sh

EXPOSE 8088
CMD ["/usr/bin/run-server.sh"]