S?=base

up:
	docker compose up --detach

up-with-kafka:
	docker compose --profile kafka up --detach

up-with-kafka-ui:
	docker compose --profile kafka-ui up --detach

submit: up
	docker compose exec spark bash -c '/opt/spark/bin/spark-submit /opt/spark/work-dir/scripts/$(S).py > /opt/spark/work-dir/logs/$(S)_$$(date +%s).out 2>/opt/spark/work-dir/logs/$(S)_$$(date +%s).outerr'

submit-with-kafka: up-with-kafka
	docker compose exec spark bash -c '/opt/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-11_0.24:3.5.2 /opt/spark/work-dir/scripts/$(S).py > /opt/spark/work-dir/logs/$(S)_$$(date +%s).out 2>/opt/spark/work-dir/logs/$(S)_$$(date +%s).outerr'

down:
	docker compose down

clean:
	rm -rf logs/