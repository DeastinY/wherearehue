# wherearehue

Using [Phue](https://github.com/studioimaginaire/phue) and [whereami](https://github.com/kootenpv/whereami) to beat some brain into those Hue lamps.

## How to use
1. Install everything with `pip install -r requirements.txt`
2. Train `whereami` some rooms. The room name has to be part of the lamp name in Hue. `whereami learn -- workroom`
3. Press the link button on your Hue bridge and fire up `wherearehue`

Exmaple output:
```
Detected room workroom.
Turn on ['workroom drawing', 'workroom spot', 'workroom main'] ? (Y/n)
Turning lights on
Turn off all other lights ? (Y/n)
Turning lights off
```

Now feel free to bind the script to any hotkey of your laptop and toggle the lights wherever you are simply by pressing that button and hitting enter twice. (Checks can easily be removed)

## Important
- Detecting the room takes some time, don't think it's not working just because it takes a couple of seconds.
- The room detection is based on [whereami](https://github.com/kootenpv/whereami), check back there for issues with the precision of the detection
- The name of the trained rooms *has to match the room of the lights* (A config file will be added later)
