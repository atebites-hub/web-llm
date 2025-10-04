# Gemma-3-270m Compilation Guide

## Overview

This guide outlines the steps to compile the Gemma-3-270m model with MLC-LLM for WebLLM integration. The model features sliding window transformers and 4-bit quantization support.

## Current Status

✅ **Completed:**
- MLC-LLM built from source (commit `bad02b4ed7a5fac3bc2e62ad999d2d6d100f311c`)
- WebLLM updated with compatibility changes from `webllm-runtime-upgrade` branch
- Gemma-3-270m model integrated into WebLLM configuration
- Model files validated (536MB model.safetensors, 32MB tokenizer.json)

🔄 **Next Steps:**
- Compile model with MLC-LLM to generate WebGPU WASM library
- Test model inference in browser environment

## Model Configuration

The Gemma-3-270m model has been added to WebLLM with the following configuration:

```typescript
{
  model: "./gemma-3-270m-it-qat-q4_0-unquantized",
  model_id: "Gemma-3-270m-IT-QAT-q4_0-MLC",
  model_lib: "TBD", // Will be generated after compilation
  vram_required_MB: 800, // Estimated for 270M model with 4-bit quantization
  low_resource_required: true,
  overrides: {
    context_window_size: 32768, // From model config
  },
}
```

## Model Features

- **Architecture**: Gemma3ForCausalLM
- **Parameters**: 270M
- **Context Window**: 32,768 tokens
- **Sliding Window**: 512 tokens (pattern: every 6th layer uses full attention)
- **Quantization**: 4-bit (Q4_0) with Quantization Aware Training (QAT)
- **VRAM Required**: ~800MB (estimated)

## Compilation Steps

### 1. Generate Model Configuration

```bash
cd /Users/jaskarn/github/web-llm/mlc-llm
python3 -m mlc_llm gen_config ./gemma-3-270m-it-qat-q4_0-unquantized --output-dir ../gemma-3-270m-mlc
```

### 2. Convert Model Weights

```bash
python3 -m mlc_llm convert_weights ./gemma-3-270m-it-qat-q4_0-unquantized --output-dir ../gemma-3-270m-mlc
```

### 3. Compile Model for WebGPU

```bash
python3 -m mlc_llm compile ../gemma-3-270m-mlc --target webgpu --output-dir ../gemma-3-270m-compiled
```

### 4. Update WebLLM Configuration

After successful compilation, update the `model_lib` path in `src/config.ts`:

```typescript
model_lib: "./gemma-3-270m-compiled/gemma-3-270m-it-qat-q4_0-unquantized-webgpu.wasm",
```

## Troubleshooting

### TVM Import Issues

If you encounter TVM import conflicts:

1. Uninstall conflicting TVM packages:
   ```bash
   pip3 uninstall apache-tvm-ffi -y
   ```

2. Use MLC-LLM's TVM:
   ```bash
   export PYTHONPATH=/Users/jaskarn/github/web-llm/mlc-llm/python:/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/python
   ```

### CMake Compatibility

If CMake build fails, use the policy workaround:

```bash
pip3 install -e . --config-settings cmake.args="-DCMAKE_POLICY_VERSION_MINIMUM=3.5"
```

## Testing

### 1. Test Model Configuration

```bash
node test_gemma3_webllm.js
```

### 2. Test Model Compilation

```bash
python3 test_gemma3_config.py
```

### 3. Test Browser Inference

Create a simple HTML test file to verify the model works in the browser environment.

## Expected Output

After successful compilation, you should have:

- `gemma-3-270m-it-qat-q4_0-unquantized-webgpu.wasm` - WebGPU WASM library
- Model configuration files
- Tokenizer files
- Quantized model weights

## Performance Expectations

- **Model Size**: ~200MB (4-bit quantized)
- **VRAM Usage**: ~800MB
- **Inference Speed**: Fast (270M parameters)
- **Context Length**: 32,768 tokens with sliding window attention

## Next Steps

1. Complete model compilation
2. Test inference in browser
3. Optimize performance if needed
4. Add to WebLLM examples
5. Document usage patterns

## References

- [MLC-LLM Documentation](https://llm.mlc.ai/docs/)
- [WebLLM Documentation](https://webllm.mlc.ai/)
- [Gemma-3 Model Card](https://huggingface.co/google/gemma-3-270m-it-qat-q4_0)
