## Managing environments

conda create -n myenv
conda install -n myenv scipy=0.15.0
conda activate myenv
conda deactivate


## Packages

# List packages
conda list

# Packages: env-game
conda install -c cogsci pygame

## Jupyter-lab 
conda install -c conda-forge jupyterlab

# Creating kernels for different env
conda activate cenv
conda install ipykernel
ipython kernel install --user --name=k-cenv
conda deactivate

# Change directory to D:
jupyter notebook --generate-config
# Edit in file c.NotebookApp.notebook_dir = "D:\Coding Projects\"  
