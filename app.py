import streamlit as st
import streamlit.components.v1 as components

# 1. Setup Streamlit page config
st.set_page_config(
    page_title="MedIntel AI Platform",
    layout="wide",
    initial_sidebar_state="collapsed" # We collapse the native sidebar to use our custom high-class one
)

# 2. Embed the premium responsive clinical engine HTML/JS
responsive_dashboard_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MedIntel AI - Clinical Assistant Platform</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #070b19; }
        ::-webkit-scrollbar-thumb { background: #1e3a8a; border-radius: 10px; }
    </style>
</head>
<body class="bg-[#070b19] text-slate-100 min-h-screen font-sans flex antialiased overflow-x-hidden">

    <!-- SIDEBAR -->
    <aside class="w-72 bg-[#0d1527] border-r border-blue-950/40 p-6 flex flex-col justify-between hidden lg:flex">
        <div>
            <div class="flex items-center gap-3 mb-8">
                <div class="bg-blue-600 p-2 rounded-xl text-white shadow-lg shadow-blue-500/20">
                    <i data-lucide="brain" class="w-5 h-5"></i>
                </div>
                <div>
                    <h1 class="font-bold text-base text-white tracking-wide">MedIntel AI</h1>
                    <span class="text-[10px] text-blue-400 font-bold uppercase tracking-wider">Clinical Intelligence Engine</span>
                </div>
            </div>
            
            <nav class="space-y-1">
                <p class="text-[10px] font-bold text-slate-500 uppercase tracking-wider mb-2 px-3">Diagnostic Modes</p>
                <button onclick="switchTab('assistant')" id="btn-assistant" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold bg-blue-600/15 text-blue-400 border border-blue-500/20 transition-all">
                    <i data-lucide="activity" class="w-4 h-4"></i> Interactive AI Assistant
                </button>
                <button onclick="switchTab('distillation')" id="btn-distillation" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-slate-800/40 hover:text-slate-200 transition-all">
                    <i data-lucide="layers" class="w-4 h-4"></i> SLM Edge Distillation Engine
                </button>
            </nav>
        </div>

        <div class="bg-[#111c35] p-3 rounded-xl border border-blue-900/30 flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 font-bold text-xs">MD</div>
            <div>
                <p class="text-xs font-semibold text-slate-200">Dr. Alex Sterling</p>
                <p class="text-[10px] text-slate-400">Attending Clinician</p>
            </div>
        </div>
    </aside>

    <!-- MAIN INTERFACE -->
    <main class="flex-1 flex flex-col overflow-y-auto min-h-screen">
        
        <!-- HEADER -->
        <header class="h-16 bg-[#0d1527]/80 backdrop-blur-md px-6 flex items-center justify-between border-b border-blue-950/40 sticky top-0 z-50">
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400 font-medium">System Status:</span>
                <span class="flex items-center gap-1.5 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[10px] font-bold px-2.5 py-0.5 rounded-full">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> Active Inference Matrix
                </span>
            </div>
            <div class="text-[11px] font-mono text-blue-400 bg-blue-950/50 border border-blue-900/40 px-3 py-1 rounded-md">
                Framework: PyTorch & FastAPI Core
            </div>
        </header>

        <!-- CONTENT VIEWPORTS -->
        <div class="p-6 max-w-7xl w-full mx-auto space-y-6">

            <!-- TAB 1: INTERACTIVE ASSISTANT -->
            <div id="tab-assistant" class="space-y-6">
                <div class="bg-gradient-to-r from-[#101b38] to-[#0a1024] p-6 rounded-2xl border border-blue-900/30 shadow-xl">
                    <h2 class="text-lg font-bold text-white mb-1">Multi-Scenario Patient Diagnostics</h2>
                    <p class="text-slate-400 text-xs">Simulate validation calculations across diverse models: Disease, Stage, Mortality, and Progression timelines.</p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <div class="bg-[#0d1527] border border-blue-950/60 p-5 rounded-xl space-y-4 h-fit">
                        <h3 class="text-xs font-bold uppercase text-blue-400 tracking-wider mb-2">Patient Clinical Metrics</h3>
                        <div>
                            <label class="text-[11px] text-slate-400 block mb-1">Presenting Clinical Scenarios</label>
                            <select id="patient-scenario" class="w-full bg-[#070b19] border border-blue-950 rounded-lg p-2 text-xs text-slate-200 outline-none focus:border-blue-500">
                                <option value="cardio">Cardiovascular Distress Vector (Acute Cardiac/Ischemic)</option>
                                <option value="oncology">Oncology Progression Indicator (Metastatic Tracking)</option>
                                <option value="pulmonary">Pulmonary Hypoxia Complex (Severe Respiratory stress)</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-[11px] text-slate-400 block mb-1">Patient Biomarker Factor (Serum Value)</label>
                            <input type="range" id="biomarker-val" min="10" max="100" value="65" class="w-full accent-blue-500 bg-[#070b19]">
                        </div>
                        <div>
                            <label class="text-[11px] text-slate-400 block mb-1">Comorbidity Index Multiplier</label>
                            <select id="comorbidity" class="w-full bg-[#070b19] border border-blue-950 rounded-lg p-2 text-xs text-slate-200 outline-none focus:border-blue-500">
                                <option value="low">Low Risk Matrix Factors (0 - 1)</option>
                                <option value="moderate">Moderate Structural Risks (2 - 3)</option>
                                <option value="critical">Critical End-Organ Deficits (4+)</option>
                            </select>
                        </div>
                        <button onclick="calculatePredictions()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-3 rounded-xl shadow-lg shadow-blue-600/20 tracking-wide transition-all uppercase">
                            Execute Multi-Model Engine Inference
                        </button>
                    </div>

                    <div class="bg-[#0d1527] border border-blue-950/60 p-5 rounded-xl lg:col-span-2 space-y-4">
                        <div class="flex justify-between items-center border-b border-blue-950/40 pb-3">
                            <h3 class="text-xs font-bold uppercase text-slate-300 tracking-wider">Multi-Model Target Predictions</h3>
                            <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded font-mono">Live Inferences Done</span>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="prediction-grid"></div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: DISTILLATION ENGINE PIPELINE -->
            <div id="tab-distillation" class="space-y-6 hidden">
                <div class="bg-gradient-to-r from-[#101b38] to-[#0a1024] p-6 rounded-2xl border border-blue-900/30 shadow-xl">
                    <h2 class="text-lg font-bold text-white mb-1">Small Language Model Distillation Simulator</h2>
                    <p class="text-slate-400 text-xs">Convert large clinical AI models into highly responsive architectures optimized for Edge Devices (Mobile/Raspberry Pi).</p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <div class="bg-[#0d1527] border border-blue-950/60 p-5 rounded-xl space-y-4 h-fit">
                        <h3 class="text-xs font-bold uppercase text-blue-400 tracking-wider">Distillation Parameters</h3>
                        <div>
                            <label class="text-[11px] text-slate-400 block mb-1">Target Calibration Dataset</label>
                            <select id="dataset-select" class="w-full bg-[#070b19] border border-blue-950 rounded-lg p-2 text-xs text-slate-200 outline-none">
                                <option value="sst">SST-2 (Clinical Sentiment Mapping)</option>
                                <option value="imdb">IMDB Records (Behavioral Reports)</option>
                                <option value="ag">AG News (Categorized Intake Synthesis)</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-[11px] text-slate-400 block mb-1">Compression Methods</label>
                            <div class="space-y-1.5 mt-2 text-xs">
                                <label class="flex items-center gap-2"><input type="checkbox" checked disabled class="accent-blue-500"> Knowledge Distillation</label>
                                <label class="flex items-center gap-2"><input type="checkbox" id="quantize" checked class="accent-blue-500"> Post-Training Quantization (INT8)</label>
                                <label class="flex items-center gap-2"><input type="checkbox" id="prune" class="accent-blue-500"> Structural Weights Pruning</label>
                            </div>
                        </div>
                        <button onclick="runDistillation()" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs py-3 rounded-xl tracking-wide transition-all uppercase">
                            Initialize Compilation Run
                        </button>
                    </div>

                    <div class="bg-[#0d1527] border border-blue-950/60 p-5 rounded-xl lg:col-span-2 space-y-4">
                        <h3 class="text-xs font-bold uppercase text-slate-300 tracking-wider mb-2">Pipeline Optimization Progression</h3>
                        <div class="space-y-3" id="pipeline-steps">
                            <div class="flex items-center gap-3 p-3 bg-slate-900/20 border border-blue-950 rounded-lg opacity-40" id="step1">
                                <div class="p-1 rounded bg-blue-500/10 text-blue-400"><i data-lucide="download" class="w-4 h-4"></i></div>
                                <div class="text-xs font-medium">Download Teacher Model Framework (Large Parameter Spec)</div>
                            </div>
                            <div class="flex items-center gap-3 p-3 bg-slate-900/20 border border-blue-950 rounded-lg opacity-40" id="step2">
                                <div class="p-1 rounded bg-indigo-500/10 text-indigo-400"><i data-lucide="cpu" class="w-4 h-4"></i></div>
                                <div class="text-xs font-medium">Train Student Model Parameters & Knowledge Distillation Matrix</div>
                            </div>
                            <div class="flex items-center gap-3 p-3 bg-slate-900/20 border border-blue-950 rounded-lg opacity-40" id="step3">
                                <div class="p-1 rounded bg-purple-500/10 text-purple-400"><i data-lucide="shrink" class="w-4 h-4"></i></div>
                                <div class="text-xs font-medium">Apply Post-Training Model Compression Metrics</div>
                            </div>
                            <div class="flex items-center gap-3 p-3 bg-slate-900/20 border border-blue-950 rounded-lg opacity-40" id="step4">
                                <div class="p-1 rounded bg-cyan-500/10 text-cyan-400"><i data-lucide="file-check" class="w-4 h-4"></i></div>
                                <div class="text-xs font-medium">Convert Graph to Optimized ONNX / TensorFlow Lite Runtime Format</div>
                            </div>
                        </div>

                        <div id="distill-output" class="hidden mt-4 p-4 bg-[#111c35] border border-blue-900/40 rounded-xl grid grid-cols-3 gap-2 text-center">
                            <div><p class="text-[10px] text-slate-400">Memory Reduction</p><p class="text-base font-bold text-emerald-400" id="out-mem">-74.2%</p></div>
                            <div><p class="text-[10px] text-slate-400">Inference Speedup</p><p class="text-base font-bold text-cyan-400" id="out-speed">4.1x Fast</p></div>
                            <div><p class="text-[10px] text-slate-400">Target Framework</p><p class="text-base font-bold text-white font-mono text-xs mt-1" id="out-format">ONNX Runtime</p></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </main>

    <script>
        function switchTab(tab) {
            document.getElementById('tab-assistant').classList.add('hidden');
            document.getElementById('tab-distillation').classList.add('hidden');
            document.getElementById('btn-assistant').className = "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-slate-800/40 hover:text-slate-200 transition-all";
            document.getElementById('btn-distillation').className = "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-400 hover:bg-slate-800/40 hover:text-slate-200 transition-all";
            
            if(tab === 'assistant') {
                document.getElementById('tab-assistant').classList.remove('hidden');
                document.getElementById('btn-assistant').className = "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold bg-blue-600/15 text-blue-400 border border-blue-500/20 transition-all";
            } else {
                document.getElementById('tab-distillation').classList.remove('hidden');
                document.getElementById('btn-distillation').className = "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-semibold bg-blue-600/15 text-blue-400 border border-blue-500/20 transition-all";
            }
        }

        function calculatePredictions() {
            const scenario = document.getElementById('patient-scenario').value;
            const biomarker = parseInt(document.getElementById('biomarker-val').value);
            const comorbidity = document.getElementById('comorbidity').value;

            let logicMod = scenario === 'cardio' ? 1.05 : (scenario === 'oncology' ? 0.92 : 1.12);
            let riskMod = comorbidity === 'critical' ? 1.25 : (comorbidity === 'moderate' ? 1.05 : 0.85);

            const metrics = [
                { name: "Disease Presence Probability", model: "XGBoost Engine", val: Math.min(99.4, (biomarker * 0.85 * logicMod * riskMod)).toFixed(1) + "%", status: "Inference Validated" },
                { name: "Disease Stage Identification", model: "Scikit-Learn Classifier", val: "Stage " + (riskMod > 1.1 ? "IV Critical" : (riskMod > 0.9 ? "III Advanced" : "I-II Localized")), status: "Structural Match" },
                { name: "Mortality Risk Factor", model: "TensorFlow Deep Neural", val: Math.min(98.9, (biomarker * 0.72 * riskMod)).toFixed(1) + "%", status: riskMod > 1.1 ? "High Critical Priority" : "Stable Phase" },
                { name: "Clinical Recovery Target Vector", model: "PyTorch Predictive Logic", val: Math.max(12, (100 - (biomarker * 0.65 * riskMod))).toFixed(1) + "% Profile", status: "Calculated Likelihood" },
                { name: "Hospital Readmission Event Probability", model: "XGBoost Core System", val: Math.min(95.0, (biomarker * 0.45 * riskMod)).toFixed(1) + "%", status: "Pipeline Evaluation Verified" },
                { name: "Disease Progression Speed Horizon", model: "SHAP-Supported Meta Ensemble", val: (logicMod * riskMod * 2.4).toFixed(2) + "x Baseline Acceleration", status: "Explainable Matrix Output" }
            ];

            const grid = document.getElementById('prediction-grid');
            grid.innerHTML = '';

            metrics.forEach(m => {
                grid.innerHTML += `
                    <div class="bg-[#111c35]/40 border border-blue-900/30 p-4 rounded-xl flex flex-col justify-between hover:border-blue-700/50 transition-all">
                        <div>
                            <span class="text-[10px] text-slate-400 font-mono tracking-tight block mb-0.5">${m.model}</span>
                            <h4 class="text-xs font-bold text-slate-200">${m.name}</h4>
                        </div>
                        <div class="mt-4 flex justify-between items-end">
                            <span class="text-base font-mono font-bold text-white tracking-tight">${m.val}</span>
                            <span class="text-[9px] font-semibold text-blue-400 bg-blue-950/80 px-2 py-0.5 rounded border border-blue-900/30">${m.status}</span>
                        </div>
                    </div>
                `;
            });
        }

        function runDistillation() {
            const hasQuantize = document.getElementById('quantize').checked;
            const hasPruning = document.getElementById('prune').checked;

            for(let i=1; i<=4; i++) {
                document.getElementById('step' + i).className = "flex items-center gap-3 p-3 bg-slate-900/20 border border-blue-950 rounded-lg opacity-40 transition-all duration-300";
            }
            document.getElementById('distill-output').classList.add('hidden');

            setTimeout(() => { document.getElementById('step1').className = "flex items-center gap-3 p-3 bg-[#111c35] border border-blue-500/40 rounded-lg scale-[1.01] transition-all duration-300"; }, 100);
            setTimeout(() => { document.getElementById('step2').className = "flex items-center gap-3 p-3 bg-[#111c35] border border-indigo-500/40 rounded-lg scale-[1.01] transition-all duration-300"; }, 700);
            setTimeout(() => { document.getElementById('step3').className = "flex items-center gap-3 p-3 bg-[#111c35] border border-purple-500/40 rounded-lg scale-[1.01] transition-all duration-300"; }, 1400);
            setTimeout(() => { 
                document.getElementById('step4').className = "flex items-center gap-3 p-3 bg-[#111c35] border border-cyan-500/40 rounded-lg scale-[1.01] transition-all duration-300"; 
                
                let finalReduction = 50 + (hasQuantize ? 25 : 0) + (hasPruning ? 12 : 0);
                let finalSpeed = 1.5 + (hasQuantize ? 2.0 : 0) + (hasPruning ? 1.1 : 0);
                
                document.getElementById('out-mem').innerText = `-${finalReduction}%`;
                document.getElementById('out-speed').innerText = `${finalSpeed.toFixed(1)}x Fast`;
                document.getElementById('out-format').innerText = hasQuantize ? "TensorFlow Lite (INT8)" : "ONNX Runtime v2";
                
                document.getElementById('distill-output').classList.remove('hidden');
            }, 2100);
        }

        window.onload = () => {
            lucide.createIcons();
            calculatePredictions();
        };
    </script>
</body>
</html>
"""

# 3. Render inside the Streamlit context seamlessly with full width and viewport calculation height
components.html(responsive_dashboard_html, height=850, scroller=True)
