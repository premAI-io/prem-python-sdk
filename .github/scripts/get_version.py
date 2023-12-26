#!/usr/bin/env python3
import json
import subprocess
import sys


def get_latest_release_tag() -> str:
    """Return the tag name of the latest release."""
    try:
        result = subprocess.run(
            ["gh", "release", "view", "--json", "tagName"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        json_string = result.stdout.decode("utf8").strip()
    except subprocess.CalledProcessError as err:
        error_message = err.stderr.decode("utf8").strip()
        if "release not found" in error_message:
            return "0.0.0"
        else:
            print(f"Error executing 'gh release view': {error_message}")
            sys.exit(1)

    try:
        return json.loads(json_string)["tagName"]
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON: {json_err}")
        print(f"JSON string received: {json_string}")
        sys.exit(1)


def generate_next_patch_version(current_version: str) -> str:
    """Generate the next patch version."""
    major, minor, patch = current_version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def main():
    """Generate a new release tag and name without creating a GitHub release."""
    try:
        latest_release_tag = get_latest_release_tag()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    new_version = generate_next_patch_version(latest_release_tag)

    # Print the new release tag and name to stdout
    print(new_version, end="")


if __name__ == "__main__":
    main()
