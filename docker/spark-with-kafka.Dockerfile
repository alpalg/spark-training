FROM apache/spark:3.5.3

RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.3/spark-sql-kafka-0-10_2.12-3.5.3.jar
RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.12/3.5.3/spark-streaming-kafka-0-10-assembly_2.12-3.5.3.jar
RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.8.0/kafka-clients-3.8.0.jar