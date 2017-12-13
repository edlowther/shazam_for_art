(
  function() {
    var upload_input = document.getElementById("file-upload");
    console.log(upload_input);
    upload_input.onchange = function() {
      console.log("Painting selected: " + this.value.replace("C:\\fakepath\\", ""));
      var label = document.getElementById('upload_label');
      console.log(label);
      label.innerHTML = "Painting selected: " + this.value.replace("C:\\fakepath\\", "");
    };
  }
)();
