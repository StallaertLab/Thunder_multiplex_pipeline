# Thunder_general_pipeline
A general pipeline to quantify a multiplexed experiment from the Thunder microscope. 

**00_extract_tiles.ipynb**

input: 

- lif file containing all the rounds of the experiment

output: 

- individual tif files for each tile (WELL_r_ROUND_ch_CHANNEL_TILE)

**01_correct_illumination_BaSiC.ipynb**

input: 

- individual tif files for each tile (WELL_r_ROUND_ch_CHANNEL_TILE)

output: 

- individual tif files for each tile corrected for flatness of illuminaiton (WELL_r_ROUND_ch_CHANNEL_TILE)
- illumination patterns found with BASIC (for QC)

**02_ASHLAR.ipynb**

input: 

- individual tif files for each tile corrected for flatness of illuminaiton (WELL_r_ROUND_ch_CHANNEL_TILE)
- a dictionary mapping round and channel to the biomarker name

output: 

- assembled and aligned images (WELL_ashlar_SIGNAL_NAME)


**03_segment_cellpose.ipynb**

input: 

- assembled and aligned images (WELL_ashlar_SIGNAL_NAME)

output: 

- segmented masks (WELL_mask)


**04_quantify_regionprops.ipynb**

input: 

- assembled and aligned images (WELL_ashlar_SIGNAL_NAME)
- segmented masks (WELL_mask)

output: 

- data frame with calculated object properties and median per image (background estimation)


