const tables = document.querySelectorAll(".element");
const color_panel = document.querySelector(".color-panel");
const container = document.querySelector(".container");
HideColors();
let current_selected;
container.addEventListener("dblclick", function (e) {
  if (e.target.classList.contains("element")) {
    if (e.target == current_selected) {
      RemoveBoarder();
      HideColors();
    } else {
      current_selected = e.target;
      RemoveBoarder();
      ShowColors();
      color_panel.addEventListener("click", function (color) {
        if (color.target.classList.contains("green")) {
          current_selected.style.backgroundColor = "green";
        } else if (color.target.classList.contains("blue")) {
          current_selected.style.backgroundColor = "blue";
        } else if (color.target.classList.contains("orange")) {
          current_selected.style.backgroundColor = "orange";
        } else if (color.target.classList.contains("white")) {
          current_selected.style.backgroundColor = "white";
        } else if (color.target.classList.contains("red")) {
          current_selected.style.backgroundColor = "red";
        } else if (color.target.classList.contains("yellow")) {
          current_selected.style.backgroundColor = "yellow";
        } else if (color.target.classList.contains("pink")) {
          current_selected.style.backgroundColor = "pink";
        } else if (color.target.classList.contains("gold")) {
          current_selected.style.backgroundColor = "gold";
        }

      });
      current_selected.style.border = "2px solid black";
    }
  }
});

//Remove Borders
const RemoveBoarder = function () {
  tables.forEach((table) => {
    table.style.border = "none";
  });
};

//Show Color Panel
const ShowColors = function () {
  color_panel.classList.remove("hidden");
};

// Hide Color Panel
function HideColors() {
  color_panel.classList.add("hidden");
}

function saveColors() {
  let arrayColors = [];
  let child;
  let color;
  let parent = document.getElementById('container');
  let children = parent.children;
  for (let i = 0; i < children.length; i++) {
    child = children[i];
    color = child.style.backgroundColor;
    
    if (color == 'red') {
      color = 'red';
    } else if (color == 'gold') { 
      color = 'gold';
    } else if (color == 'pink') { 
      color = 'pink';
    } else if (color == 'orange') { 
      color = 'orange';
    } else if (color == 'yellow') { 
      color = 'yellow';
    }  else if (color == 'blue') { 
      color = 'blue';
    }  else if (color == 'white') { 
      color = 'white';
    }  else if (color == 'green') { 
      color = 'green';
    }  
    arrayColors.push(color);
  }

  let form = document.getElementById('form');
  let inputTag;
  for (let index = 0; index < arrayColors.length; index++) {
    const element = arrayColors[index];
    inputTag = `<input type="text" name="${index}" value="${element}" style="display: none;"></input>`;
    form.innerHTML = form.innerHTML + inputTag;
  }

  form.submit()
}
