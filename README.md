# mute-sounds
 Custom server sound silentifier for Counter-Strike.
 This script searches for all `.wav` sound files recursively in `cstrike_downloads/sound` and then replaces them with `valve/sound/ambiance/_comma.wav`.
 *The script doesn't take into account .res files that could exclude sounds that are part of maps!

I also added a small piece of code to test different methods to accomplish file scanning recursively. Results vary by OS, but os.walk() is generally the fastest option.

# Running
Set the path Half-Life in `settings.py`, and optinally path to a backup file. Then run `replace_sounds.py`.

```python
PATH_TO_HL = r"D:\SteamLibrary\steamapps\common\Half-Life"
PATH_TO_BACKUP = "D:\custom_sounds.zip"
EXCLUDE_DIRS = ['gungame']
```
```sh
python3 "replace_sounds.py"
```
