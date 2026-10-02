import requests
from pathlib import Path

url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"

output_dir = Path("data/")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "input.txt"

response = requests.get(url)
response.raise_for_status()

output_file.write_bytes(response.content)

print(f"Downloaded to: {output_file}")
print(f"Size: {output_file.stat().st_size / 1024:.2f} KB")