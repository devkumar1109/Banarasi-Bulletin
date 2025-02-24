window.onload = function () {
    document.getElementById("searchBar").addEventListener("input", searchArticles);
};

function searchArticles() {
    const query = document.getElementById("searchBar").value.trim();

    if (query.length === 0) {
        document.getElementById("searchResults").innerHTML = "";
        return;
    }

    console.log("Searching for:", query);  // Debugging log

    fetch(`/api/search?q= ${encodeURIComponent(query)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Search results:", data); // Debugging log

            const resultsContainer = document.getElementById("articles-container");
            resultsContainer.innerHTML = "";

            if (data.length === 0) {
                resultsContainer.innerHTML = "No articles found.";
                return;
            }

            data.forEach(article => {
                const capsule = document.createElement("div");
                capsule.classList.add("capsule");
                capsule.style.cursor = 'pointer';

                const img = document.createElement("img");
                img.src = article.image; // Assuming the API returns an image URL
                img.alt = article.title;

                const title = document.createElement("h3");
                title.innerText = article.title;

                capsule.appendChild(img);
                capsule.appendChild(title);

                // Link to the corresponding blog page
                capsule.onclick = () => {
                    window.location.href = article.link; // Link from the API response
                };

                resultsContainer.appendChild(capsule);
            });
        })
        .catch(error => console.error("Error fetching search results:", error));
}
