const funFacts = [
    "Justin Bieber was discovered on YouTube.",
    "He plays drums, guitar, and piano.",
    "Justin Bieber's first album was 'My World'.",
    "He has won multiple Grammy Awards.",
    "His favorite color is purple."
];

const factList = document.getElementById("fun-facts-list");
const factBtn = document.getElementById("new-fact-btn");

factBtn.addEventListener("click", () => {
    const randomFact = funFacts[Math.floor(Math.random() * funFacts.length)];
    factList.innerHTML = `<li>${randomFact}</li>`;
});
