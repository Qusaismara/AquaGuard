# AquaGuard — Hybrid Intelligent Drowning Rescue System

## Senior Project Title
Smart Pool Monitoring Using Computer Vision and Data Analytics

## Student Information
- Ahmad Nazzal— ID: [202210827] — Pool Manager & Data Generation  
- Qusai Smara — ID: [202210188] — Alert Manager & Statistics  
- Abdalrahm Abdalqader — ID: [202210769] — Visualizer & Main Pipeline  

---

## Project Description

AquaGuard is a Python-based simulation system for smart drowning detection and pool monitoring analytics.

The system focuses on:
- Managing pool configurations and zones
- Logging and analyzing drowning alerts
- Computing statistical insights
- Visualizing alert data using charts

It simulates the backend data layer of an AI-powered real-time drowning detection system.

---

## Project Structure

- pool_manager.py → Handles pools and zones
- alert_manager.py → Handles alert logging and statistics
- visualizer.py → Generates charts (bar + pie)
- main.py → Runs the full system
- create_sample_data.py → Generates sample JSON/CSV data
- pools.json → Pool configuration data
- alerts.csv → Alert logs
- requirements.txt → Required Python packages
- report.md → Full project report

---

## Requirements

Install required library:

```bash
pip install matplotlib