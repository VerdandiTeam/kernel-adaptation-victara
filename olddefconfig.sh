#!/bin/sh
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG="$DIR/sfos-victara_defconfig"
LINUX="${LINUX:-$DIR/linux}"
OUT="$(mktemp -d)"

trap 'rm -rf "$OUT"' EXIT

cp "$CONFIG" "$OUT/.config"
make -C "$LINUX" O="$OUT" ARCH=arm olddefconfig
cp "$OUT/.config" "$CONFIG"
