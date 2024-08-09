FROM mysql:5.7

COPY ./queries/main.sql/ /docker-entrypoint-initd.d/