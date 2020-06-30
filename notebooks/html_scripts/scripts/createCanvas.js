//Avoid use of "const" as it can cause "identifier already declared" error if cell is re-ran

//holds colour name e.g. "goldenrod" and HEX code.
var selectedID = "";
var selectedValue = "";

//holds the encoded pattern infromation("abcdef-") in an array of arrays
var textCanvas = [[],[]];

//updates the stylesheet to have a grid of dimnensions specified
function setCSSGrid(rows, cols) {
  let canvas = document.getElementById("canvas");
  canvas.style.setProperty('--canvas-rows', rows);
  canvas.style.setProperty('--canvas-cols', cols);
}

// Called by makeGrid
// input: dimensions of canvas
// output: an array of specified size where each element is '-'
//update the 2d array representation of the canvas when a canvas button is pressed
function createTextCanvas(rows,cols) {
  var tempCanvas = [...Array(Number(rows)).keys()].map(e => Array(Number(cols)));

  for (let i = 0; i<rows; i++) {
    for (let j = 0; j<cols; j++) {
       tempCanvas[i][j] = "-";
    }
  }
  return tempCanvas;
}


// called by canvas buttons
// input row  and column specifying the button
// output: None
// updates the array holding the encoded canvas pattern to show a change in the canvas
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

//makes canvas visible
function showPaintArea() {
  let paintArea = document.getElementById("paint-area");
  paintArea.style.display = "block";
}

