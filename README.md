# Bot-Timer

- Press & release to start the countdown.
- Press & release to pause / unpause.
- Hold & release to reset to idle state.

## Setup

Will require disabling some kernel modules - see https://github.com/jgarff/rpi_ws281x

## GPIO

- LED signal on pin 18 (remember to also tie other signal pin to ground https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/)
- Button between pin 12 & ground

## TODO

- [x] Implement basic timer logic
- [x] Implement states
- [x] Handle button input
- [ ] Add sound
  - [x] Countdown
  - [ ] Change countdown sound to something more copyright friendly?
  - [ ] End of round
- [ ] Tweak LEDs