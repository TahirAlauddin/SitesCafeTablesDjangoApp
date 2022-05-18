const tables = document.querySelectorAll(".element");
const color_panel = document.querySelector(".color-panel");
const container = document.querySelector(".container");
let color_selector = document.getElementById("color-selector");
let counter = 0;
HideColors();
let current_selected;
container.addEventListener("dblclick", function (e) {
  console.log("double clicked")
  if (e.target.classList.contains("element")) {

    //? Adjusting top positioning of tables
    let tables = document.getElementById('container');
    let table;
    let previous_top;
    let new_top;  
    for (let i=0; i < tables.children.length; i++) {
      table = tables.children[i];
      previous_top = parseInt( table.style.top.slice(0, table.style.top.length-2) );
    }
    
    if (e.target == current_selected) {
      RemoveBorder();
      HideColors();
      color_selector.style.display = "none";
      current_selected = null;
    } else {
      current_selected = e.target;
      color_selector.style.display = "flex";
      RemoveBorder();
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
const RemoveBorder = function () {
  tables.forEach((table) => {
    table.style.border = "none";
  });
};

//Show Color Panel
// const ShowColors = function () {
function ShowColors() {
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
