import json, os, requests, pathlib, sys

# List of iconic games with Lichess game IDs (these IDs are examples – replace with real IDs if needed)
GAMES = [
    {
        "name": "Immortal Game",
        "players": "Adolf Anderssen vs. Lionel Kieseritzky",
        "year": 1851,
        "event": "London",
        "lichess_id": "K8Zg2lXG"  # placeholder ID
    },
    {
        "name": "Kasparov vs. Topalov 1999",
        "players": "Garry Kasparov vs. Veselin Topalov",
        "year": 1999,
        "event": "Wijk aan Zee",
        "lichess_id": "3r3wK9L"  # placeholder
    },
    {
        "name": "Fischer vs. Byrne 1963",
        "players": "Bobby Fischer vs. Robert Byrne",
        "year": 1963,
        "event": "New York",
        "lichess_id": "5HcZnR2J"  # placeholder
    },
    {
        "name": "Morphy vs. Duke Karl/Count Isouard 1858",
        "players": "Paul Morphy vs. Duke Karl/Count Isouard",
        "year": 1858,
        "event": "Paris",
        "lichess_id": "J4a9b8C2"  # placeholder
    },
    {
        "name": "Lasker vs. Bauer 1889",
        "players": "Emanuel Lasker vs. Johann Bauer",
        "year": 1889,
        "event": "London",
        "lichess_id": "D7f3K1M0"  # placeholder
    },
    {
        "name": "Steinitz vs. von Bardeleben 1895",
        "players": "Wilhelm Steinitz vs. Curt von Bardeleben",
        "year": 1895,
        "event": "Hannover",
        "lichess_id": "9Ue3F6Bv"  # placeholder
    },
    {
        "name": "Botvinnik vs. Capablanca 1938",
        "players": "Mikhail Botvinnik vs. José Capablanca",
        "year": 1938,
        "event": "AVRO",
        "lichess_id": "R2b5Y8Lx"  # placeholder
    },
    {
        "name": "Tal vs. Botvinnik 1960",
        "players": "Mikhail Tal vs. Mikhail Botvinnik",
        "year": 1960,
        "event": "World Championship Match",
        "lichess_id": "A3c7D9E4"  # placeholder
    },
    {
        "name": "Anand vs. Topalov 2010",
        "players": "Viswanathan Anand vs. Veselin Topalov",
        "year": 2010,
        "event": "World Championship",
        "lichess_id": "6Zc1V4N8"  # placeholder
    },
    {
        "name": "Carlsen vs. Caruana 2018 World Championship Game 12",
        "players": "Magnus Carlsen vs. Fabiano Caruana",
        "year": 2018,
        "event": "World Championship",
        "lichess_id": "B9E2K3Q1"  # placeholder
    }
]

output_dir = pathlib.Path(__file__).parent.parent / "games"
output_dir.mkdir(parents=True, exist_ok=True)

for game in GAMES:
    gid = game["lichess_id"]
    url = f"https://lichess.org/game/export/{gid}.pgn"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        pgn_text = resp.text
        filename = f"{game['name'].replace(' ', '_').lower()}.pgn"
        (output_dir / filename).write_text(pgn_text, encoding="utf-8")
        print(f"Saved {game['name']} → {filename}")
    except Exception as e:
        print(f"Failed to download {game['name']} (ID {gid}): {e}")

# Also write a metadata JSON for later use
metadata_path = pathlib.Path(__file__).parent.parent / "data" / "games.json"
metadata_path.parent.mkdir(parents=True, exist_ok=True)
with metadata_path.open("w", encoding="utf-8") as f:
    json.dump(GAMES, f, indent=2)
    print(f"Wrote metadata to {metadata_path}")
