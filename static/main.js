function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("fl-table");
  switching = true;
  dir = "asc"; 
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          for (let x = 0; x < 15; x++) {
            var tableheader = document.getElementById("table" + x)
            var headertext = tableheader.innerText
            headertext = headertext.replace("↑", "")
            headertext = headertext.replace("↓", "")
            headertext = headertext.replace(" ", "")
            tableheader.innerText = headertext
          }
          var realtableheader = document.getElementById("table" + n)
          var realheadertext = realtableheader.innerText
          realtableheader.innerText = realheadertext + " ↑"
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          for (let x = 0; x < 15; x++) {
            var tableheader = document.getElementById("table" + x)
            var headertext = tableheader.innerText
            headertext = headertext.replace("↑", "")
            headertext = headertext.replace("↓", "")
            headertext = headertext.replace(" ", "")
            tableheader.innerText = headertext
          }
          var realtableheader = document.getElementById("table" + n)
          var realheadertext = realtableheader.innerText
          realtableheader.innerText = realheadertext + " ↓"
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount ++;      
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function addlinktodd(country, time){
  var mydiv = document.getElementById("myDropdown");
  var aTag = document.createElement('a');
  aTag.setAttribute('href',"https://tablepython.vulcanwm.repl.co/data/" + country + "/" + time);
  aTag.innerText = time;
  mydiv.appendChild(aTag);
}

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}