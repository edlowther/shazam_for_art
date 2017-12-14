(
  function() {
    var upload_input = document.getElementById("file-upload");
    upload_input.onchange = function() {
      var label = document.getElementById('upload_label');
      label.innerHTML = "Painting selected";
    };
  }
)();
