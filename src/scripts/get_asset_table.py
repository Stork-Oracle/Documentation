from Crypto.Hash import keccak
import os
import requests

TABLE_HEADERS = ["Asset ID", "Encoded Asset ID"]


def keccak256(data: str) -> str:
    k = keccak.new(digest_bits=256)
    k.update(data.encode("utf-8"))
    return "0x" + k.hexdigest()


def markdown_table(table_headers, rows):
    header_row = f"| {table_headers[0]} | {table_headers[1]} |"
    separator = f"|{'-' * (len(table_headers[0]) + 2)}|{'-' * (len(table_headers[1]) + 2)}|"

    data_rows = [
        f"| {col1} | {col2} |"
        for col1, col2 in rows
    ]

    return "\n".join([header_row, separator, *data_rows])


def build_asset_md_table(stork_rest_base_url, stork_auth_token):
    resp = requests.get(f"{stork_rest_base_url}/v1/prices/assets", headers={"Authorization": f"Basic {stork_auth_token}"})
    resp.raise_for_status()
    resp_obj = resp.json()
    asset_ids = resp_obj["data"]

    rows = [(asset_id, keccak256(asset_id)) for asset_id in asset_ids]

    return markdown_table(TABLE_HEADERS, rows)


if __name__ == "__main__":
    stork_rest_base_url = os.getenv("STORK_REST_BASE_URL")
    stork_auth_token = os.getenv("STORK_AUTH_TOKEN")
    print(build_asset_md_table(stork_rest_base_url, stork_auth_token))
