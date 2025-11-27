# Kafka Learning Environment

This project provides a simple, single-node Kafka and Zookeeper setup using Docker Compose. It's designed for local development and for learning Apache Kafka.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Services

This setup consists of two main services defined in `docker-compose.yml`:

- `zookeeper`: An instance of Zookeeper, which Kafka uses for managing and coordinating brokers.
- `kafka`: A single Kafka broker instance.

The Kafka broker is configured to be accessible from your host machine on `localhost:9092`.

## How to Use

### Start the Cluster

To start the Kafka and Zookeeper containers in detached mode, run the following command from the root of the project directory:

```bash
docker-compose up -d
```

### Stop the Cluster

To stop and remove the containers, networks, and volumes, run:

```bash
docker-compose down
```

## Interacting with Kafka

Once the cluster is running, you can use the Kafka command-line tools to interact with it. The following commands should be run from your terminal in the project directory.

### Create a Topic

Create a new topic named `my-topic` with one partition and a replication factor of one.

```bash
docker-compose exec kafka kafka-topics --create --topic my-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
docker-compose exec kafka kafka-topics --create --topic my-topic --bootstrap-server kafka:29092 --replication-factor 1 --partitions 1
```

### Produce Messages to a Topic

```bash
docker-compose exec kafka kafka-console-producer --topic my-topic --bootstrap-server localhost:9092
```

### Consume Messages from a Topic

```bash
docker-compose exec kafka kafka-console-consumer --topic my-topic --from-beginning --bootstrap-server localhost:9092
```