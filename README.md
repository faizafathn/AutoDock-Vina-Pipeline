# AutoDock Vina Docking Pipeline

## Overview
This project provides an automated molecular docking pipeline using **AutoDock Vina**. It streamlines receptor and ligand preparation, docking execution, and result organization.

## Features
- Batch docking for multiple receptor-ligand pairs
- Automated receptor and ligand preparation
- Error handling for missing files
- Output result organization
- Configurable docking parameters

## Requirements
- Python 3.7+
- AutoDock Vina
- MGLTools (for preparing receptor and ligand files)
- Required Python packages: `subprocess`, `os`, `pathlib`

## Installation
1. Install **AutoDock Vina** and **MGLTools**:
   ```bash
   sudo apt install autodock-vina
   ```
   Or manually download from [AutoDock Vina](https://vina.scripps.edu/).

2. Clone this repository:
   ```bash
   git clone https://github.com/faizafathn/AutoDock-Vina-Pipeline.git
   cd AutoDock-Vina-Pipeline
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Prepare receptor and ligand files:**
   ```bash
   prepare_receptor -r receptor.pdb -o receptor.pdbqt
   prepare_ligand -l ligand.pdb -o ligand.pdbqt
   ```

2. **Run docking manually:**
   ```bash
   python autodock_vina_pipeline.py --receptor receptor.pdbqt --ligand ligand.pdbqt --out output.pdbqt --log log.txt
   ```

3. **Run batch docking:**
   Modify `config.json` to specify receptor and ligand files, then execute:
   ```bash
   python autodock_vina_pipeline.py --config config.json
   ```

## Output
Results will be stored in the `results/` directory, with docking output and log files organized for each receptor-ligand pair.

