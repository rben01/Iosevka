#!/bin/bash

set -euxo pipefail

npm install
caffeinate npm run build -- --jCmd=3 {ttf-unhinted,woff2}"::"{iosevka-rltb-proportional-sans,iosevka-rltb-mono,iosevka-rltb-mono-alt}
