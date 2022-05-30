CREATE DATABASE reshare;

CREATE USER reshare_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE reshare TO reshare_admin;