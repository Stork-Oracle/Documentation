from Crypto.Hash import keccak
import os
import requests

PUBLIC_REST_BASE_URL = "https://public-rest.jp.stork-oracle.network"
TABLE_HEADERS = ["Asset ID", "Category", "Encoded Asset ID"]


def keccak256(data: str) -> str:
    k = keccak.new(digest_bits=256)
    k.update(data.encode("utf-8"))
    return "0x" + k.hexdigest()


def markdown_table(table_headers, rows):
    header_row = "| " + " | ".join(table_headers) + " |"
    separator = "|" + "|".join("-" * (len(h) + 2) for h in table_headers) + "|"

    data_rows = ["| " + " | ".join(row) + " |" for row in rows]

    return "\n".join([header_row, separator, *data_rows])


def build_asset_md_table(stork_rest_base_url):
    resp = requests.get(f"{stork_rest_base_url}/v1/assets")
    resp.raise_for_status()
    assets = resp.json()["data"]

    rows = [
        (asset["asset_id"], asset["category"], keccak256(asset["asset_id"]))
        for asset in sorted(assets, key=lambda a: a["asset_id"])
    ]

    return markdown_table(TABLE_HEADERS, rows)


if __name__ == "__main__":
    stork_rest_base_url = os.getenv("STORK_PUBLIC_REST_BASE_URL", PUBLIC_REST_BASE_URL)
    print(build_asset_md_table(stork_rest_base_url))
