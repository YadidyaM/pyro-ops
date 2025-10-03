import pandas as pd
from pyro_ops.data_persistence import HDF5Store
from pyro_ops.analysis_core import rolling_zscore

# Synthetic CSV-like data
telemetry = pd.DataFrame({
    "time": pd.date_range("2025-01-01", periods=20, freq="T"),
    "temp_c": [20.0, 20.1, 20.2, 20.1, 20.0, 20.3, 20.4, 20.2, 20.1, 20.0, 20.1, 20.2, 20.1, 20.0, 21.5, 20.2, 20.1, 20.1, 20.0, 20.1],
})

# Compute rolling z-score on temp
telemetry["temp_z"] = rolling_zscore(telemetry["temp_c"], window=5)

# Persist to HDF5
store = HDF5Store("examples/telemetry_demo.h5")
store.write_table(
    "/payload/temp",
    telemetry,
    metadata={"unit": "C", "description": "Synthetic payload temperature with z-score"},
)
print("Wrote examples/telemetry_demo.h5 -> /payload/temp")
