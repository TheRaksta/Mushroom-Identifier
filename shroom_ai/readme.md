# 🍄 Shroom AI - Mushroom Classification System

## Overview
Shroom AI is a machine learning-powered application that helps identify mushrooms using computer vision. The system:
1. Determines if a mushroom is edible or not
2. For edible mushrooms, identifies the most likely species
3. Provides confidence scores for all predictions

⚠️ **IMPORTANT SAFETY NOTICE**: This tool is for educational purposes only. Never consume wild mushrooms based solely on AI predictions. Always consult with professional mycologists for mushroom identification.

## 🏗️ Architecture
The project consists of two main components:
- **Frontend**: A Streamlit web application for image upload and result display
- **Backend**: A FastAPI service running two ML models:
  - Edibility detection model
  - Species identification model (activated only for edible mushrooms)

## 🛠️ Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose (for containerized deployment)
- Make (for using the provided Makefile)
- At least 4GB of RAM
- 10GB of free disk space

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/shroom_ai.git
cd shroom_ai
```

### 2. Initial Setup
```bash
# Create models directory and check requirements
make init-models

# Set up development environment
make setup
```

### 3. Add Required Models
Add in your own model files in the `models/` directory:
- `edible_detector.h5`: Mushroom edibility classification model
- `species_detector.h5`: Mushroom species identification model

### 4. Start the Application
```bash
# Start in development mode (Docker by default)
make dev

# Or start in local mode
make dev-local
```

Visit `http://localhost:8501` to access the web interface.

## 🛠️ Makefile Commands

The project includes a Makefile to streamline setup and execution. Here are the available commands:

### Primary Command
```bash
make setup-and-run
```
This is the main command you should use. It will:
1. Check if Python 3.10+ is installed
2. Verify Docker and Docker Compose installation
3. Confirm all requirement files are present
4. Verify ML models are in place
5. Start the application if all checks pass

When running this command, you'll see status updates like:
```bash
Checking Python installation...
✓ Python 3.10 or higher is installed (3.10.2)

Checking Docker installation...
✓ Docker and Docker Compose are installed

Checking dependencies...
✓ All requirement files present

Verifying ML models...
✓ All required models present

All checks passed! Starting application...
```

If any requirements are missing, you'll receive clear instructions on what needs to be added.

### Additional Commands

```bash
# Stop the application
make stop

# Clean up temporary files and stop containers
make clean

# Display help information
make help
```

### Common Issues and Solutions

1. **Missing Models**
   ```bash
   ✗ Missing required models:
     - edible_detector.h5 (Mushroom edibility classification model)
     - species_detector.h5 (Mushroom species identification model)
   ```
   Solution: Add the required model files to the `models/` directory

2. **Docker Not Running**
   ```bash
   ✗ Docker is not installed
   ```
   Solution: Install Docker and Docker Compose

3. **Python Version**
   ```bash
   ✗ Python 3.10 or higher is required
   ```
   Solution: Install or upgrade to Python 3.10+

### Best Practices
- Always use `make setup-and-run` for the initial setup and running the application
- Use `make stop` to properly shut down the application
- If you encounter any issues, run `make clean` and try again

## 🎯 Usage Guide

1. Access the web interface at `http://localhost:8501`
2. Upload a mushroom image using the file uploader
3. Click "Classify" to analyze the image
4. Review the results:
   - Edibility status and confidence score
   - If edible, top 3 likely species with confidence scores
   - Safety warnings and recommendations

## 🐳 Docker Configuration

The application uses Docker Compose with two services:
- Frontend (Streamlit) on port 8501
- Backend (FastAPI) on port 8000

## 📁 Project Structure
```
shroom_ai/
├── backend/               # FastAPI backend service
│   ├── config/           # Backend configuration
│   └── services/         # Core services (image & model)
├── frontend/             # Streamlit web interface
├── models/               # ML model files
├── Makefile             # Build and development commands
└── docker-compose.yml   # Docker services configuration
```

## 🔒 Security Notes
- The application includes safety warnings about mushroom consumption
- Model predictions should never be the sole basis for mushroom consumption
- Always verify mushroom identification with experts

## 🐛 Troubleshooting

### Common Issues
1. **Missing Models**
   ```bash
   make init-models  # Check model requirements
   ```

2. **Docker Issues**
   ```bash
   make clean       # Clean and restart
   make dev         # Start fresh
   ```

3. **Port Conflicts**
   - Ensure ports 8000 and 8501 are available
   - Modify docker-compose.yml if needed

### Error Messages
- "Model not found": Place required models in models/ directory
- "Connection refused": Ensure both services are running
- "Out of memory": Increase Docker memory allocation

## 📚 Development Notes

### Best Practices
- Always use `make format` before committing
- Check logs using `make logs` when debugging
- Use `make clean` to reset the environment
