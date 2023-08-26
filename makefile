up:
	@docker-compose down
	@sudo rm -r .data
	@docker-compose up --build fastapi 
	
initialize:
	@docker exec -w /usr/src fastapi alembic upgrade head
	@docker exec -w /usr/src/app fastapi python util/dump_construction_tbl.py
reload:
	@docker-compose up --build fastapi

kw-up: kw-build kw-run

kw-build:
	@docker build -t kw_svc -f kw_svc_docker.yml .

kw-run:
	@echo "Booting up Keyword service Docker Container"
	@docker run -it --gpus '"device=0"' --ipc=host --name kw_svc  -p 8000:8000 -v `pwd`/keyword_svc:/workspace/kw_svc kw_svc:latest /bin/bash

kw-rm:
	@docker rm kw_svc