function startCamera(videoElementId) {
    const video = document.getElementById(videoElementId);
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
                window.localStream = stream;
            })
            .catch(function(err) {
                console.error("Error accessing camera:", err);
                alert("Cannot access the camera. Please check permissions.");
            });
    } else {
        alert("Camera not supported on this browser.");
    }
}

function stopCamera() {
    if (window.localStream) {
        window.localStream.getTracks().forEach(track => track.stop());
    }
}

function captureFrame(videoElementId) {
    const video = document.getElementById(videoElementId);
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL('image/jpeg', 0.8);
}

async function sendFaceToAPI(endpoint, base64Image, btnElement) {
    const originalText = btnElement.innerHTML;
    btnElement.innerHTML = 'Processing...';
    btnElement.disabled = true;

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: base64Image })
        });
        const result = await response.json();
        
        btnElement.innerHTML = originalText;
        btnElement.disabled = false;
        
        return result;
    } catch (error) {
        console.error("API Error:", error);
        btnElement.innerHTML = originalText;
        btnElement.disabled = false;
        return { success: false, msg: "Network error occurred." };
    }
}
