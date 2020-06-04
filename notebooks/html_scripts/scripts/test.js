//Avoid use of "const" as it can cause "identifier already declared" error if cell is re-ran

//holds colour name e.g. "goldenrod" and HEX code.
var selectedID = "";
var selectedValue = "";

//holds the encoded pattern infromation("abcdef-") in an array of arrays
var textCanvas = [[],[]];



function setCSSGrid(rows, cols) {
  let canvas = document.getElementById("canvas");
  canvas.style.setProperty('--canvas-rows', rows);
  canvas.style.setProperty('--canvas-cols', cols);
}

function createTextCanvas(rows,cols) {
  var tempCanvas = [...Array(Number(rows)).keys()].map(e => Array(Number(cols)));

  for (let i=0; i<rows; i++) {
    for (let j=0; j<cols; j++) {
       tempCanvas[i][j] = "-";
    }
  }
  return tempCanvas;
}

function updateTextCanvas(row, col) {
  let colourDict = {
    "#000000": "a",
    "#F5DEB3": "b",
    "#800000": "c",
    "#ffe07c": "d",
    "#DAA520": "e",
    "#F0E68C": "f",
    "#d5a967": "-"
  };

  textCanvas[row][col] = colourDict[selectedValue];
}

function showPaintArea() {
  let paintArea = document.getElementById("paint area");
  paintArea.style.display = "block";
}

function makeGrid(rows, cols) {
  setCSSGrid(rows,cols);
  let canvas = document.getElementById("canvas");

  for (let i = 0; i < rows*cols; i++) {
    let btn = document.createElement("button");
    btn.id = Math.floor(i/cols) + ',' +  i % cols;

    var cln = btn.cloneNode(true);
    canvas.appendChild(cln).className = "canvas-square";
  }

  document.querySelectorAll('.canvas-square').forEach(function(e) {
    e.addEventListener('click', function() {
      if (selectedID) {
        this.style.backgroundColor = selectedValue;
        let id = this.id;
        let coords = id.split(",")
        updateTextCanvas(coords[0], coords[1]);
      }
    })
  });
  show();
  return createTextCanvas(rows, cols);

}

function canvasArrToString(arr) {
  let dims = [arr[0].length, arr.length];
  let stringCanvas = "";

  for(let i=0; i<dims[1]; i++) {
    for(let j=0; j<dims[0]; j++) {
      stringCanvas = stringCanvas + arr[i][j];
    }
    if(i<dims[1]-1) {
      stringCanvas = stringCanvas + "\\n";
    }
  }
  return stringCanvas;
}

function createDirList() {
  let kernel = IPython.notebook.kernel;
  let command = "generate_pattern_dir_listing()";
  kernel.execute(command);
}

/*setGrid creates all the variables needed for the canvas
 * is ran by the clicking the shape button
  * */
function setGrid(){
  let rows = document.getElementById("height").value;
  let cols = document.getElementById("width").value;
  createDirList();
  textCanvas = makeGrid(rows,cols);
}

document.getElementById("paint area").style.display = "none";

async function displaySaveStatus(url, fileName) {
  try{
    const response = await fetch(url)
    const data = await response.text();
    console.log(data);
    dirList = data.split(", ");
    if(dirList.includes(fileName)) {
      console.log("it saved");
    } else {
      console.log("it did not save");
    }
  } catch {
      console.error(err);
    }
}

async function save(url) {
  try {
    let fileName = document.getElementById("file-name").value;
    const response = await fetch(url);
    const data = await response.text();
    console.log(data);
    console.log(fileName);
    dirList = data.split(', ');
    console.log("list:", dirList);
    if(dirList.includes(fileName)) {
      console.log("failure")
    } else {
      let stringCanvas = canvasArrToString(textCanvas);
      let kernel = IPython.notebook.kernel;
      let command = "save_edited_pattern('" + fileName + "', '" + stringCanvas + "')";
      kernel.execute(command);
      setTimeout(function(){displaySaveStatus(url, fileName); }, 1000);
    }
   } catch {
   console.error("catch");
   }
}

document.querySelectorAll('.colour-options').forEach(function(e) {
  e.addEventListener('click', function() {
    this.style.borderColor = "green";
    if(selectedID && selectedID !== this.id) {
      document.getElementById(selectedID).style.borderColor = "";
    }
    selectedID = this.id;
    selectedValue = this.value;
  })
});

document.querySelectorAll('.save-btn').forEach(function(e) {
  e.addEventListener('click', function() {
    save('patterns/dirList');
  })
});
