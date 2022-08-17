FROM docker.io/galenguyer/nginx:1.21.6-alpine-spa

COPY templates /usr/share/nginx/html

EXPOSE 8080
