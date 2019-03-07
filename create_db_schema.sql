create user jobsbot_user with
    SUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    LOGIN
    ENCRYPTED PASSWORD 'jobsbot_pwd';
create database jobsbot;
\connect jobsbot
create table jobs (
    id serial primary key,
    job_title text,
    job_url text,
    job_description text,
    company_name text,
    crawled_date text,
    posted_date text)
