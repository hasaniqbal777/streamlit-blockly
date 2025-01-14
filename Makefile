# Usage: $ make {command}

.ONESHELL:

.PHONY: serve-frontend
serve-frontend: 
	cd frontend && npm run dev

.PHONY: build-frontend
build-frontend: 
	cd frontend && npm run build

.PHONY: serve-streamlit
serve-streamlit: 
	PYTHONPATH="src:$$PYTHONPATH" streamlit run tests/app.py