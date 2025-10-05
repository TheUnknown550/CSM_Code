# Cardiac Self-Monitoring Tool (CS-M Tool) – Code Repository

## Overview
This repository contains the **experimental and testing code** for the CS-M Tool project, which aims to tackle **heart disease detection** through a combination of a custom recording device, a React Native app, and Neural Network AI. The focus here is on **AF detection, noise filtering, and algorithm testing**.

## Repository Structure

- **AF Algorithm/**  
  Contains scripts to implement and automatically test the AF detection algorithm.  

- **NoiseCancel/**  
  Scripts for noise cancellation and preprocessing heart sound data.  

- **Random_Python/**  
  Miscellaneous testing scripts related to AF detection experiments.  

- **Sounds/**  
  Sample heart sound files used for testing and training the AI.  

- **Test.py / Test copy.py**  
  Scripts to test AF detection workflows and validate results.  

- **.gitattributes**  
  Git configuration file.

## Recent file imports

On 2025-10-05 some content from a previously separate clone (the `Other/` folder) was consolidated into this repository to avoid duplication and make the project easier to manage. The moves were staged and some files were relocated into existing folders. A copy of the original `Other/` contents is preserved at `./staged_imports/Other_original` for review.

Key changes:

- WAV and audio files from `Other/` were moved into `./Sounds/`.
- `rnn_model.h5` was moved into `./AI/Models/`.
- `AICheckCompare.py` (from `Other/AI`) was moved into `./AI/`.
- `ExcelHighlight.py` was moved to `./Others/` at the repository root.
- The `ANC/` folder from `Other/` was moved to `./ANC_imported/`.
- The `AudioProcess/` folder from `Other/` was moved to the repository root as `./AudioProcess/`.

If anything looks misplaced or you want different organization (for example, renaming `ANC_imported/` to `ANC/` or merging certain notebooks into `NoiseCancel/`), tell me which folders to adjust and I will update the layout.
