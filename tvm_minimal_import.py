#!/usr/bin/env python3
"""
Minimal TVM import to bypass initialization issues
"""

import sys
import os
import ctypes

def minimal_tvm_import():
    """Import TVM with minimal dependencies"""
    
    # Set up environment
    os.environ['DYLD_LIBRARY_PATH'] = '/Users/jaskarn/github/web-llm/mlc-llm/build/tvm:/Users/jaskarn/github/web-llm/mlc-llm/build/lib:/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/build/lib'
    
    # Load TVM C++ libraries first
    try:
        libtvm = ctypes.CDLL('/Users/jaskarn/github/web-llm/mlc-llm/build/tvm/libtvm.dylib')
        libtvm_ffi = ctypes.CDLL('/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/build/lib/libtvm_ffi.dylib')
        print("✅ TVM C++ libraries loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load TVM C++ libraries: {e}")
        return None
    
    # Try to import TVM components directly
    try:
        # Import tvm_ffi first
        import tvm_ffi
        print("✅ tvm_ffi imported successfully")
        
        # Try to import TVM base components
        sys.path.insert(0, '/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/python')
        
        # Import TVM base components
        from tvm.base import TVMError, __version__
        print(f"✅ TVM base imported successfully, version: {__version__}")
        
        # Try to import TVM runtime components
        from tvm.runtime import Object
        print("✅ TVM runtime imported successfully")
        
        # Try to import TVM IR components
        from tvm.ir import IRModule
        print("✅ TVM IR imported successfully")
        
        # Try to import TVM target components
        from tvm.target import Target
        print("✅ TVM target imported successfully")
        
        return {
            'version': __version__,
            'base': True,
            'runtime': True,
            'ir': True,
            'target': True
        }
        
    except Exception as e:
        print(f"❌ Failed to import TVM components: {e}")
        return None

if __name__ == "__main__":
    result = minimal_tvm_import()
    if result:
        print("✅ TVM minimal import successful!")
        print(f"TVM version: {result['version']}")
        print(f"Components available: {list(result.keys())}")
    else:
        print("❌ TVM minimal import failed!")
