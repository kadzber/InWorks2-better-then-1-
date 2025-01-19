async function fetchJsonFile() {
  try {
    const inputValue = document.getElementById("inputField").value.trim();
    const [x, y] = inputValue.split(" ");

    if (!x || !y) {
      throw new Error("Invalid input. Please provide both year and round.");
    }

    const response = await fetch("race_results.json");

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    const race = data[x][y];

    console.log(race);
  } catch (error) {
    console.error("Error fetching the JSON file:", error);
  }
}
