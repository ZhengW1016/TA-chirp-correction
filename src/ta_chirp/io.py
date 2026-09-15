import pandas as pd


def read_ta_csv(file_path):
    """
    Read a transient absorption CSV file.

    The CSV format is:
    - first row: delay time
    - first column: wavelength
    - inner part: TA signal
    """

    data = pd.read_csv(file_path, header=None)

    delay_ps = data.iloc[0, 1:].astype(float).to_numpy()

    wavelength_nm = data.iloc[1:, 0].astype(float).to_numpy()

    signal = data.iloc[1:, 1:].astype(float).to_numpy()

    return wavelength_nm, delay_ps, signal