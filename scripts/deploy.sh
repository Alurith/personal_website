#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing requirements"
pip install -r requirements.txt
echo "Installing tailwind"
npm install -D tailwindcss
echo "Generating HTML"
cd src && make publish
cd ..
echo "Building production css"
npx tailwindcss -i ./src/theme/static/css/input.css -o ./src/output/theme/css/output.css
