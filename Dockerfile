FROM openlake/spark-py:3.3.1
USER root

# JVM which runs Hadoop needs a custom ca certificate
COPY cert/ca.crt .
RUN keytool -import -trustcacerts -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit -noprompt -alias tls -file ca.crt

WORKDIR /app
RUN pip3 install pyspark==3.3.1
COPY src/*.py .
