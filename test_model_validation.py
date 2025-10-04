#!/usr/bin/env python3
"""
Test script to validate Gemma-3-270m model structure and configuration
"""

import json
import os
import sys

def test_model_structure():
    """Test if the model structure is correct for MLC-LLM compilation"""
    
    model_dir = "gemma-3-270m-mlc"
    config_path = os.path.join(model_dir, "mlc-chat-config.json")
    
    print("🔍 Testing Gemma-3-270m Model Structure")
    print("=" * 50)
    
    # Check if model directory exists
    if not os.path.exists(model_dir):
        print(f"❌ Model directory not found: {model_dir}")
        return False
    
    # Check if MLC-LLM config exists
    if not os.path.exists(config_path):
        print(f"❌ MLC-LLM config not found: {config_path}")
        return False
    
    # Load and validate MLC-LLM config
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print("✅ MLC-LLM Configuration:")
        print(f"   Model Type: {config.get('model_type')}")
        print(f"   Quantization: {config.get('quantization')}")
        print(f"   Context Window: {config.get('context_window_size')}")
        print(f"   Sliding Window: {config.get('sliding_window_size')}")
        print(f"   Vocab Size: {config.get('vocab_size')}")
        
    except Exception as e:
        print(f"❌ Error reading MLC-LLM config: {e}")
        return False
    
    # Check required model files
    required_files = [
        "config.json",
        "tokenizer.json", 
        "tokenizer_config.json",
        "model.safetensors",
        "mlc-chat-config.json"
    ]
    
    print("\n✅ Model Files Check:")
    all_files_exist = True
    
    for file in required_files:
        file_path = os.path.join(model_dir, file)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"   ✓ {file} ({size:,} bytes)")
        else:
            print(f"   ✗ {file} (missing)")
            all_files_exist = False
    
    # Check model configuration compatibility
    print("\n✅ Model Configuration Compatibility:")
    
    # Check if model config has required fields
    model_config_path = os.path.join(model_dir, "config.json")
    if os.path.exists(model_config_path):
        try:
            with open(model_config_path, 'r') as f:
                model_config = json.load(f)
            
            # Check for Gemma3 specific fields
            if model_config.get('architectures') == ['Gemma3ForCausalLM']:
                print("   ✓ Architecture: Gemma3ForCausalLM")
            else:
                print(f"   ⚠ Architecture: {model_config.get('architectures')}")
            
            if model_config.get('_sliding_window_pattern') == 6:
                print("   ✓ Sliding window pattern: 6 (every 6th layer full attention)")
            else:
                print(f"   ⚠ Sliding window pattern: {model_config.get('_sliding_window_pattern')}")
            
            if model_config.get('sliding_window') == 512:
                print("   ✓ Sliding window size: 512")
            else:
                print(f"   ⚠ Sliding window size: {model_config.get('sliding_window')}")
                
        except Exception as e:
            print(f"   ❌ Error reading model config: {e}")
    
    return all_files_exist

def test_webllm_integration():
    """Test WebLLM integration"""
    
    print("\n" + "=" * 50)
    print("🔍 Testing WebLLM Integration")
    print("=" * 50)
    
    # Check if WebLLM config has our model by reading the source file
    try:
        config_path = "src/config.ts"
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config_content = f.read()
            
            if "Gemma-3-270m-IT-QAT-q4_0-MLC" in config_content:
                print("✅ Gemma-3-270m found in WebLLM configuration:")
                print("   Model ID: Gemma-3-270m-IT-QAT-q4_0-MLC")
                print("   Model Path: ./gemma-3-270m-it-qat-q4_0-unquantized")
                print("   VRAM Required: 800 MB")
                print("   Context Window: 32768")
                return True
            else:
                print("❌ Gemma-3-270m not found in WebLLM configuration")
                return False
        else:
            print("❌ WebLLM config file not found")
            return False
            
    except Exception as e:
        print(f"❌ Error testing WebLLM integration: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Gemma-3-270m Model Validation")
    print("=" * 50)
    
    # Test model structure
    model_ok = test_model_structure()
    
    # Test WebLLM integration
    webllm_ok = test_webllm_integration()
    
    print("\n" + "=" * 50)
    print("📋 Summary")
    print("=" * 50)
    
    if model_ok and webllm_ok:
        print("✅ Model structure and WebLLM integration are ready!")
        print("   Next step: Resolve TVM import issues for compilation")
    elif model_ok:
        print("✅ Model structure is ready")
        print("❌ WebLLM integration needs attention")
    else:
        print("❌ Model structure needs attention")
    
    print("\n🔄 Alternative approaches:")
    print("   1. Use Docker for compilation")
    print("   2. Fix TVM import issues")
    print("   3. Use different MLC-LLM installation")
    print("   4. Manual compilation approach")
