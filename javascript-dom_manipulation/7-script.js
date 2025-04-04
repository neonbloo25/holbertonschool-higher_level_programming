fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(response => response.json())
.then(data => {
  let moviesList = document.querySelector("#list_movies");
  data.results.forEach(movie => {
    let li = document.createElement("li");
    li.textContent = movie.title;
    moviesList.appendChild(li);
  });
})
.catch(error => console.log(error));
