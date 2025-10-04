# WebLLM Test Suite

This directory contains comprehensive tests for WebLLM functionality.

## Test Structure

### Core Tests
- **`*.test.ts`** - Unit tests for WebLLM components
- **`scripts/`** - Test scripts and utilities

### Model-Specific Tests
- **`gemma3/`** - Gemma-3-270m model integration tests
  - Comprehensive feature testing
  - Browser inference testing
  - Performance analysis
  - WebLLM integration validation

## Running Tests

### Unit Tests
```bash
# Run all unit tests
npm test

# Run specific test file
npm test -- conversation.test.ts
```

### Gemma-3 Tests
```bash
# Run comprehensive Gemma-3 tests
cd tests/gemma3
node test_gemma3_features.js
```

### Browser Tests
```bash
# Start HTTP server for browser tests
python3 -m http.server 8000

# Open browser test page
open http://localhost:8000/tests/gemma3/test_gemma3_browser.html
```

## Test Coverage

The test suite covers:
- Core WebLLM functionality
- Model integration and configuration
- Browser compatibility
- Performance characteristics
- API compatibility
- Error handling

## Prerequisites

- Node.js 18+
- Python 3.8+ (for some tests)
- Modern browser with WebGPU support
- Model files downloaded (for model-specific tests)

## Contributing

When adding new tests:
1. Follow existing naming conventions
2. Include comprehensive test coverage
3. Document test requirements
4. Update this README if needed
