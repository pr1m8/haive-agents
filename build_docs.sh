#!/bin/bash
# Build script for haive-agents documentation with clean structure

echo "🧹 Cleaning previous build..."
rm -rf docs/build

echo "📚 Building documentation with Furo + AutoAPI..."
echo "This may take 10-15 minutes due to the large codebase."
echo ""

# Build without parallel processing to avoid errors
poetry run sphinx-build -b html docs/source docs/build/html

echo ""
echo "✅ Build complete!"
echo ""
echo "📂 To view the documentation:"
echo "   1. Serve locally: python -m http.server 8000 --directory docs/build/html"
echo "   2. Open browser: http://localhost:8000"
echo ""
echo "Or open directly:"
echo "   xdg-open docs/build/html/index.html"