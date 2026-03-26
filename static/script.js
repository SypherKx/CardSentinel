// Initialize Lucide icons
lucide.createIcons();

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predict-form');
    const submitBtn = document.getElementById('submit-btn');
    const inputField = document.getElementById('features-input');
    
    const resultContainer = document.getElementById('result-container');
    const loadingSpinner = document.getElementById('loading-spinner');
    const predictionResult = document.getElementById('prediction-result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const features = inputField.value.trim();
        if (!features) return;

        // Reset UI state
        resultContainer.classList.remove('hidden');
        loadingSpinner.classList.remove('hidden');
        predictionResult.classList.add('hidden');
        submitBtn.disabled = true;

        try {
            // Fake delay for aesthetic scanning effect
            await new Promise(resolve => setTimeout(resolve, 800));

            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ features: features })
            });

            const data = await response.json();
            
            loadingSpinner.classList.add('hidden');
            predictionResult.classList.remove('hidden', 'safe', 'fraud');

            if (response.ok) {
                if (data.status === 'legit') {
                    predictionResult.classList.add('safe');
                    predictionResult.innerHTML = `
                        <i data-lucide="shield-check" class="status-icon"></i>
                        <div class="result-content">
                            <h3>Transaction Secure</h3>
                            <p>No anomalous patterns detected. Transaction authorized.</p>
                        </div>
                    `;
                } else {
                    predictionResult.classList.add('fraud');
                    predictionResult.innerHTML = `
                        <i data-lucide="shield-alert" class="status-icon"></i>
                        <div class="result-content">
                            <h3>Fraud Alert</h3>
                            <p>Anomalous signature detected. Transaction blocked for security.</p>
                        </div>
                    `;
                }
            } else {
                predictionResult.classList.add('fraud'); // Reuse fraud styling for errors visually
                predictionResult.style.borderColor = "var(--border-color)";
                predictionResult.style.backgroundColor = "rgba(0,0,0,0.5)";
                predictionResult.style.animation = "none";
                predictionResult.innerHTML = `
                    <i data-lucide="alert-circle" style="color:var(--text-secondary); width:32px; height:32px; flex-shrink:0;"></i>
                    <div class="result-content">
                        <h3 style="color:var(--text-primary);">Analysis Failed</h3>
                        <p>${data.error || 'Server error occurred during network analysis.'}</p>
                    </div>
                `;
            }
            
            // Re-initialize any new icons injected into the DOM
            lucide.createIcons();

        } catch (error) {
            loadingSpinner.classList.add('hidden');
            predictionResult.classList.remove('hidden', 'safe', 'fraud');
            predictionResult.innerHTML = `
                <i data-lucide="wifi-off" style="color:var(--text-secondary); width:32px; height:32px; flex-shrink:0;"></i>
                <div class="result-content">
                    <h3 style="color:var(--text-primary);">Connection Error</h3>
                    <p>Unable to reach the Sentinel Network. Check your connection.</p>
                </div>
            `;
            lucide.createIcons();
        } finally {
            submitBtn.disabled = false;
        }
    });

    // Auto-resize textarea
    inputField.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
});
