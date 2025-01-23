/*
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
*/
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

    const driver = race.results;

    const ObjectLenght = Object.keys(driver).length;

    for (let i = 0; i < ObjectLenght; i++) {
      console.log(driver[i].DriverNum);
      console.log(driver[i].Laps);
      console.log(driver[i].Pos);
      console.log(driver[i].TimeToLeader);
      console.log(driver[i].Driver);
      console.log("-------------------");
    }

    console.log(race);
  } catch (error) {
    console.error("Error fetching the JSON file:", error);
  }
}
