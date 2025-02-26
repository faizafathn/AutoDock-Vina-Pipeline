# AutoDock-Vina-Pipeline

## Overview
This project provides an automated pipeline for molecular docking using **AutoDock Vina**. It allows batch docking of multiple receptor-ligand pairs, making it efficient for virtual screening.

## Features
- **Automated preparation** of receptors and ligands.
- **Batch docking** of multiple receptor-ligand pairs.
- **Log files** generated for each docking run.
- **Results management** in organized directories.

## Installation
### **Prerequisites**
Ensure you have the following installed:
- **Python 3.x**
- **AutoDock Vina**
- **AutoDock Tools** (for preparing receptor/ligand files)

Install dependencies (if required):
```bash
pip install numpy pandas

## Usage
<<<<<<< HEAD


=======
### *1. Prepare Input Files*
- **Place receptor .pdbqt files in your working directory.**
- **Place ligand .pdbqt files in your working directory.**
- **Create a config.txt file with Vina docking parameters.
 ced98b8 (Added README.md)

### *2. Run the Pipeline*

'''bash
python autodock_vina_pipeline.py

### *3. Output
Results will be stored in the results/ directory.

## Confirguration
Modify the config.txt file to define docking parameters such as:

center_x = 10
center_y = 20
center_z = 30
size_x = 40
size_y = 40
size_z = 40
exhaustiveness = 8
num_modes = 9
energy_range = 3
