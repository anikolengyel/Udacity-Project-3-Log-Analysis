# Udacity-Project-3-Log-Analysis
A simple reporting tool with Python and PostgreSQL.

Introduction

This is a project wokrk for Udacity's Full Stack Nanodegree program. In This
project work I explored a database with complex SQL queries. The project
is similar to an internal reporting tool that uses a database to get log data
and gain information about the user preferences and activity.

Setup

Clone this repository.
The repository contains:
- project_3.py source code
- an example text file of the programs output
- this README.md file

Download the newsdata.sql from Udacity's course page. It will run scripts
to create the database.

The database contains the following tables:
- authors: A list of the authors who published the articles
- articles: Information about the articles themselves
- log: Information about every time a user has accessed the site.

If you do not have the necessary programs, you will need to install the followings:
- python3
- Vagrant
- Virtual Box

Running

Launch Vagrant by running vagrant up from the command line, then log with
vagrant ssh.

To load the data, type the command psql -d news -f newsdata.sql in the news
database.

Run project_3.py to execute the program.

