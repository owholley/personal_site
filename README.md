# Personal Site
This is my personal site, displaying my web development skills. I've built some features into this site that I would like to extend in the future. It consists of a Django project with minimal extras, essentially just Postgres, some HTML/CSS, and a touch of JavaScript. You can check it out at https://owenwholley.com!

The site is lives on a Linux server, publicly available on a DigitalOcean virtual machine, and available locally for testing on a Raspberry Pi.

Django runs inside of a Gunicorn WSGI app server using a Postgres database. An Nginx reverse proxy sends outside requests to the Gunicorn server for processing. 

## Project Structure
The complete Django project is broken up into apps in the following way:
* Accounts - Custom User set up
* Blog - Basic weblog application
* Config - Common Django project settings etc.
* Contact - E-mail contact form
* Pages - Static pages (Home, About, etc.)
* Sewing - Product gallery & detail application detailing some of my sewing work
* Tags - M2M Content Tagging System
