#!/usr/bin/env python3
"""
Direct test of MLC-LLM functionality without CLI
"""

import sys
import os
import json

# Add MLC-LLM paths
sys.path.insert(0, '/Users/jaskarn/github/web-llm/mlc-llm/python')
sys.path.insert(0, '/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/python')

# Set library path
os.environ['DYLD_LIBRARY_PATH'] = '/Users/jaskarn/github/web-llm/mlc-llm/build/lib:/Users/jaskarn/github/web-llm/mlc-llm/build/tvm'

try:
    # Try to import MLC-LLM components directly
    from mlc_llm.model import Model
    from mlc_llm.quantization import Quantization
    from mlc_llm.compiler import Compiler
    
    print("✅ MLC-LLM components imported successfully!")
    
    # Test model configuration loading
    config_path = "/Users/jaskarn/github/web-llm/gemma-3-270m-mlc/mlc-chat-config.json"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
        print("✅ Model configuration loaded successfully!")
        print(f"   Model type: {config.get('model_type')}")
        print(f"   Quantization: {config.get('quantization')}")
        print(f"   Context window: {config.get('context_window_size')}")
    else:
        print("❌ Model configuration not found")
        
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
