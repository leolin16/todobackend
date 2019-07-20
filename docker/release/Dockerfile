FROM leolin16/todobackend-base:latest
LABEL Author="Leo Lin <leolin@leolin.studio>"

# Copy application artifacts
COPY target /wheelhouse

# Activate virtual environment and install wheel support, 
RUN . /appenv/bin/activate && \
    # pip install --no-index -f /wheelhouse mysqlclient && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse

# RUN manage.py collectstatic --noinput
# RUN manage.py migrate --noinput
