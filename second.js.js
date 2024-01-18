let url = "https://kontests.net/api/v1/all";
let response = fetch(url);

response
  .then((v) => {
    return v.json();
  })
  .then((data) => {
    // Assuming you have a cardContainer element with the class "cardContainer"
    let cardContainers = document.querySelectorAll(".cardContainer");

    // Loop through all elements with the class "cardContainer" and update their content
    cardContainers.forEach((cardContainer) => {
      cardContainer.innerHTML = JSON.stringify(data);
    });
  })