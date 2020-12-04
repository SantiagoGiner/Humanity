document.addEventListener('DOMContentLoaded', () => {
    const searchResult = document.getElementById('search_result');
    const searchButton = document.getElementById('search');
    searchButton.onclick = () => {
        const query = document.getElementById('query').value;
        $.ajax({
            url: `https://www.googleapis.com/books/v1/volumes?q="${query}"`,
            dataType: 'json',

            success: (data) => {
                let html = '';
                for(let i = 0; i < data.items.length; i++) {
                    html += `<form method="post">`
                    html += `<p class="container my-2">Title: "${data.items[i].volumeInfo.title}"</p>`;
                    html += `<input name="title" style="display:none;" value="${data.items[i].volumeInfo.title}">`;
                    html += `<p class="container my-2">Author(s): "${data.items[i].volumeInfo.authors}"</p>`;
                    html += `<input name="author" style="display:none;" value="${data.items[i].volumeInfo.authors}">`;
                    if(data.items[i].volumeInfo.imageLinks) {
                        html += `<img class="img mb-4" src="${data.items[i].volumeInfo.imageLinks.thumbnail}">`;
                        html += `<input name="cover" style="display:none;" value="${data.items[i].volumeInfo.imageLinks.thumbnail}">`;
                    }
                    html += `<button class="btn btn-success mx-2" type="submit">Select</button>`;
                    html += '</form>'
                    html += '<hr>';
                }
                searchResult.innerHTML = html;
            }
        });
    }
});