#!/usr/bin/env python3
import json
import subprocess


def get_latest_release_tag() -> str:
    """Return the tag name of the latest release."""
    json_string = (
        subprocess.run(
            ["gh", "release", "view", "--json", "tagName"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.decode("utf8")
        .strip()
    )

    return json.loads(json_string)["tagName"]


def generate_next_patch_version(current_version: str) -> str:
    """Generate the next patch version."""
    major, minor, patch = current_version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def main():
    """Generate a new release tag and name without creating a GitHub release."""
    try:
        latest_release_tag = get_latest_release_tag()
    except subprocess.CalledProcessError as err:
        if err.stderr.decode("utf8").startswith("HTTP 404:"):
            # The project doesn't have any releases yet.
            new_version = "0.0.1"
        else:
            raise
    else:
        new_version = generate_next_patch_version(latest_release_tag)

    # Print the new release tag and name to stdout
    print(new_version, end="")


if __name__ == "__main__":
    main()
