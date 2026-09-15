# TA Chirp Correction

A reproducible Python/Jupyter workflow for wavelength-dependent time-zero
(chirp) correction of transient absorption (TA) data.

## Scope

This project provides a workflow to:

1. Read sample and solvent TA data from CSV files.
2. Check the wavelength and delay-time axes.
3. Select chirp points from the early-time solvent map.
4. Fit the wavelength-dependent time-zero function \(t_0(\lambda)\).
5. Apply the solvent-derived chirp correction to the sample data.
6. Export the corrected TA data and diagnostic figures.

The sample data are not independently chirp-fitted. The chirp correction
applied to the sample is determined only from the solvent measurement.

## Data format

The input CSV files should have the following format:

- The first row contains delay time in ps.
- The first column contains wavelength in nm.
- The remaining matrix contains the TA signal.
- Sample and solvent must have the same wavelength axis.
- Sample and solvent may have different delay-time axes.

## Project structure

```text
TA-chirp-correction/
├── README.md
├── notebooks/
├── src/
│   └── ta_chirp/
├── tests/
├── docs/
└── data/
    └── example/