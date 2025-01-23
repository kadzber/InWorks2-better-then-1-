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
      var DriverNum = driver[i].DriverNum;
      var Laps = driver[i].Laps;
      var Pos = driver[i].Pos;
      var TimeToLeader = driver[i].TimeToLeader;
      var Driver = driver[i].Driver;

      const body = document.querySelector("tbody");
      let tags = "";

      driver.map((d) => {
        tags += `<tr>
        <td>  ${d.Pos}     </td>
        <td>  ${d.DriverNum}     </td>
        <td>  ${d.Driver}     </td>                
        <td>  ${d.TimeToLeader}      </td>     
        <td>  ${d.Laps}     </td>`;
      });
      body.innerHTML = tags;
    }

    console.log(race);
  } catch (error) {
    console.error("Error fetching the JSON file:", error);
  }
}
