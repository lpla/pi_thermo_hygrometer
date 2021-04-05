# Raspberry Pi Thermo-Hygrometer
Use your Raspberry Pi as a Thermo-Hygrometer using BME280 and SSD1306 modules.

Read comments in code to modify the values for your specific setup and modules models.

Once you got it working from command line, if you want to run it from Raspberry boot, just run `crontab -e` (it will open crontab file with your default editor), add this line at the end:

```
@reboot python3 /home/pi/pi_thermo_hygrometer/ssd1306_bme280_info.py &
```

And then reboot to check if it works without any human intervention.

Keep it cool!
