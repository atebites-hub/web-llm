#!/usr/bin/env python3
"""
Script to download Gemma-3-270m model files from HuggingFace
"""

import os
import sys
from huggingface_hub import snapshot_download

def download_gemma3_model():
    """Download Gemma-3-270m model files from HuggingFace"""
    
    model_id = "google/gemma-3-270m-it-qat-q4_0"
    local_dir = "./gemma-3-270m-it-qat-q4_0-unquantized"
    
    print(f"🔍 Downloading Gemma-3-270m model from HuggingFace")
    print(f"   Model ID: {model_id}")
    print(f"   Local Directory: {local_dir}")
    print("=" * 60)
    
    try:
        # Create local directory if it doesn't exist
        os.makedirs(local_dir, exist_ok=True)
        
        # Download the model
        print("📥 Starting download...")
        snapshot_download(
            repo_id=model_id,
            local_dir=local_dir,
            local_dir_use_symlinks=False,
            resume_download=True
        )
        
        print("✅ Download completed successfully!")
        
        # Verify downloaded files
        print("\n🔍 Verifying downloaded files:")
        required_files = [
            "config.json",
            "tokenizer.json", 
            "tokenizer_config.json",
            "model.safetensors"
        ]
        
        for file in required_files:
            file_path = os.path.join(local_dir, file)
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f"   ✓ {file} ({size:,} bytes)")
            else:
                print(f"   ✗ {file} (missing)")
                return False
        
        print("\n✅ All required model files are present!")
        print(f"   Model ready for MLC-LLM compilation")
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False

def check_model_config():
    """Check the downloaded model configuration"""
    
    config_path = "./gemma-3-270m-it-qat-q4_0-unquantized/config.json"
    
    if not os.path.exists(config_path):
        print("❌ Model config not found")
        return False
    
    try:
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print("\n📋 Model Configuration:")
        print(f"   Architecture: {config.get('architectures', ['Unknown'])[0]}")
        print(f"   Model Type: {config.get('model_type', 'Unknown')}")
        print(f"   Hidden Size: {config.get('hidden_size', 'Unknown')}")
        print(f"   Num Layers: {config.get('num_hidden_layers', 'Unknown')}")
        print(f"   Attention Heads: {config.get('num_attention_heads', 'Unknown')}")
        print(f"   Sliding Window: {config.get('sliding_window', 'Unknown')}")
        print(f"   Context Window: {config.get('max_position_embeddings', 'Unknown')}")
        print(f"   Vocab Size: {config.get('vocab_size', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Gemma-3-270m Model Download Script")
    print("=" * 60)
    
    # Download the model
    success = download_gemma3_model()
    
    if success:
        # Check configuration
        check_model_config()
        
        print("\n📋 Next Steps:")
        print("1. Run: python3 test_gemma3_config.py")
        print("2. Compile model with MLC-LLM")
        print("3. Test in WebLLM")
    else:
        print("\n❌ Download failed. Please check your internet connection and try again.")
        sys.exit(1)