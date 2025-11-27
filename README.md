# Kafka Learning Project

This project is a simple demonstration of a Kafka producer and consumer using Python with `aiokafka` and a `FastAPI` web server.

## Project Structure
The project is organized to separate the application source code from project-level configuration.

```
kafka-learning/
├── app/
│   ├── __init__.py         # Makes 'app' a Python package
│   ├── consumer.py         # Kafka consumer script
│   ├── main.py             # FastAPI application
│   ├── producer.py         # Kafka producer service
│   └── requirements.txt    
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.7+
- A running Kafka instance (e.g., using Docker).
- An "events" topic created in Kafka.

## Setup

1.  **Clone the repository** (if you are working with git) and navigate into the project directory.

2.  **Create and activate a virtual environment.** The project is set up to use a `venv` directory inside the `app` folder.

    ```bash
    # On Windows
    python -m venv app/venv
    app\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv app/venv
    source app/venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r app/requirements.txt
    ```

## Configuration

Currently, the Kafka bootstrap server is hardcoded to `localhost:9092` in both `app/producer.py` and `app/consumer.py`.

For a real-world application, it is recommended to move this configuration to environment variables or a configuration file.

## How to Run

You'll need two separate terminals to run the consumer and the producer (FastAPI server).

1.  **Run the Kafka Consumer:**
    In your first terminal, run the consumer script:
    ```bash
    python -m app.consumer
    ```
    You should see the message "Kafka consumer started...".

2.  **Run the FastAPI Producer:**
    In your second terminal, start the FastAPI server using `uvicorn`:
    ```bash
    uvicorn app.main:app --reload
    ```

3.  **Send a message:**
    You can now send a `POST` request to the `/publish` endpoint. Here is an example using `curl`:
    ```bash
    curl -X POST "http://127.0.0.1:8000/publish" -H "Content-Type: application/json" -d '{"key": "value", "another_key": 123}'
    ```

    In the consumer terminal, you should see the consumed message printed.