//called by setGrid and updateCanvas
//input: dimensions of the array
//output: an array of specified size where each element is '-'
//Creates the blank encoded pattern
function makeGrid(rows, cols) {
  setCSSGrid(rows,cols);
  let canvas = document.getElementById("canvas");

  for (let i = 0; i<rows*cols; i++) {
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

// called by save
// input: array holding 'abcdef-' encoded patten
// return: a string encoding the 'abcdef' pattern
function canvasArrToString(arr) {
  let dims = [arr[0].length, arr.length];
  let stringCanvas = "";

  for(let i = 0; i<dims[1]; i++) {
    for(let j = 0; j<dims[0]; j++) {
      stringCanvas = stringCanvas + arr[i][j];
    }
    stringCanvas = stringCanvas + "\\n";
  }
  return stringCanvas;
}

// called by setGrid, loadCanvas and save button
// input: none
// output: none
// Calls python code to create dirList file which lists all patterns in '/patterns'
function createDirList() {
  let kernel = IPython.notebook.kernel;
  let command = "generate_pattern_dir_listing()";
  kernel.execute(command);
}

// called up updateCanavas and setGrid
// input: none
// output:none
// removes all buttons from the grid
function removeGrid() {
  [].forEach.call(document.querySelectorAll('.canvas-square'), function(e){
    e.parentNode.removeChild(e);
  });
}

// Called by CreateBlank Canvas button
// input: none
// output: none
// grabs the values selected for height and width and creates the grid of buttons
function setGrid(){
  let rows = Math.floor(document.getElementById("height").value);
  let cols = Math.floor(document.getElementById("width").value);

  //clips input if out of range
  if (rows<4) {rows=4;}
  else if(rows>50) {rows=50;}
  if (cols<4) {cols=4;}
  else if (cols>50) {cols=50;}

  //clears existing settings
  selectedID = "";
  selectedValue = "";
  removeGrid();

  //updates screen with new settings
  createDirList();
  textCanvas = makeGrid(rows,cols);
}

//called by asyncUpdateFileList
//input: the file select html element
//output: none
//removes all option from the dropdown menu
function removeOptions(fileSelect) {
  let length = fileSelect.options.length;
  for (let i = length-1; i>=0; i--) {
    fileSelect.remove(0);
  }
}

// called throughout
// input: none
// output: a list of the files listed in '/patterns/dirList'
async function getFileDir() {
  try{
    const response = await fetch("patterns/dirList");
    const data = await response.text();
    const dirList = await data.split(", ");
    return dirList;
  } catch {
    console.error("failed to grab list");
  }
}

// called by updateFileList
// input: none
// output: none
// get the current dirList file and update the dropdown menu with availble patterns
async function asyncUpdateFileList(fromRefresh) {
  try{
    let dirList  = await getFileDir();
    if(dirList) {
      let fileSelect = document.getElementById("file-list");
      removeOptions(fileSelect);
      for(elem in dirList){
        let newOption = new Option(dirList[elem], dirList[elem]);
        fileSelect.add(newOption, undefined);
      }
    }
  if(fromRefresh){
    document.getElementById("paint-area").style.display = "none";
  }
  }catch{
    console.error("failed to grab list");
  }
}

// Called by the Refresh button
// input: none
// output: none
// resets the canvas then 0.5 seconds later
function updateFileList(){
  loadCanvas();
  setTimeout(function(){ asyncUpdateFileList("true"); }, 500);
}

// Called by saveAndDisplay 3 seconds after saving
// input: fileName
// output: none
// writes out the save status beside the save button
async function isSaved(fileName){
  try{
    const checkResponse = await fetch("patterns/"+ fileName);
    const checkData = await checkResponse.text();
    if(checkData) {
      document.getElementById("status-text").innerHTML = "filename: '" + fileName + "' saved.";
    }
  } catch {
    document.getElementById("status-text").innerHTML = "try saving again.";
  }
}

// Called by saveAndDisplay
// input: the fileName selected
// output:  none
// Calls the python code to save the pattern
function save(fileName){
  let stringCanvas = canvasArrToString(textCanvas);
  let kernel = IPython.notebook.kernel;
  let command = "save_edited_pattern('" + fileName + "', '" + stringCanvas + "')";
  kernel.execute(command);
}

// Called by the save button
// input: the fileName specified by the dropdown
// output: none
// checks if the fileName is already in use, saves if not
async function saveAndDisplay(fileName) {
  try{
    //from the patternsFolder read the "dirList" file and check if the fileName is used
    const dirList = await getFileDir();
    const nameUsed = dirList.includes(fileName);
    if (nameUsed) {
      document.getElementById("status-text").innerHTML = "filename: '" + fileName + "' already used";
    } else {
      save(fileName);
      document.getElementById("status-text").innerHTML = "Saving...";
      setTimeout(function() { isSaved(fileName); }, 3000);
    }
  } catch {
    document.getElementById("status-text").innerHTML = "File failed to save.";
  }
}

// Called by up updateCanvas
// input: an 2d Array storing the 'abcdef-' code
// output: none
// updates button colours to reflect the pattern
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

  for(let col=0; col<patternArr[0].length; col++){
    for(let row=0; row<patternArr.length; row++){
      let symbol = patternArr[row][col];
      if (symbol!== "-") {
        let index = row + "," + col
        document.getElementById(index).style.backgroundColor = colourDict[symbol];
      }
    }
  }
}


// Called by loadCanvas
// input: a pattern string in "abcdef-"
// output: the string in a 2d array format
function patternToArr(pattern) {
  let patternArr = pattern.split("\n");

  if (patternArr[patternArr.length -1] === "") {
    patternArr.splice(-1,1);
  }

  let cols = patternArr[0].length;
  let regular = patternArr.every((elem) => elem.length === cols);
  if (!regular) {
    return 0;
  }
  //turn each element of the array into an array
  patternArr = patternArr.map((x) => x.split(""));
  return patternArr;
}

// called by loadCanvas
// input: an array of 'abcdef-'
// output: none
// generates the new html grid
function updateCanvas(patternArr){
  //hides the current grid
  document.getElementById("paint-area").style.display = "none";

  let cols = patternArr[0].length;
  let rows = patternArr.length;

  //if the dimesions are okay, delete the old grid and display a new one
  if(cols>=4 && cols<=50 && rows>=4 && rows<=50){
    selectedID = "";
    selectedValue= "";
    removeGrid();
    makeGrid(rows,cols);
    setColours(patternArr);
    textCanvas = patternArr;
  } else {
    document.getElementByID("load-status") = "canvas dimensions outside of range";
  }
}

//Called by Edit Canvas button
//input: none
//output: none
//grabs the file selected and outputs it on the canvas below
async function loadCanvas() {
  // grab the file selected by user
  let e = document.getElementById("file-list");
  fileName = e.options[e.selectedIndex].value
  try {
    //load the 'abcdef-' string from the motif file selected
    const response = await fetch("patterns/"+ fileName);
    const pattern = await response.text();
    patternArr = patternToArr(pattern);

    //update the dirList file in the pattern directory
    createDirList();

    //if the patternfile is legitimate(dimensions agree)
    if(patternArr) {
      updateCanvas(patternArr);
    }else{
      document.getElementByID("load-status") = "canvas dimensions outside of range";
    }
  } catch {
    console.error("did not load");
  }
}

//hide the canvas
document.getElementById("paint-area").style.display = "none";

//place onClick on the pallette buttons
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

//placed onClick on the save button
document.querySelectorAll('.save-btn').forEach(function(e) {
  e.addEventListener('click', function() {
    createDirList();
    let fileName = document.getElementById("file-name").value;
    saveAndDisplay(fileName);
  })
});

asyncUpdateFileList("false");
