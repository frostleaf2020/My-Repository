"use strict";

document.getElementById("b_en").onclick = function() {
  var t_en = document.getElementById("inp").value;
  document.getElementById('outp').innerText = xmorse.encode(t_en);
}

document.getElementById("b_de").onclick = function() {
  var t_en = document.getElementById("inp").value;
  document.getElementById('outp').innerText = xmorse.decode(t_en);
}

document.getElementById("b_co").onclick = function() {
  document.getElementById("outp").select();
  document.execCommand("copy");
}
