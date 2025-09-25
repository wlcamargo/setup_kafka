# Setup Kafka 

## Project Description

This project demonstrates the use of **Apache Kafka** by integrating a simple Python-based frontend application with a Kafka consumer service.  

- The **frontend**, developed in Python (Streamlit), produces and sends messages to Kafka.  
- A **consumer**, also implemented in Python, subscribes to the Kafka topic, processes the incoming messages, and writes the data into **Amazon S3 / Minio**.  

The goal is to provide a practical example of how Kafka can be used for message streaming between applications and cloud storage.

## Setup and Run

### Start Kafka with Docker Compose

Run the following command in the project root:

```bash
docker-compose up -d
```

This will start:

Check Kafka-UI at: [http://localhost:9007](http://localhost:9007)

### Requirements

- Docker and Docker Compose installed
- Python 3.8+
  
Install Python dependencies:

```bash
pip install -r requirements.txt
```

### app_producer.py

- streamlit application to generate data
- Sends messages to Kafka

#### how to run app?
```
streamlit run app_producer.py
```

link: [http://localhost:8501](http://localhost:8501)

### consumer_s3.py

- This script consumes messages from Kafka and stores the data in S3.

#### how to run consumer?
```
python consumer_s3.py
```

## References

https://kafka.apache.org/documentation

https://hub.docker.com/r/obsidiandynamics/kafka 

https://hub.docker.com/r/provectuslabs/kafka-ui

https://github.com/dpkp/kafka-python  

https://faker.readthedocs.io/en/master/

https://docs.streamlit.io/ 

https://docs.confluent.io/

https://whimsical.com/kafka-EbWjeGL3gDg9apxewMyGhB

https://softwaremill.com/kafka-visualisation/

## Developer

| Developer        | LinkedIn                                                                 | E-mail                  | Portfolio                               |
|------------------|--------------------------------------------------------------------------|--------------------------|-----------------------------------------|
| Wallace Camargo  | [LinkedIn](https://www.linkedin.com/in/wallace-camargo-35b615171/)       | wallacecpdg@gmail.com    | [Portfolio](https://wlcamargo.github.io/) |
