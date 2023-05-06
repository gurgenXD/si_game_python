migrations-make: ## Создать миграцию базы данных.
	$(POETRY_RUN) python -m cli migrations make "Initial commit."

migrations-up: ## Накатить миграции.
	$(POETRY_RUN) python -m cli migrations up

migrations-down: ## Откатить последнюю миграцию.
	$(POETRY_RUN) python -m cli migrations down


start-api: ## Запусть API.
	python -m cli start api
