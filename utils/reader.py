from pathlib import Path

def reader(bot):
    data_folder = Path("data")
    lyrics_files = {
        file.stem: file.name
        for file in data_folder.glob("*.txt")
    }
    
    file_name = lyrics_files.get(bot)

    if file_name is None:
        raise ValueError(f"Unsupported bot: {bot}")
    
    file_path = data_folder / file_name

    with open(file_path, encoding="utf-8", errors="ignore") as f:
        lyrics = [lyric.replace('\\n','\n') for lyric in f]
    return lyrics