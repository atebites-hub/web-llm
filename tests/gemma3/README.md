# Gemma-3-270m Test Suite

This directory contains comprehensive tests for the Gemma-3-270m model integration with WebLLM.

## Test Files

### Core Tests
- **`test_gemma3_features.js`** - Comprehensive feature testing (model config, files, sliding window, quantization, WebLLM integration)
- **`test_gemma3_webllm.js`** - WebLLM integration testing
- **`test_gemma3_config.py`** - Model configuration validation
- **`test_browser_inference.js`** - Browser inference testing and simulation
- **`test_performance.js`** - Performance analysis and benchmarking

### Browser Tests
- **`test_gemma3_browser.html`** - Interactive browser test page
- **`test_gemma3_webllm_simple.js`** - Simple WebLLM integration test

## Running Tests

### Node.js Tests
```bash
# Run comprehensive feature test
node tests/gemma3/test_gemma3_features.js

# Test WebLLM integration
node tests/gemma3/test_gemma3_webllm.js

# Test browser inference capabilities
node tests/gemma3/test_browser_inference.js

# Test performance characteristics
node tests/gemma3/test_performance.js
```

### Python Tests
```bash
# Test model configuration
python3 tests/gemma3/test_gemma3_config.py
```

### Browser Tests
```bash
# Start HTTP server
python3 -m http.server 8000

# Open browser test page
open http://localhost:8000/tests/gemma3/test_gemma3_browser.html
```

## Test Results

All tests should pass with 100% success rate:

- ✅ Model Configuration: Valid
- ✅ Model Files: All present
- ✅ Sliding Window: Properly configured
- ✅ 4-bit Quantization: Working correctly
- ✅ WebLLM Integration: Ready
- ✅ Browser Compatibility: Excellent
- ✅ Performance: Optimized

## Prerequisites

- Model files downloaded (`gemma-3-270m-it-qat-q4_0-unquantized/`)
- WebLLM library built (`npm run build`)
- Node.js 18+ for JavaScript tests
- Python 3.8+ for Python tests
- Modern browser with WebGPU support for browser tests

## Troubleshooting

### Model Files Missing
```bash
# Download model files
python3 scripts/download_gemma3_model.py
```

### WebLLM Build Issues
```bash
# Rebuild WebLLM
npm run build
```

### Browser Compatibility
- Ensure WebGPU support is enabled
- Check browser version (Chrome 113+, Firefox 110+, Safari 16.4+)
- Verify sufficient VRAM (1GB+ recommended)
