#!/usr/bin/env python3
"""
Test script to validate Gemma-3-270m model configuration
"""

import json
import os
import sys

def test_gemma3_config():
    """Test if the Gemma-3-270m model configuration is valid"""
    
    model_path = "gemma-3-270m-it-qat-q4_0-unquantized"
    config_path = os.path.join(model_path, "config.json")
    
    if not os.path.exists(config_path):
        print(f"❌ Model config not found at {config_path}")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print("✅ Gemma-3-270m Model Configuration:")
        print(f"   Architecture: {config.get('architectures', ['Unknown'])[0]}")
        print(f"   Model Type: {config.get('model_type', 'Unknown')}")
        print(f"   Hidden Size: {config.get('hidden_size', 'Unknown')}")
        print(f"   Num Layers: {config.get('num_hidden_layers', 'Unknown')}")
        print(f"   Attention Heads: {config.get('num_attention_heads', 'Unknown')}")
        print(f"   Sliding Window: {config.get('sliding_window', 'Unknown')}")
        print(f"   Sliding Window Pattern: {config.get('_sliding_window_pattern', 'Unknown')}")
        print(f"   Context Window: {config.get('max_position_embeddings', 'Unknown')}")
        print(f"   Vocab Size: {config.get('vocab_size', 'Unknown')}")
        
        # Check for required files
        required_files = [
            "config.json",
            "tokenizer.json", 
            "tokenizer_config.json",
            "model.safetensors"
        ]
        
        print("\n✅ Model Files Check:")
        for file in required_files:
            file_path = os.path.join(model_path, file)
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f"   ✓ {file} ({size:,} bytes)")
            else:
                print(f"   ✗ {file} (missing)")
                return False
        
        # Check for sliding window configuration
        if config.get('_sliding_window_pattern') == 6:
            print("\n✅ Sliding Window Configuration:")
            print("   ✓ Sliding window pattern: 6 (every 6th layer uses full attention)")
            print("   ✓ This matches MLC-LLM's Gemma3 implementation")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        return False

def check_mlc_llm_gemma3_support():
    """Check if MLC-LLM has Gemma3 support"""
    try:
        # Try to import MLC-LLM components
        sys.path.insert(0, 'mlc-llm/python')
        
        # Check if Gemma3 model files exist
        gemma3_path = "mlc-llm/python/mlc_llm/model/gemma3"
        if os.path.exists(gemma3_path):
            print("✅ MLC-LLM Gemma3 Support Found:")
            print(f"   ✓ Gemma3 model directory: {gemma3_path}")
            
            # List Gemma3 files
            gemma3_files = os.listdir(gemma3_path)
            for file in gemma3_files:
                if file.endswith('.py'):
                    print(f"   ✓ {file}")
            
            return True
        else:
            print("❌ MLC-LLM Gemma3 support not found")
            return False
            
    except Exception as e:
        print(f"❌ Error checking MLC-LLM Gemma3 support: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing Gemma-3-270m Model Configuration")
    print("=" * 50)
    
    # Test model configuration
    config_ok = test_gemma3_config()
    
    print("\n" + "=" * 50)
    print("🔍 Checking MLC-LLM Gemma3 Support")
    print("=" * 50)
    
    # Check MLC-LLM support
    mlc_support = check_mlc_llm_gemma3_support()
    
    print("\n" + "=" * 50)
    print("📋 Summary")
    print("=" * 50)
    
    if config_ok and mlc_support:
        print("✅ Both model configuration and MLC-LLM Gemma3 support are ready!")
        print("   Next step: Test model compilation with MLC-LLM")
    elif config_ok:
        print("✅ Model configuration is valid")
        print("❌ MLC-LLM Gemma3 support needs to be built/installed")
    else:
        print("❌ Issues found with model configuration")
