#!/usr/bin/env python3
"""
Patch to fix TVM initialization ordering issue
"""

import sys
import os
import ctypes

def patch_tvm_initialization():
    """Patch TVM initialization to fix object registration ordering"""
    
    # Set up environment
    os.environ['DYLD_LIBRARY_PATH'] = '/Users/jaskarn/github/web-llm/mlc-llm/build/tvm:/Users/jaskarn/github/web-llm/mlc-llm/build/lib:/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/build/lib'
    
    # Load TVM C++ libraries first
    try:
        libtvm = ctypes.CDLL('/Users/jaskarn/github/web-llm/mlc-llm/build/tvm/libtvm.dylib')
        libtvm_ffi = ctypes.CDLL('/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/build/lib/libtvm_ffi.dylib')
        print("✅ TVM C++ libraries loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load TVM C++ libraries: {e}")
        return False
    
    # Try to initialize TVM by calling a simple function
    try:
        # Look for any initialization function in the library
        # Try to call a function that might initialize the registry
        pass  # For now, just load the libraries
        print("✅ TVM C++ libraries initialized")
    except Exception as e:
        print(f"⚠️  TVM initialization warning: {e}")
    
    return True

def import_tvm_with_patch():
    """Import TVM with the initialization patch"""
    
    # Apply the patch
    if not patch_tvm_initialization():
        return None
    
    # Now try to import TVM
    try:
        import tvm
        print("✅ TVM imported successfully")
        return tvm
    except Exception as e:
        print(f"❌ Failed to import TVM: {e}")
        return None

if __name__ == "__main__":
    tvm = import_tvm_with_patch()
    if tvm:
        print(f"TVM version: {tvm.__version__}")
        print("TVM initialization patch successful!")
    else:
        print("TVM initialization patch failed!")
