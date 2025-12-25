const fileInput = document.querySelector('input[type="file"]');
const uploadText = document.querySelector('.upload-content .text');
const form = document.querySelector('form');
const button = document.querySelector('button');

fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    uploadText.textContent = fileInput.files[0].name;
  }
});

form.addEventListener('submit', () => {
  button.textContent = "Predicting...";
  button.disabled = true;
});

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (!file.name.endsWith('.csv')) {
    alert("Please upload a CSV file only");
    fileInput.value = "";
  }
});
function askAI() {
  const questionBox = document.getElementById("ai-question");
  const answerBox = document.getElementById("ai-answer");

  const question = questionBox.value.trim();

  if (!question) {
    alert("Please enter a question for the AI");
    return;
  }

  answerBox.textContent = "AI is thinking... ⏳";

  fetch("/ask-ai", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question: question })
  })
    .then(response => response.json())
    .then(data => {
      answerBox.textContent = data.answer;
    })
    .catch(error => {
      answerBox.textContent = "Error communicating with AI service.";
      console.error(error);
    });
}


