server:
	flask run

migrations:
	flask db init

migrate:
	flask db migrate	

upgrade:
	flask db migrate
		