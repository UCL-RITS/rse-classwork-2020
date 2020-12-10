'''Analysis script for some DSEA measurements.'''

import os

from processing import analyse, is_valid, load, preprocess
from visualisation import fu_map, save_figure


def extract_mean(data_file):
    """Load a dataset, smooth it and run the analysis algorithm on it.

    :param data_file: input file containing raw data from an experiment.
    """
    assert os.path.exists(data_file), f"File not found: {data_file}"
    assert is_valid(data_file), f"File {data_file} not in DSEA format."
    data = load(data_file)
    # This smoothing is necessary to avoid singular behaviour, see Kim (2012)
    scaling = 0.3  # scaling factor to apply, from Reyes & Pace (2004)
    smoothed_data = preprocess(data, scaling)
    return analyse(smoothed_data)


if __name__ == "__main__":
    # The files from my last 3 experiments.
    # Note that we can't run this on the data from the MT-3 because the
    # files lack the header!
    raw_files = ['81500.tab', '48151.tab', '62342.tab']
    results = [extract_mean(input_file) for input_file in raw_files]
    for result in results:
        save_figure(fu_map(result))
