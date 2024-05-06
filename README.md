# Thunder_general_pipeline
A general pipeline to quantify a multiplexed experiment from the Thunder microscope. 

**00_extract_tiles.ipynb**

input: 

- lif file containing all the rounds of the experiment

output: 

- individual tif files for each tile (WELL_r_ROUND_ch_CHANNEL_TILE)

**01_correct_illumination.ipynb**

input: 

- individual tif files for each tile (WELL_r_ROUND_ch_CHANNEL_TILE)

output: 

- individual tif files for each tile corrected for flatness of illuminaiton (WELL_r_ROUND_ch_CHANNEL_TILE)
- illumination patterns found with BASIC (for QC)


