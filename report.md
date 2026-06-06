# AquaGuard — Hybrid Intelligent Drowning Rescue System
## Smart Pool Monitoring Using Computer Vision and Data Analytics

# Project Report

## Team Members
- Ahmad — Pool Manager & Data Generation  
- Qusai — Alert Manager & Statistics  
- Abdalrahm — Visualizer & Main Pipeline  

# Project Overview

AquaGuard is a smart drowning detection and monitoring system that simulates a real-world pool surveillance environment. The system does not directly implement computer vision, but focuses on the data management and analytics layer of a full AI-based drowning detection system.

It handles pool configurations, drowning alert logging, data filtering and analysis, statistical reporting, and data visualization using charts.

# Objectives

The main objectives of this project are:
- Load and manage structured data using JSON and CSV
- Implement alert logging with validation rules
- Perform statistical analysis using Python
- Visualize data using Matplotlib
- Apply Object-Oriented Programming (OOP) principles
- Simulate a real-world AI safety monitoring system

# Project Structure

The project is organized into modular components:
- pool_manager.py → Handles pool and zone management
- alert_manager.py → Handles alert logging and analytics
- visualizer.py → Generates charts and visual reports
- main.py → Runs the full system pipeline
- create_sample_data.py → Generates test data
- requirements.txt → Lists dependencies

# Data Formats

## pools.json
Stores pool configurations including zones and camera assignments.

Each pool contains:
- Pool ID
- Name
- Dimensions
- Multiple zones with depth and camera mapping

## alerts.csv
Stores all drowning detection alerts.

Each record contains:
- Alert ID
- Pool ID and Zone ID
- Timestamp
- Confidence score
- Status (Rescued / False_Alarm / Missed)
- Response time in seconds

# System Workflow

The system follows this pipeline:
1. Load pool data from pools.json
2. Load alert logs from alerts.csv
3. Manage pools using PoolManager
4. Process and analyze alerts using AlertManager
5. Generate statistics and summaries
6. Visualize results using Visualizer

# Analytics Features

The system computes:
- Total number of alerts
- Number of rescued cases
- Number of false alarms
- Number of missed detections
- Average confidence score
- Average response time

# Data Visualization

Two main charts are generated:

## Bar Chart
Displays the number of alerts per Pool-Zone combination.

## Pie Chart
Shows distribution of alert statuses:
- Rescued
- False Alarm
- Missed

# Testing & Sample Data

A sample data generator (create_sample_data.py) is used to:
- Create realistic pool configurations
- Generate synthetic alert logs
- Enable system testing without real sensors

# How to Run the Project

1. Install dependencies:
pip install matplotlib

2. Generate sample data:
python create_sample_data.py

3. Run test file:
python test_project.py

4. Run full system (optional):
python main.py

# Key Technologies Used

- Python 3
- JSON handling
- CSV processing
- Object-Oriented Programming (OOP)
- Matplotlib for visualization
- Data analytics using pure Python

# Conclusion

AquaGuard demonstrates how structured data and analytics can be used to simulate a smart drowning detection system.

It provides insights into high-risk pool zones, system performance, alert accuracy, and response time.

This project represents a foundational layer for real-time AI-based safety systems in aquatic environments.