from pyopm150 import OPM150, GAIN, UNITS

devices = OPM150.find_devices() # Get all available devices
print("Available Devices: {}\n\n".format(", ".join(devices) if len(devices) > 0 else "None"))

opm = OPM150() # Create OPM150 instance
opm.connect(devices[0]) # Connect to first device in list

print("Firmware version: {}".format(opm.opm_firmware_version))
print("Serial number: {}".format(opm.opm_serial_number))
print("Date of manufacturing: {}".format(opm.opm_date_of_manufacturing))
print("OPM150 is 100 kHz: {}\n\n".format(opm.opm_is_100khz))

print("Detector serial number: {}".format(opm.opm_detector_serial))
print("Detector min wavelength: {}".format(opm.opm_detector_min_wavelength))
print("Detector max wavelength: {}".format(opm.opm_detector_max_wavelength))
print("Detector is integrating sphere: {}\n\n".format(opm.opm_detector_is_integrating_sphere))

print("Device info:\n{}\n\n".format(opm.opm_get_info()))

opm.opm_set_wavelength(660) # Set wavelength
opm.opm_set_gain(GAIN.X1) # Set gain

print("Current wavelength: {}".format(opm.opm_get_wavelength())) # Print current wavelength
print("Current gain: {}".format(opm.opm_get_gain())) # Print current gain

opm.set_unit(UNITS.MICROAMPERE) # Set unit to use in measurements
print("Current Unit: {}".format(opm.unit))

opm.filter = 1.0 # Set filter factor
print("Current filter factor: {}\n\n".format(opm.filter)) # Print filter factor


print("Raw measurement value: ".format(opm.opm_get_single_raw_measure())) # Get direct measurement value from device

measurement_value = opm.opm_get_measurement() # Get measurement value in specified unit
print("Measurement Value: {} {}\n\n".format(measurement_value[0], measurement_value[1])) # measurement value in specified unit

opm.opm_set_gain(GAIN.AUTO) # Set auto gain
print("Current gain: {}".format(opm.opm_get_gain())) # Print current gain

measurement_value = opm.opm_get_measurement() # Get measurement value in specified unit
print("Measurement Value: {}{}\n\n".format(measurement_value[0], measurement_value[1])) # measurement value in specified unit



# ONLY FOR nW/cm², µW/cm², mW/cm², W/cm²
opm.set_unit(UNITS.MICROWATTS_PER_SQUARE_CENTIMETER) # Set unit to use in measurements

opm.aperture_in_mm = 7.0 # Set aperture in mm
print("Current Aperture in mm: {}".format(opm.aperture_in_mm)) # Print aperture in mm

print("Current gain: {}".format(opm.opm_get_gain())) # Print current gain

measurement_value = opm.opm_get_measurement() # Get measurement value in specified unit
print("Measurement Value: {}{}".format(measurement_value[0], measurement_value[1])) # measurement value in specified unit


opm.disconnect()