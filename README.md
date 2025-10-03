# Pyro‑Ops — Ground Ops and Telemetry Automation for SmallSats

[![PyPI](https://img.shields.io/pypi/v/pyro-ops.svg)](https://pypi.org/project/pyro-ops/)
[![CI](https://github.com/YadidyaM/pyro-ops/actions/workflows/ci.yml/badge.svg)](https://github.com/YadidyaM/pyro-ops/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Pyro‑Ops is a modular Python toolkit that turns raw spacecraft downlink into actionable insight and safe, repeatable operations. It standardizes CCSDS telemetry ingest, persists mission data to queryable HDF5 with metadata, provides baseline FDIR analytics (with optional ML), validates command sequences against mission definitions, and integrates with open ground infrastructure (e.g., SatNOGS) and orbit propagation libraries.

Why it exists: hardware and launch have been democratized; ground ops automation hasn’t. Many first missions burn critical time building ad‑hoc scripts to parse packets, wrangle storage, and hand‑craft commands. Pyro‑Ops focuses the ground segment into a reusable, testable, mission‑agnostic core you can trust and extend.

## Install

```bash
pip install pyro-ops
```

Optional extras:

- Orbits: `pip install pyro-ops[orbits]`
- XTCE: `pip install pyro-ops[xtce]`
- ML (batch): `pip install pyro-ops[ml]`
- ML (streaming): `pip install pyro-ops[ml_stream]`
- Space (astropy/sgp4/spiceypy): `pip install pyro-ops[space]`
- PUS tools: `pip install pyro-ops[pus]`
- Docs: `pip install pyro-ops[docs]`

## Quickstart

```python
from pyro_ops.analysis_core import rolling_zscore
from pyro_ops.data_persistence import HDF5Store

import pandas as pd

series = pd.Series([1, 1, 1, 10, 1, 1])
z = rolling_zscore(series, window=3)

store = HDF5Store("telemetry.h5")
store.write_table("/payload/temp", pd.DataFrame({"t": [1,2,3], "temp": [20.1, 20.5, 21.0]}), metadata={"unit": "C"})
```

## Architecture

- Data Interface: CCSDS packet decode wrappers (fixed/variable bitfields via `ccsdspy`)
- Data Persistence: HDF5 time‑series tables with mission metadata (MetaSat‑aligned)
- Analysis Core: FDIR utilities (e.g., rolling z‑score) and adapters for `scikit‑learn`, `river`, `pyod`
- Operations Control: Pythonic DSL with XTCE/eICD ingestion stubs for validation and serialization
- Ground Integration: SatNOGS scheduling (dry‑run by default) and orbit helpers (`skyfield`, `sgp4`, SPICE)

Design principles
- Separation of concerns across layers; stable interfaces; optional heavy deps via extras
- Safety first: no automatic uplink in examples/tests; network actions expose `dry_run`
- Reproducibility: pinned deps, CI, tests, and HDF5 as the default analysis substrate

## Roadmap (short)
- XTCE normalization and validation utilities
- PUS service helpers and examples with `spacepackets`
- Dataset loaders for ESA/OPSSAT‑AD/NASA telemetry benchmarks
- More streaming FDIR detectors and explainability hooks
- Expanded SatNOGS helpers and ground pass planners

## Who is it for?
- University teams and first‑time builders who want a reliable ground baseline
- Small teams scaling operations across satellites without scaling headcount
- Researchers evaluating FDIR algorithms on standardized telemetry layouts

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

## License

Apache-2.0
