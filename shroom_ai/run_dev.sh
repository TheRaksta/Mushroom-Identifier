#!/bin/bash

# run_dev.sh
MODE=${1:-docker}  # Default to docker mode if no argument provided

if [ "$MODE" = "docker" ]; then
    echo "Starting services using Docker..."
    
    # Check if containers are already running
    if [ "$(docker-compose ps -q)" ]; then
        echo "Stopping existing containers..."
        docker-compose down
    fi
    
    # Build and start containers
    docker-compose up --build

elif [ "$MODE" = "local" ]; then
    echo "Starting services locally..."
    
    # Start backend
    echo "Starting FastAPI backend..."
    cd backend
    python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
    BACKEND_PID=$!
    
    # Wait for backend to start
    sleep 3
    
    # Start frontend
    echo "Starting Streamlit frontend..."
    cd ../frontend
    streamlit run streamlit_app.py --server.port 8501 &
    FRONTEND_PID=$!
    
    # Handle script termination
    trap "kill $BACKEND_PID $FRONTEND_PID" EXIT
    
    # Wait for either process to exit
    wait $BACKEND_PID $FRONTEND_PID

else
    echo "Invalid mode. Use 'docker' or 'local'"
    exit 1
fi