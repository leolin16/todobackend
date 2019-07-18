FROM leolin/todobackend-base:latest
LABEL Author="Leo Lin <leolin@leolin.studio>"

# install dev/build dependencies, libmysqlclient-dev is for avoiding can not find mysql_config error
RUN apt-get update && \
    apt-get install -qy python3.7-dev gcc libmysqlclient-dev

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# PIP env variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: build artifacts (Wheels) are output here
VOLUME [ "/wheelhouse" ]

# OUTPUT: Test reports are output here
VOLUME [ "/reports" ]

# OUTPUT: Build cache
VOLUME [ "/build" ]

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT [ "test.sh" ]
CMD [ "python", "manage.py", "test", "--noinput" ]

# Add application source
COPY src /application
WORKDIR /application