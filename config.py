import os
import custom_defs

def read_config(file):
    default_settings = {
        "scanner": "firefly",
        "fwhm": "0.2",
        "sectral_sl": "0.05",
        "spacial_sl": "0.05",
        "custom_fwhm": False
    }
    if not os.path.isfile(file):
        print("Settings file cannot be found.")
        return default_settings
    loaded_settings = {}
    with open("settings.conf", "r") as f:
        for line in f:
            setting_data = line.split("=", 1)
            setting = setting_data[0].lower().strip()
            data = setting_data[1]
            if data.lower() == "true":
                data = True
            elif data.lower() == "false":
                data = False
            else:
                data.strip()
            loaded_settings[setting] = data
    for setting in loaded_settings:
        if setting not in default_settings:
            print("{} is not a known setting. This setting is ignored".format(setting))
        else:
            default_settings[setting] = loaded_settings[setting]
    return default_settings

def fwhm(spacial, spectral, function_type=None):
    fwhm_defs = {
        "default": fwhm,
        "option_2": fwhm2,
        "custom": custom_defs.fwhm
    }
    # if function_type is not None:
    #     return fwhm_defs[function_type](spacial, spectral)
    # else:
    #     return fwhm_default(spacial, spectral)
    if settings["custom_fwhm"]:
        return fwhm_defs["custom"](spacial, spectral)
    else:
        return fwhm_default(spacial, spectral)
    # print(fwhm_defs["default"](1, 2))
    # print(fwhm_defs["option_2"](1, 2))
    # print(fwhm_defs["custom"](1, 2))

def fwhm_default(spacial, spectral):
    return spacial*2 + spectral*100

def fwhm2(spacial, spectral):
    return spacial*1000 + spectral

def main():
    global settings
    settings = read_config("settings.conf")
    for setting in settings:
        print("{} is set to {}".format(setting, settings[setting]))
    # if settings["custom_fwhm"]:
    #     print("ok")
    #     fwhm(1, 2, function_type="custom")
    # else:
    #     fwhm(1, 2)
    # fwhm_defs = {
    #     "default": fwhm,
    #     "option_2": fwhm2,
    #     "custom": custom_defs.fwhm
    # }
    #
    # print(fwhm_defs["default"](1, 2))
    # print(fwhm_defs["option_2"](1, 2))
    # print(fwhm_defs["custom"](1, 2))
    print(fwhm(1, 2))

if __name__ == "__main__":
    main()