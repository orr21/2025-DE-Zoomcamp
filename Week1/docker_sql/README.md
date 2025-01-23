# Docker SQL Data Ingestion

This project demonstrates how to automate data ingestion into a PostgreSQL database running in a Docker container. The provided `data_ingestion.ipynb` notebook explains the ingestion process conceptually, while the actual implementation is handled in the `code` directory.

## Folder Structure

```
.
├── HOMEWORK.md               # Homeworks Week1
├── code                      # Source code for the ingestion pipeline
│   ├── Dockerfile            # Dockerfile for the ingestion service
│   ├── ingest_data.py        # Python script for data ingestion
│   └── requirements.txt      # Python dependencies
├── data                      # Placeholder for raw data files
├── data_ingestion.ipynb      # Notebook explaining the ingestion process
├── docker-compose.yml        # Compose file to manage services
├── imgs                      # Images for documentation
│   ├── Screenshot1.png       # Various screenshots
│   └── ...
└── requirements.txt          # Additional Python dependencies
```

## Getting Started

### Prerequisites

Make sure you have the following installed:

1. **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
2. **Docker Compose**: [Get Docker Compose](https://docs.docker.com/compose/install/)
3. **Python**: [Download Python](https://www.python.org/downloads/) (Optional, for running the notebook locally)

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/orr21/2025-DE-Zoomcamp.git
   cd 2025-DE-Zoomcamp/Week1/docker_sql
   ```

2. **Start Services with Docker Compose**
   
   Run the following command to start the PostgreSQL and pgAdmin services:
   ```bash
   docker-compose up -d
   ```

   This will start a PostgreSQL container accessible on `localhost:5432`, and a pgAdmin container accessible on `localhost:5050`.

3. **Explore the Data**

   Use any PostgreSQL client to connect to the database and verify the data ingestion. Default credentials are:
   - **Host**: `localhost`
   - **Port**: `5432`
   - **Username**: `postgres`
   - **Password**: `postgres`
   - **Database**: `ny_taxi`

   Example CLI connection:
   ```bash
   psql -h localhost -p 5432 -U postgres -d ny_taxi
   ```

   Alternatively, access pgAdmin via `http://localhost:5050`:
   - **Email**: `admin@admin.com`
   - **Password**: `admin`

   Add a new server in pgAdmin:
   - **Host name/address**: `postgres`
   - **Port**: `5432`
   - **Maintenance database**: `postgres`
   - **Username**: `postgres`
   - **Password**: `postgres`

### Optional: Explore the Notebook

The `data_ingestion.ipynb` notebook explains the ingestion process step by step. Open it in Jupyter Notebook to review:

```bash
jupyter notebook data_ingestion.ipynb
```

## Notes

- Ensure the data files are present in the `data` folder before running the ingestion script.
- Modify the database connection settings in `ingest_data.py` if using custom credentials.

## Screenshots

The `imgs` directory contains visual to prove homework answers.

## Stopping Services

To stop the PostgreSQL and pgAdmin containers, run:
```bash
docker-compose down
