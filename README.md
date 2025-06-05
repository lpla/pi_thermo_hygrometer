# Raspberry Pi Thermo-Hygrometer
Use your Raspberry Pi as a Thermo-Hygrometer using BME280 and SSD1306 modules.

Note: be sure those modules are connected and the I2C interface is active through `raspi-config`.

Install basic dependences with `sudo apt install git python3-pip libjpeg-dev` (`libjpeg-dev` is only neeeded for the Python dependency `pillow` that is compiled in some environments).
Also, for some `pillow` compilations, some more dependencies are needed: `sudo apt install libfreetype6-dev libopenjp2-7-dev`
Then `git clone https://github.com/lpla/pi_thermo_hygrometer.git && cd pi_thermo_hygrometer` to download the code.

Use `sudo pip install --upgrade RPi.GPIO --break-system-packages` and `sudo pip install -r requirements.txt --break-system-packages` to install the Python dependencies (sorry not sorry about `--break-system-packages`).

Read comments in `ssd1306_bme280_info.py` code to modify the values for your specific setup (like the I2C bus, as I have two configured in 1 and 11) and modules models. For a different locale, first install the desired ones with `sudo dpkg-reconfigure locales`

Once you got it working from command line (a simple `python3 ssd1306_bme280_info.py` should be enough), if you want to run it from Raspberry boot, just run `sudo crontab -e` (it will open crontab file with your default editor), add this line at the end:

```
@reboot python3 /home/pi/pi_thermo_hygrometer/ssd1306_bme280_info.py &
```

And then reboot to check if it works fine without any human intervention.

Keep it cool!
