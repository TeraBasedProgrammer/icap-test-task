# Usage: make <command>

# Run django server
run:
	python manage.py runserver 8000

# Run django python shell
shell:
	python manage.py shell -i ipython

# Create django migrations
makemigr:
	python manage.py makemigrations

# Migrate django migrations
migrate:
	python manage.py migrate

# Create superuser
createuser:
	python manage.py createsuperuser

# Fill up the database
setupdb:
	python manage.py setup-db

# Clear the database
resetdb:
	python manage.py reset-db
