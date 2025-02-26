import os
import subprocess
from pathlib import Path

def prepare_receptor(receptor_pdb, output_pdbqt):
    """Prepare receptor file for docking."""
    command = f"prepare_receptor -r {receptor_pdb} -o {output_pdbqt}"
    subprocess.run(command, shell=True, check=True)

def prepare_ligand(ligand_pdb, output_pdbqt):
    """Prepare ligand file for docking."""
    command = f"prepare_ligand -l {ligand_pdb} -o {output_pdbqt}"
    subprocess.run(command, shell=True, check=True)

def run_docking(receptor_pdbqt, ligand_pdbqt, config_file, output_folder):
    """Run AutoDock Vina docking."""
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / "docking_output.pdbqt"
    log_file = output_path / "docking_log.txt"

    command = f"vina --receptor {receptor_pdbqt} --ligand {ligand_pdbqt} --config {config_file} --out {output_file} --log {log_file}"
    subprocess.run(command, shell=True, check=True)

def batch_docking(receptors, ligands, config_file, output_folder):
    """Run docking for multiple receptor-ligand pairs."""
    for receptor in receptors:
        for ligand in ligands:
            rec_name = Path(receptor).stem
            lig_name = Path(ligand).stem
            run_docking(receptor, ligand, config_file, f"{output_folder}/{rec_name}_{lig_name}")

def visualize_results(output_folder):
    """Placeholder for visualization function."""
    print(f"Results available in: {output_folder}")

def main():
    """Main workflow"""
    receptors = ["receptor1.pdbqt", "receptor2.pdbqt"]
    ligands = ["ligand1.pdbqt", "ligand2.pdbqt"]
    config_file = "config.txt"
    output_folder = "results"

    batch_docking(receptors, ligands, config_file, output_folder)
    visualize_results(output_folder)

if __name__ == "__main__":
    main()
