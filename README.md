# Visual Novel

- Extract .rpa files
- Unobfuscate .rpyc files

## Usage

- Extract .rpa files
```
python rpatool.py -x /Users/brad/Library/Application\ Support/Steam/steamapps/common/Doki\ Doki\ Literature\ Club/game/images.rpa -o extract
```

- Unobfuscate .rpyc files
```
python2.7 unrpyc.py ../extract_script/script-ch0.rpyc
```

## Reference

- https://github.com/Shizmob/rpatool/
- https://github.com/CensoredUsername/unrpyc
- https://www.renpy.org/
