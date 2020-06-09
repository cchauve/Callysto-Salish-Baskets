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
  let paintArea = document.getElementById("paint-area");
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
  showPaintArea();
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

function removeGrid() {
  [].forEach.call(document.querySelectorAll('.canvas-square'), function(e){
    e.parentNode.removeChild(e);
  });
}

/*setGrid creates all the variables needed for the canvas
 * is ran by the clicking the shape button
  * */
function setGrid(){
  let rows = document.getElementById("height").value;
  let cols = document.getElementById("width").value;
  if (rows < 5) {rows = 5;}
  else if(rows >50) {rows = 50;}
  if (cols < 5) {cols = 5;}
  else if (cols > 50) {cols = 50;}
  selectedID = "";
  selectedValue = "";
  removeGrid();
  createDirList();
  textCanvas = makeGrid(rows,cols);
}

function removeOptions(fileSelect) {
  let length = fileSelect.options.length;
  console.log("length of list:", length);
  for (let i = 0; i < length; i++) {
    fileSelect.remove(i);
    console.log("in remove list");
  }
}

async function getFileDir() {
  try{
    const response = await fetch("patterns/dirList");
    const data = await response.text();
    const dirList = await data.split(", ");
    console.log(dirList);
    return dirList;
  } catch {
    console.error("failed to grab list");
  }
}

async function updateFileList() {
  try{
    let dirList  = await getFileDir();
    console.log(dirList);
    if(dirList) {
      console.log("true List");
      let fileSelect = document.getElementById("file-list");
      removeOptions(fileSelect);
      for(elem in dirList){
        console.log("elem:", dirList[elem]);
        let opt = document.createElement("option");
        opt.value = dirList[elem];
        opt.innerHTML = dirList[elem];
        fileSelect.appendChild(opt);
      }
    }
  }catch{
    console.error("failed to grab list");
  }
}

/*Checks if a new patternfile has been created and updates
 * the text next to the save button appropriatly
 */
async function isSaved(fileName){
  try{
    const checkResponse = await fetch("patterns/"+ fileName);
    const checkData = await checkResponse.text();
    console.log(checkData);
    console.log(typeof checkData);
    if(checkData) {
      document.getElementById("status-text").innerHTML = "filename: '" + fileName + "' saved.";
    }
  } catch {
    document.getElementById("status-text").innerHTML = "try saving again.";
  }
}

function save(fileName){
  let stringCanvas = canvasArrToString(textCanvas);
  let kernel = IPython.notebook.kernel;
  let command = "save_edited_pattern('" + fileName + "', '" + stringCanvas + "')";
  kernel.execute(command);
}

async function saveAndDisplay(fileName) {
  try{
    const dirList = await getFileDir();
    const nameUsed = dirList.includes(fileName);
    if (nameUsed) {
      document.getElementById("status-text").innerHTML = "filename: '" + fileName + "' already used";
    } else {
      save(fileName);
      document.getElementById("status-text").innerHTML = "Saving...";
      setTimeout(function() { isSaved(fileName); }, 3000);
      setTimeout(function() { updateFileList(); }, 3000);
    }
  } catch {
    document.getElementById("status-text").innerHTML = "File failed to save.";
  }
}

function setColours(patternArr){
  const colourDict = {
    "a": "#000000",
    "b": "#F5DEB3",
    "c": "#800000",
    "d": "#ffe07c",
    "e": "#DAA520",
    "f": "#F0E68C",
    "-": "#d5a967"
  };
  console.log("in setColours");

  for(let col=0; col<patternArr[0].length; col++){
    for(let row=0; row<patternArr.length; row++){
      let symbol = patternArr[row][col];
      if (symbol!== "-") {
        let index = row + "," + col
        console.log(index, symbol);
        document.getElementById(index).style.backgroundColor = colourDict[symbol];
      }
    }
  }
}

function patternToArr(pattern) {
  let patternArr = pattern.split("\n");
  console.log(patternArr);
  if (patternArr[patternArr.length -1] === "") {
    patternArr.splice(-1,1);
  }
  console.log(patternArr);
  let cols = patternArr[0].length;
  let regular = patternArr.every((elem) => elem.length === cols);
  if (!regular) {
    return 0;
  }
  console.log("is reg");
  patternArr = patternArr.map((x) => x.split(""));
  console.log(patternArr);
  return patternArr;
}

function updateCanvas(patternArr){
  document.getElementById("paint-area").style.display = "none";
  cols = patternArr[0].length;
  rows = patternArr.length;
  if(cols >= 5 && cols <= 51 && rows >=5 && rows <= 50){
    selectedID = "";
    selectedValue= "";
    removeGrid();
    makeGrid(rows,cols);
    setColours(patternArr);

  } else {
    //print error
  }
}
async function loadCanvas() {
  let e = document.getElementById("file-list");
  fileName = e.options[e.selectedIndex].value
  console.log(fileName);
  try {
    const response = await fetch("patterns/"+ fileName);
    const pattern = await response.text();
    console.log(pattern);
    patternToArr(pattern);
    patternArr = patternToArr(pattern);
    if(patternArr) {
      updateCanvas(patternArr);
    }else{
      // put error message
    }
  } catch {
    console.error("did not load");
  }
}

document.getElementById("paint-area").style.display = "none";

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
    createDirList();
    let fileName = document.getElementById("file-name").value;
    saveAndDisplay(fileName);
  })
});

updateFileList();
