#!/bin/sh

mkdir /var/opt/voters_counter
cp -R voters_counter_project /var/opt/voters_counter
mkdir /var/opt/voters_counter/wsgi
cp django.wsgi /var/opt/voters_counter/wsgi
chown -R www-data /var/opt/voters_counter

cp apache2.conf /etc/apache2/apache2.conf

cp -R www/media /var/www
chown -R www-data /var/www

apache2ctl -k graceful

