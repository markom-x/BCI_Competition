
import mne

raw = mne.io.read_raw_gdf("A01T.gdf", preload=True)
raw.filter(1., 40.).notch_filter(50.)
raw.plot(block=True, n_channels=22, title="BCIC IV-2a")

"""
import mne
raw_E = mne.io.read_raw_gdf("A01E.gdf", preload=True)
raw_E.filter(1., 40.).notch_filter(50.)
raw_E.plot(block=True, n_channels=22, title="BCIC IV-2a")
"""