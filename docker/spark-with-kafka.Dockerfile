FROM apache/spark:3.5.3

ENV MAVEN_SPARK_SQL_KAFKA=https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.3/spark-sql-kafka-0-10_2.12-3.5.3.jar \
    MAVEN_SPARK_STREAMING_KAFKA=https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.12/3.5.3/spark-streaming-kafka-0-10-assembly_2.12-3.5.3.jar \
    MAVEN_KAFKA_CLIENTS=https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.8.0/kafka-clients-3.8.0.jar \
    MAVEN_COMMON_POOL=https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.9.0/commons-pool2-2.9.0.jar

RUN wget -P ${SPARK_HOME}/jars ${MAVEN_SPARK_SQL_KAFKA}; \
    wget -P ${SPARK_HOME}/jars ${MAVEN_SPARK_STREAMING_KAFKA}; \
    wget -P ${SPARK_HOME}/jars ${MAVEN_KAFKA_CLIENTS}; \
    wget -P ${SPARK_HOME}/jars ${MAVEN_COMMON_POOL}

