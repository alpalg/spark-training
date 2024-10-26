S?=base

up:
	docker compose up --detach

submit: up
	docker compose exec spark bash -c '/opt/spark/bin/spark-submit /opt/spark/work-dir/scripts/$(S).py > /opt/spark/work-dir/logs/$(S)_$$(date +%s).out 2>/opt/spark/work-dir/logs/$(S)_$$(date +%s).outerr'

down:
	docker compose down

clean:
	rm -rf logs/