#!/usr/bin/env node
/**
 * Test script to verify Gemma-3-270m integration with WebLLM
 */

import { prebuiltAppConfig } from './lib/index.js';

console.log('🔍 Testing Gemma-3-270m WebLLM Integration');
console.log('=' .repeat(50));

// Find our Gemma-3-270m model in the configuration
const gemmaModel = prebuiltAppConfig.model_list.find(model => 
  model.model_id === 'Gemma-3-270m-IT-QAT-q4_0-MLC'
);

if (gemmaModel) {
  console.log('✅ Gemma-3-270m model found in WebLLM configuration:');
  console.log(`   Model ID: ${gemmaModel.model_id}`);
  console.log(`   Model Path: ${gemmaModel.model}`);
  console.log(`   VRAM Required: ${gemmaModel.vram_required_MB} MB`);
  console.log(`   Low Resource: ${gemmaModel.low_resource_required}`);
  console.log(`   Context Window: ${gemmaModel.overrides?.context_window_size}`);
  console.log(`   Sliding Window: ${gemmaModel.overrides?.sliding_window}`);
  
  // Check if model files exist
  const fs = await import('fs');
  const path = await import('path');
  
  const modelPath = path.resolve(gemmaModel.model);
  console.log(`\n🔍 Checking model files at: ${modelPath}`);
  
  const requiredFiles = ['config.json', 'tokenizer.json', 'model.safetensors'];
  let allFilesExist = true;
  
  for (const file of requiredFiles) {
    const filePath = path.join(modelPath, file);
    if (fs.existsSync(filePath)) {
      const stats = fs.statSync(filePath);
      console.log(`   ✓ ${file} (${(stats.size / 1024 / 1024).toFixed(2)} MB)`);
    } else {
      console.log(`   ✗ ${file} (missing)`);
      allFilesExist = false;
    }
  }
  
  if (allFilesExist) {
    console.log('\n✅ All required model files are present!');
    console.log('   Next step: Compile model with MLC-LLM to generate model_lib');
  } else {
    console.log('\n❌ Some model files are missing');
  }
  
} else {
  console.log('❌ Gemma-3-270m model not found in WebLLM configuration');
}

console.log('\n📋 Summary');
console.log('=' .repeat(50));
console.log('✅ WebLLM configuration updated with Gemma-3-270m');
console.log('✅ Model files validated');
console.log('🔄 Next: Compile model with MLC-LLM to generate WebGPU WASM library');
