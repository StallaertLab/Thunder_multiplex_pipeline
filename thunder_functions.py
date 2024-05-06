import numpy as np


def get_tile_all_channels(img_lif_list, ch_num_list, im_ind):
    """
    Extracts a single tile across all specified channels from a list of LIF (Leica Image File) images. Each channel's data
    from the specified tile index is retrieved and compiled into a list.

    Parameters:
    - img_lif_list (list of LIF images): The list of LIF image objects to process.
    - ch_num_list (list of int): A list specifying the number of channels for each image in `img_lif_list`.
    - im_ind (int): The index of the tile to extract from each image.

    Returns:
    - numpy.ndarray: An array where each element is the data for one channel of the specified tile, extracted from all given images.

    Notes:
    - The function assumes that each LIF image object has a method `get_frame` which retrieves data based on z-stack level (z),
      time point (t), channel (c), and mosaic tile index (m).
    - This function is designed to work with LIF files that have multiple mosaic tiles and channels.
    """
    tile_list = []
    for im,ch_num in zip(img_lif_list,ch_num_list):
        for ch in range(ch_num):
            t = np.array(im.get_frame(z=0, t=0, c=ch, m=im_ind))
            tile_list.append(t)
    return np.array(tile_list)


def create_tiles_99(img_lif_list, ch_num_list, frame_size=2048):
    """
    Extracts and rearranges individual tiles from lif files into a 9x9 grid format. Specifically designed for images tiled
    as circles within a 9x9 grid configuration, covering 69 collected tiles.

    Parameters:
    - img_lif_list (list): A list of lif images from which tiles are extracted.
    - ch_num_list (list): A list indicating the number of channels in each image from img_lif_list.
    - frame_size (int, optional): The dimension of each frame in pixels. Default is 2048 pixels.

    Returns:
    - list: A list of numpy arrays, each representing a tile. The tiles are arranged to form a 9x9 grid, where certain positions
      in the grid (corners) are filled with zero arrays to maintain the grid shape.

    Notes:
    - The grid positions that are not directly filled with image data from the lif files are filled with zero arrays of the
      same dimensions to preserve the 9x9 grid shape.
    - The function relies on a helper function `get_tile_all_channels` to extract tile data for each relevant grid position.
    """
    total_channels = sum(ch_num_list)
    tile_index = 0
    tiles = []

    # Row configuration for the 9x9 grid
    row_config = {
        0: (2, 5, 2),
        1: (1, 7, 1),
        7: (1, 7, 1),
        8: (2, 5, 2)
    }

    # Create the tiles for each row in the 9x9 grid
    for row in range(9):
        left_zeros, real_tiles, right_zeros = row_config.get(row, (0, 9, 0))

        # Add left zero tiles
        tiles.extend(np.zeros((total_channels, frame_size, frame_size), dtype='uint16') for _ in range(left_zeros))

        # Add real tiles from the lif images
        for _ in range(real_tiles):
            tile = get_tile_all_channels(img_lif_list, ch_num_list, tile_index)
            tiles.append(tile)
            tile_index += 1

        # Add right zero tiles
        tiles.extend(np.zeros((total_channels, frame_size, frame_size), dtype='uint16') for _ in range(right_zeros))

    return tiles