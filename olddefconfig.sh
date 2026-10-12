#!/bin/sh
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG="$DIR/config-motorola-victara.armv7"
FRAGMENT="$DIR/sfos.config"
LINUX="${LINUX:-$DIR/../linux}"
OUT="$(mktemp -d)"

trap 'rm -rf "$OUT"' EXIT

cd "$LINUX"
ARCH=arm scripts/kconfig/merge_config.sh -m -O "$OUT" "$CONFIG" "$FRAGMENT"
make O="$OUT" ARCH=arm olddefconfig
cp "$OUT/.config" "$CONFIG"
