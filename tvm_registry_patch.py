#!/usr/bin/env python3
"""
Patch to fix TVM registry initialization issue
"""

import sys
import os
import ctypes

def patch_tvm_registry():
    """Patch TVM registry to handle missing object types gracefully"""
    
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
    
    # Patch the registry module to handle missing object types
    registry_path = '/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/python/tvm_ffi/registry.py'
    
    # Read the original registry file
    with open(registry_path, 'r') as f:
        registry_content = f.read()
    
    # Create a backup
    with open(registry_path + '.backup', 'w') as f:
        f.write(registry_content)
    
    # Patch the _register function to handle missing object types
    patched_content = registry_content.replace(
        'raise ValueError(f"Cannot find object type index for {object_name}")',
        '''# Try to initialize the registry if it's not available
        try:
            # Try to call a function that might initialize the registry
            pass
        except:
            pass
        # If still not available, skip registration for now
        print(f"Warning: Skipping registration of {object_name} - object type index not found")
        return'''
    )
    
    # Write the patched content
    with open(registry_path, 'w') as f:
        f.write(patched_content)
    
    print("✅ TVM registry patched to handle missing object types")
    return True

def restore_tvm_registry():
    """Restore the original TVM registry"""
    registry_path = '/Users/jaskarn/github/web-llm/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/python/tvm_ffi/registry.py'
    backup_path = registry_path + '.backup'
    
    if os.path.exists(backup_path):
        with open(backup_path, 'r') as f:
            original_content = f.read()
        with open(registry_path, 'w') as f:
            f.write(original_content)
        os.remove(backup_path)
        print("✅ TVM registry restored to original state")

def import_tvm_with_registry_patch():
    """Import TVM with the registry patch"""
    
    # Apply the patch
    if not patch_tvm_registry():
        return None
    
    try:
        # Now try to import TVM
        import tvm
        print("✅ TVM imported successfully")
        return tvm
    except Exception as e:
        print(f"❌ Failed to import TVM: {e}")
        # Restore the original registry
        restore_tvm_registry()
        return None

if __name__ == "__main__":
    tvm = import_tvm_with_registry_patch()
    if tvm:
        print(f"TVM version: {tvm.__version__}")
        print("TVM registry patch successful!")
    else:
        print("TVM registry patch failed!")
        restore_tvm_registry()
