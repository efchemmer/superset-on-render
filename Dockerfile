FROM apache/superset:latest

ENV SUPERSET_HOME=/app/superset_home

USER root

# Install custom dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Ensure directories exist
RUN mkdir -p /app/superset_home

# Copy Superset config
COPY superset_config.py /app/pythonpath/superset_config.py

# Copy custom entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

USER superset

# Expose port
EXPOSE 8088

# Use custom entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]