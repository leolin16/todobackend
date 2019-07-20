FROM nginx
LABEL Author="Leo Lin <leolin@leolin.studio>"

# Copy configuration file
COPY todobackend.conf /etc/nginx/conf.d/todobackend.conf