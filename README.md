# pyopm150
[![License](https://img.shields.io/github/license/artifex-engineering/pyopm150)](https://github.com/artifex-engineering/pyopm150/blob/main/LICENSE)
![PyPI - Status](https://img.shields.io/pypi/status/pyopm150)
![PyPI - Version](https://img.shields.io/pypi/v/pyopm150)

**Python library for the Artifex Engineering OPM150**


## Installation
Install via pip:
```bash
pip install pyopm150
```

Install manually:
```bash
git clone https://github.com/artifex-engineering/pyopm150.git
cd pyopm150
pip install .
```

## Usage
```python
from pyopm150 import OPM150, GAIN, UNITS

# List all available devices
devices = OPM150.find_devices() # Get all available devices
print("Available Devices: {}\n\n".format(", ".join(devices) if len(devices) > 0 else "None"))

# Create OPM150 instance
opm = OPM150()

# Connect to first OPM150 device in list
opm.connect(devices[0])

# Set wavelength
opm.opm_set_wavelength(660)

# Set gain
opm.opm_set_gain(GAIN.X1)

# Set unit to use in measurements
opm.set_unit(UNITS.MICROAMPERE)

# Print single measurement
measurement = opm.opm_get_measurement()
print(f"{measurement[0]:.8f} {measurement[1]}")

opm.disconnect()
```

## Query current states and device informations
```python
print("Firmware version: {}".format(opm.opm_firmware_version))
print("Serial number: {}".format(opm.opm_serial_number))
print("Date of manufacturing: {}".format(opm.opm_date_of_manufacturing))
print("OPM150 is 100 kHz: {}\n\n".format(opm.opm_is_100khz))

print("Detector serial number: {}".format(opm.opm_detector_serial))
print("Detector min wavelength: {}".format(opm.opm_detector_min_wavelength))
print("Detector max wavelength: {}".format(opm.opm_detector_max_wavelength))
print("Detector is integrating sphere: {}\n\n".format(opm._opm_detector_is_integrating_sphere))

print("Device info:\n{}\n\n".format(opm.opm_get_info()))


print("Current wavelength: {}".format(opm.opm_get_wavelength()))
print("Current gain: {}".format(opm.opm_get_gain()))
print("Current Unit: {}".format(opm.unit))
print("Current filter factor: {}\n\n".format(opm.filter))
```

## nW/cm², µW/cm², mW/cm², W/cm²
```python
opm.set_unit(UNITS.MICROWATTS_PER_SQUARE_CENTIMETER) # Set unit to use in measurements

opm.aperture_in_mm = 7.0 # Set aperture in mm
print("Current Aperture in mm: {}".format(opm.aperture_in_mm)) # Print aperture in mm

measurement_value = opm.opm_get_measurement() # Get measurement value in specified unit
print("Measurement Value: {}{}".format(measurement_value[0], measurement_value[1])) # measurement value in specified unit
```

## Available Units
- **Nanoampere (nA)**: UNITS.NANOAMPERE
- **Microampere (µA)**: UNITS.MICROAMPERE
- **Milliampere (mA)**: UNITS.MILLIAMPERE
- **Ampere (A)**: UNITS.AMPERE
- **Nanowatts (nW)**: UNITS.NANOWATTS
- **Microwatts (µW)**: UNITS.MICROWATTS
- **Milliwatts (mW)**: UNITS.MILLIWATTS
- **Watts (W)**: UNITS.WATTS
- **Nanowatts per square centimeter (nW/cm²)**: UNITS.NANOWATTS_PER_SQUARE_CENTIMETER
- **Microwatts per square centimeter (µW/cm²)**: UNITS.MICROWATTS_PER_SQUARE_CENTIMETER
- **Milliwatts per square centimeter (mW/cm²)**: UNITS.MILLIWATTS_PER_SQUARE_CENTIMETER
- **Watts per square centimeter (W/cm²)**: UNITS.WATTS_PER_SQUARE_CENTIMETER
- **Decibel-milliwatts (dBm)**: UNITS.DECIBEL_MILLIWATTS

## Gain levels:
- **x1**: GAIN.X1
- **x10**: GAIN.X10
- **x100**: GAIN.X100
- **x1000**: GAIN.X1000
- **x10000**: GAIN.X10000
- **Auto**: GAIN.AUTO
