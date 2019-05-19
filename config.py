import os

def read_config(file):
    default_settings = {
        "scanner": "firefly",
        "fwhm": "0.2",
        "sectral_sl": "0.05",
        "spacial_sl": "0.05"
    }
    if not os.path.isfile(file):
        print("Settings file cannot be found.")
        return default_settings
    loaded_settings = {}
    with open("settings.conf", "r") as f:
        for line in f:
            setting_data = line.split("=", 1)
            setting = setting_data[0].lower().strip()
            data = setting_data[1].strip()
            loaded_settings[setting] = data
    for setting in loaded_settings:
        if setting not in default_settings:
            print("{} is not a known setting. This setting is ignored".format(setting))
        else:
            default_settings[setting] = loaded_settings[setting]
    return default_settings


def main():
    settings = read_config("settings.conf")
    for setting in settings:
        print("{} is set to {}".format(setting, settings[setting]))

if __name__ == "__main__":
    main()