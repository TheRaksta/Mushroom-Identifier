# Makefile for Shroom AI Project

# Configuration Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
DOCKER_COMPOSE := docker-compose
DOCKER := docker
PROJECT_NAME := shroom_ai

# Directory structure
MODELS_DIR := models
MODEL_EDIBLE := $(MODELS_DIR)/edible_detector.h5
MODEL_SPECIES := $(MODELS_DIR)/species_detector.h5

# Requirements files
REQUIREMENTS_BACKEND := backend/requirements.txt
REQUIREMENTS_FRONTEND := frontend/requirements.txt
REQUIREMENTS_ROOT := requirements.txt

# Checklist tracking
CHECKS_DIR := .checks
SETUP_COMPLETE_FILE := $(CHECKS_DIR)/setup_complete

# Colors for pretty printing
CYAN := "\033[0;36m"
GREEN := "\033[0;32m"
YELLOW := "\033[0;33m"
RED := "\033[0;31m"
NC := "\033[0m" # No Color

.PHONY: all help setup-and-run check-python check-docker check-deps verify-models clean stop

# Default target
all: help

# Help message
help:
	@echo $(CYAN)"Shroom AI - Mushroom Classification Project"$(NC)
	@echo ""
	@echo "Available commands:"
	@echo "  make setup-and-run  - Check requirements, setup environment, and run application"
	@echo "  make clean          - Stop containers and clean temporary files"
	@echo "  make stop           - Stop running containers"
	@echo ""
	@echo $(YELLOW)"Required Model Files (place in models/ directory):"$(NC)
	@echo "  - edible_detector.h5  (Mushroom edibility classification model)"
	@echo "  - species_detector.h5 (Mushroom species identification model)"

# Main setup and run command
setup-and-run: check-python check-docker check-deps verify-models
	@if [ -f $(SETUP_COMPLETE_FILE) ]; then \
		echo $(GREEN)"All checks passed! Starting application..."$(NC); \
		$(DOCKER_COMPOSE) up --build; \
	else \
		echo $(RED)"Setup incomplete. Please address the issues above before running the application."$(NC); \
		exit 1; \
	fi

# Check Python installation
check-python:
	@echo $(CYAN)"Checking Python installation..."$(NC)
	@if command -v $(PYTHON) >/dev/null 2>&1; then \
		python_version=$$($(PYTHON) -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'); \
		if [ $$(echo "$$python_version >= 3.10" | bc -l) -eq 1 ]; then \
			echo $(GREEN)"✓ Python 3.10 or higher is installed ($$python_version)"$(NC); \
			mkdir -p $(CHECKS_DIR); \
			touch $(CHECKS_DIR)/python_check; \
		else \
			echo $(RED)"✗ Python 3.10 or higher is required (found $$python_version)"$(NC); \
			rm -f $(CHECKS_DIR)/python_check; \
			exit 1; \
		fi \
	else \
		echo $(RED)"✗ Python is not installed"$(NC); \
		rm -f $(CHECKS_DIR)/python_check; \
		exit 1; \
	fi

# Check Docker installation
check-docker:
	@echo $(CYAN)"Checking Docker installation..."$(NC)
	@if command -v docker >/dev/null 2>&1; then \
		if command -v docker-compose >/dev/null 2>&1; then \
			echo $(GREEN)"✓ Docker and Docker Compose are installed"$(NC); \
			mkdir -p $(CHECKS_DIR); \
			touch $(CHECKS_DIR)/docker_check; \
		else \
			echo $(RED)"✗ Docker Compose is not installed"$(NC); \
			rm -f $(CHECKS_DIR)/docker_check; \
			exit 1; \
		fi \
	else \
		echo $(RED)"✗ Docker is not installed"$(NC); \
		rm -f $(CHECKS_DIR)/docker_check; \
		exit 1; \
	fi

# Check dependencies
check-deps:
	@echo $(CYAN)"Checking dependencies..."$(NC)
	@missing_files="" ; \
	for file in $(REQUIREMENTS_BACKEND) $(REQUIREMENTS_FRONTEND) $(REQUIREMENTS_ROOT); do \
		if [ ! -f $$file ]; then \
			missing_files="$$missing_files\n  - $$file"; \
		fi \
	done ; \
	if [ ! -z "$$missing_files" ]; then \
		echo $(RED)"✗ Missing requirement files:$$missing_files"$(NC); \
		rm -f $(CHECKS_DIR)/deps_check; \
		exit 1; \
	else \
		echo $(GREEN)"✓ All requirement files present"$(NC); \
		mkdir -p $(CHECKS_DIR); \
		touch $(CHECKS_DIR)/deps_check; \
	fi

# Verify models
verify-models:
	@echo $(CYAN)"Verifying ML models..."$(NC)
	@missing_models="" ; \
	if [ ! -d $(MODELS_DIR) ]; then \
		echo $(YELLOW)"Creating models directory..."$(NC); \
		mkdir -p $(MODELS_DIR); \
	fi; \
	if [ ! -f $(MODEL_EDIBLE) ]; then \
		missing_models="$$missing_models\n  - edible_detector.h5 (Mushroom edibility classification model)"; \
	fi; \
	if [ ! -f $(MODEL_SPECIES) ]; then \
		missing_models="$$missing_models\n  - species_detector.h5 (Mushroom species identification model)"; \
	fi; \
	if [ ! -z "$$missing_models" ]; then \
		echo $(RED)"✗ Missing required models:$$missing_models"$(NC); \
		echo $(YELLOW)"\nAction Required:"$(NC); \
		echo "Please add the missing model files to the $(MODELS_DIR)/ directory"; \
		echo "Contact your team lead or check documentation for obtaining these models"; \
		rm -f $(CHECKS_DIR)/models_check; \
		exit 1; \
	else \
		echo $(GREEN)"✓ All required models present"$(NC); \
		mkdir -p $(CHECKS_DIR); \
		touch $(CHECKS_DIR)/models_check; \
	fi
	@if [ -f $(CHECKS_DIR)/python_check ] && \
	    [ -f $(CHECKS_DIR)/docker_check ] && \
	    [ -f $(CHECKS_DIR)/deps_check ] && \
	    [ -f $(CHECKS_DIR)/models_check ]; then \
		touch $(SETUP_COMPLETE_FILE); \
	fi

# Stop running containers
stop:
	@echo $(CYAN)"Stopping all containers..."$(NC)
	$(DOCKER_COMPOSE) down
	@echo $(GREEN)"All containers stopped!"$(NC)

# Clean temporary files and stop containers
clean:
	@echo $(CYAN)"Cleaning project..."$(NC)
	$(DOCKER_COMPOSE) down
	@rm -rf $(CHECKS_DIR)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@echo $(GREEN)"Clean complete!"$(NC)