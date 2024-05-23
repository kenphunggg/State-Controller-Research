FROM mysql:5.7.15

MAINTAINER me

ENV MYSQL_ROOT_PASSWORD = 'PQThai29112003'
ENV MYSQL_DATABASE = 'randomNumberDB'
ENV MYSQL_USER = 'kenphung'
ENV MYSQL_HOST = '%'

ADD mysql.sql /docker-entrypoint-initdb.d

EXPOSE 3306