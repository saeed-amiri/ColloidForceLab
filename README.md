# ColloidForceLab
ColloidForceLab is a computational toolkit designed to simulate and analyze DLVO (Derjaguin-Landau-Verwey-Overbeek) potential interactions between colloidal particles. This project provides a robust framework for studying colloidal stability, particle aggregation, and the effects of various forces in colloidal systems.

## What:
Simulation of the aggregation of coated-silica nanoparticles (colloidal) at the water-oil interfaces in the presence of surfactants.

## Why:
Simulating the aggregation of many nanoparticles (NPs) with all-atom simulations is unfeasible due to computational limitations. Therefore, we need to use a different approach, such as coarse-graining. Here, we will simulate the situation in a 2D case only, treating NPs as single points with a radius.

## How:
The model will be built here, and the forces between the nanoparticles (NPs) will be computed using the GROMACS package. The final model will be simulated within LAMMPS.

## Strucure:
```
ColloidForceLab/
├── src/
│   ├── common/
│   │   └── logger.py
|   |   └── ...
├── tests/
│   ├── test_logger.py
|   |   └── ...
├── README.md
├── setup.py
```