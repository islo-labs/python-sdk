#!/usr/bin/env python3
"""End-to-end SDK lifecycle test.

Usage:
    ISLO_API_KEY=<your-key> uv run python scripts/e2e_test.py
"""

from __future__ import annotations

import os
import sys
import time

from islo import Islo


def main():
    api_key = os.environ.get("ISLO_API_KEY")
    if not api_key:
        print("Set ISLO_API_KEY environment variable first")
        sys.exit(1)

    # API key is automatically exchanged for a session JWT
    client = Islo()
    print(f"Client configured: {client._client_wrapper._base_url}")

    # 1. Create sandbox
    print("\n--- Create sandbox ---")
    sandbox = client.sandboxes.create_sandbox(
        name="sdk-e2e-test",
        image="ubuntu:22.04",
        vcpus=2,
        memory_mb=2048,
        disk_gb=5,
    )
    print(f"Created: {sandbox.name} (status={sandbox.status}, id={sandbox.id})")

    # 2. Wait for running
    print("\n--- Wait for running ---")
    for i in range(30):
        sb = client.sandboxes.get_sandbox(sandbox.name)
        print(f"  [{i}] status={sb.status}")
        if sb.status == "running":
            break
        time.sleep(2)
    else:
        print("Timed out waiting for sandbox to start")
        client.sandboxes.delete_sandbox(sandbox.name)
        sys.exit(1)

    # 3. Exec command
    print("\n--- Exec: echo test ---")
    exec_result = client.sandboxes.exec_in_sandbox(
        sandbox_name=sandbox.name,
        command=["echo", "hello from islo-sdk"],
    )
    print(f"Exit code: {exec_result.exit_code}")

    # 4. List sandboxes
    print("\n--- List sandboxes ---")
    sandboxes = client.sandboxes.list_sandboxes()
    print(f"Total: {sandboxes.total}, showing {len(sandboxes.items)} items")
    for sb in sandboxes.items[:3]:
        print(f"  {sb.name} ({sb.status})")

    # 5. Delete sandbox
    print("\n--- Delete sandbox ---")
    client.sandboxes.delete_sandbox(sandbox_name=sandbox.name)
    print("Deleted")

    print("\n All lifecycle steps completed successfully!")


if __name__ == "__main__":
    main()
