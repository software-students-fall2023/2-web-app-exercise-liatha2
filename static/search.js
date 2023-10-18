window.onload = function () {
    var text = "SearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\nSearchSearchSearchSearchSearchSearch\n"
    var div = document.getElementById("title");
    var index = 0;
    var cursor = document.createElement("span");
    cursor.id = "cursor";
    cursor.textContent = "|";
    div.appendChild(cursor);
  
    function typeWriter() {
      if (index < text.length) {
        var letter = document.createTextNode(text[index]);
        var span = document.createElement("span");
        span.appendChild(letter);
        div.insertBefore(span, cursor);
        index++;
        setTimeout(typeWriter, 200); // Add more delay here if you want slower typing
      } else {
        div.removeChild(cursor);
      }
    }
   
  typeWriter();
  };
  