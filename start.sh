export SQLALCHEMY_DATABASE_URI='postgresql://jurassic:pass123@localhost/pitches'
export SECRET_KEY='WREWH9WEHGIOEHWGIOEHGNES'

# python3 manage.py shell
python manage.py server
# python manage.py db init
# python manage.py db migrate -m "schema"
# python manage.py db upgrade
# python manage.py db stamp heads