const canvas = document.getElementById("monteCarloCanvas");
const ctx = canvas.getContext("2d");
const pointCountDisplay = document.getElementById("pointCount");
const piEstimateDisplay = document.getElementById("piEstimate");
const startButton = document.getElementById("startButton");
const resetButton = document.getElementById("resetButton");

const width = canvas.width;
const height = canvas.height;
const centerX = width / 2;
const centerY = height / 2;
const radius = width / 2;

let totalPoints = 0;
let pointsInCircle = 0;
let animationId = null;

// Draw the initial circle
ctx.beginPath();
ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
ctx.strokeStyle = "#000";
ctx.stroke();

function reset() {
    totalPoints = 0;
    pointsInCircle = 0;
    pointCountDisplay.textContent = "0";
    piEstimateDisplay.textContent = "0";
    ctx.clearRect(0, 0, width, height);
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.stroke();
}

function simulatePoint() {
    const x = Math.random() * width;
    const y = Math.random() * height;
    
    const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
    const isInside = distance <= radius;
    
    ctx.fillStyle = isInside ? "blue" : "red";
    ctx.fillRect(x, y, 2, 2);
    
    totalPoints++;
    if (isInside) pointsInCircle++;
    
    const piEstimate = 4 * (pointsInCircle / totalPoints);
    
    pointCountDisplay.textContent = totalPoints.toLocaleString();
    piEstimateDisplay.textContent = piEstimate.toFixed(6);
    
    if (totalPoints < 100000) {
        animationId = requestAnimationFrame(simulatePoint);
    }
}

startButton.addEventListener("click", () => {
    if (!animationId) {
        simulatePoint();
    }
});

resetButton.addEventListener("click", () => {
    cancelAnimationFrame(animationId);
    animationId = null;
    reset();
});

reset();