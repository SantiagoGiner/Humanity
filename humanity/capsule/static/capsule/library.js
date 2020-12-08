// Wait for page content to be loaded
document.addEventListener('DOMContentLoaded', () => {
    const searchResult = document.getElementById('search_result');
    const searchButton = document.getElementById('search');
    // When the search button is clicked
    searchButton.onclick = () => {
        const query = document.getElementById('query').value;
        // Do an AJAX call to the Google Books API with the user's query
        $.ajax({
            url: `https://www.googleapis.com/books/v1/volumes?q="${query}"&langRestrict=en&key=AIzaSyDELF8MtiIWbSsCTypDl_ApypKcs4HcPX8`,
            dataType: 'json',
            // If the query is successful
            success: (data) => {
                // If query returned a result
                if (data.items != undefined) {
                    let html = '';
                    // Display the query results, including book title, author(s), and cover photo
                    for (let i = 0; i < data.items.length; i++) {
                        // Form that when submitted will indicate that the user has selected one book
                        html += `<form method="post">`;
                        // Display the book title, with a hidden input containing said title
                        html += `<p class="container my-2">Title: 
                                ${data.items[i].volumeInfo.title}</p>`;
                        html += `<input name="title" style="display:none;" 
                                value="${data.items[i].volumeInfo.title}">`;
                        // Display the author(s) along with another hidden input containing these
                        html += `<p class="container my-2">Author(s): 
                                ${data.items[i].volumeInfo.authors}</p>`;
                        html += `<input name="author" style="display:none;" 
                                value="${data.items[i].volumeInfo.authors}">`;
                        // If there are image links, display the cover photo
                        if (data.items[i].volumeInfo.imageLinks != undefined) {
                            html += `<img class="img mb-4" 
                                    src="${data.items[i].volumeInfo.imageLinks.thumbnail}">`;
                            // Hidden input with the image source
                            html += `<input name="cover" style="display:none;"
                                        value="${data.items[i].volumeInfo.imageLinks.thumbnail}">`;
                        }
                        // If there is a description, save it as a hidden input in the form
                        if (data.items[i].volumeInfo.description != undefined) {
                            html += `<input name="description" style="display:none;" 
                                       value=${JSON.stringify(data.items[i].volumeInfo.description)}>`;
                        }
                        // Add the select button and end the form
                        html += `<button class="btn btn-success mx-2" type="submit">Select</button>`;
                        html += '</form>';
                        html += '<hr>';
                    }
                    // Set the HTML of the search result section to be the newly generated
                    searchResult.innerHTML = html;
                }
                // If query did not return any results, inform the user so
                else {
                    searchResult.innerHTML = '<h4>That query did not return any results!</h4>';
                }
            },
            // If query could not be carried out, inform the user thusly
            error: () => {
                searchResult.innerHTML = '<h4>Invalid input: please try with different words</h4>';
            }
        });
    }
});