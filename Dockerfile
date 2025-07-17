FROM apache/superset:latest

ENV SUPERSET_HOME=/app/superset_home

USER root

# Install Google BigQuery driver
RUN pip install pybigquery --upgrade

# Ensure directories exist for config/logs
RUN mkdir -p /app/superset_home

# Copy superset config
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset

EXPOSE 8088
CMD ["/usr/bin/run-server.sh"]