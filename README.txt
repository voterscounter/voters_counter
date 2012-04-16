Описание на русском и английском языках в этом файле эквивалентны.
Russian and English descriptions in this are equal.

Установка
Installation
=========
Требования к ПО
Requirements
---------------
* Ubuntu 10.04 (32-bit) (возможно работает на других Linux = should be compatible with other Linuxes)
* Python 2.6 (возможно работает на Python 2.4.x = probably compatible with Python 2.4.x, too)
* Django 1.3.x

Установка на Ubuntu 10.04 (32-bit)
Installation for Ubuntu 10.04 (32-bit)
----------------------------------
Для того, чтобы установить Voters Counter на Ubuntu необходимо выполнить
следующие действия:
In order to install Voters Counter for Ubuntu, please, do the following

1. [ОДНОКРАТНО] Установить Git:
1. [DONE ONCE] Install Git:
sudo apt-get install git-core

2. [ОДНОКРАТНО] Установить Apache HTTP Server:
2. [DONE ONCE] Install Apache HTTP Server:
sudo apt-get install apache2

3. [ОДНОКРАТНО] Установить mod_wsgi:
3. [DONE ONCE] Install mod_wsgi:
sudo apt-get install libapache2-mod-wsgi

4. [ОДНОКРАТНО] Создать и перейти в директорию, в которой будет размещаться Voters Counter:
4. [DONE ONCE] Create and change to directory where Voters Counter will reside:
mdkir /opt
cd /opt

5. [ОДНОКРАТНО] Получить исходный код из репозитория github:
5. [DONE ONCE] Get source from git repository at github:
[sudo] git clone git://github.com/voterscounter/voters_counter.git

6. [ОПЦИОНАЛЬНО] Получить актуальную версию исходного кода (если предыдущие шаги проделывались ранее):
6. [OPTIONAL] Get the latest sources (if previous steps are done before):
cd /opt/voters_counter
[sudo] git pull

7. [ОДНОКРАТНО] Создать конфигурационный файл для buildout:
7. [DONE ONCE] Create buildout configuration file:
sudo cp configuration/my.buildout.cfg.template my.buildout.cfg
sudo vim my.buildout.cfg
# Set VOTERS_COUNTER_ROOT = /opt/voters_counter
# Set VOTERS_COUNTER_DB_ROOT = /var/opt/voters_counter
# Если Вы указали деректорию отличную от /opt на шаге 4, то установите значения VOTERS_COUNTER_ROOT и
# VOTERS_COUNTER_DB_ROOT соответствующим образом
# If you used directory different than /opt at step 4, then set values of VOTERS_COUNTER_ROOT and
# VOTERS_COUNTER_DB_ROOT respectively

8. [ОПЦИОНАЛЬНО] Сделать резервную копию конфигурационного файла Apache HTTP Server:
8. [OPTIONAL] Backup Apache HTTP Server configuration file:
cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf.bak

9. Установить Django-приложение Voters Counter:
9. Install Voters Counter Django-application:
cd /opt/voters_counter
sudo python bootstrap.py
sudo ./bin/buildout -c my.buildout.cfg
sudo ./bin/deploy

Редактировать settings.py DEBUG = False