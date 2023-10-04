# Icap test task
Test admin panel website made with Django

## Technologies used
* Django
* HTML
* Tailwind CSS

## Installation
* If you wish to run your own build, first ensure you have installed Python on your computer globally.
* If everything is installed, clone this repository to your computer:
```bash
https://github.com/TeraBasedProgrammer/icap-test-task
```
* Setup dependencies
  1. Cd into the project directory
      ```bash
      $ cd icap-test-task
      ```
  2. Create a python virtual environment
      ```bash
      $ python -m venv env
      ```
  3. Activate venv
     * Linux
     ```bash
     $ source env/bin/activate
     ```

     * Windows (run the file)
     ```bash
     $ env\Scripts\activate.bat
     ```
  4. Install dependencies
      ```bash
      $ pip install -r requirements.txt
      ```
* Run the application
  * Makefile
  ```bash
  $ make run
  ```
  or
  * manage.py
  ```bash
  $ python manage.py runserver 8000
  ```
## Usage

To apply migrations and create database use following command:

```bash
make migrate
```
or
```bash
python manage.py migrate
```

* For now, website has no data. To make it look like it has to be, you should type following command in terminal:

```bash
make setupdb
```
or
```bash
python manage.py setup-db
```
It will activate the script that will automatically set up the database.

* To clean the database use:
```bash
make resetdb
```
or
```bash
python manage.py reset-db
```



* To use website as administrator you should create a superuser:
In terminal write the following command:
```bash
$ python manage.py createsuperuser
```
Follow the steps, suggested by Django and then log in the system (localhost:8000/login/)