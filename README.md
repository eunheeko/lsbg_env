# README for lsbg project

updated as of Nov. 17, 2023

## Getting started

Download utility codes and data

### code
Use git clone to copy the repository
```
git clone https://github.com/eunheeko/lsbg_env.git
```
Or download a `utils` folder and necessary notebooks.

### data
- [download](https://www.dropbox.com/scl/fo/5jc4b85uio14u39c04f27/h?rlkey=6m46csyglk4i9r5vtz3pqntyb&dl=0)
    - `data` folder should be inside the workspace
### 


## Structures
* codes
    - utils/
        + `decomposition.py`: functions for fitting bulge & disck component of a input galaxy
        + `mistree.py`: class for running MST algorithm
        + `sdss.py`: conversion between `SDSS object ID` and `observation info`
        + `ufunc.py`: useful/miscellaneous functions
    - notebooks/
        + [1_LSBG_candidates.ipynb](1_LSBG_candidates.ipynb): LSBG candidates in Stripe82
        + [2_LSS_Alpasan14.ipynb](2_LSS_Alpasan14.ipynb): LSS identification method, following Alpasan+14
        + [3_LSS_effect_of_linking_length_and_minimum_halo_mass.ipynb](3_LSS_effect_of_linking_length_and_minimum_halo_mass.ipynb)
        + [4_results.ipynb](4_results.ipynb)
        + To be updated
    - data/
        + [download](https://www.dropbox.com/scl/fo/5jc4b85uio14u39c04f27/h?rlkey=6m46csyglk4i9r5vtz3pqntyb&dl=0)



## Notes
Further details can be found [here](notes.md)