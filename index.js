// Getting references to the h1 tag that will display the count, the increment, and decrement buttons
var $count = document.querySelector(".panel h1");
var $incrementBtn = document.querySelector(".panel .btn.btn-primary");
var $decrementBtn = document.querySelector(".panel .btn.btn-danger");


// Add click event listeners to the buttons, call the functions passed in
$incrementBtn.addEventListener("click", handleIncrementClick);
$decrementBtn.addEventListener("click", handleDecrementClick);

// Initialize the count at 0
var count = 0;
var current_font_size = parseInt(window.getComputedStyle($count, null).getPropertyValue('font-size'),10)
var red = 0;
var blue = 0;

// Render the count value to the page for the first time when it loads
renderCount();

function renderCount() {
  // Update the inner text of the $count element
  $count.innerText = count;
  $count.style.fontSize = `${current_font_size}px`;
  $count.style.color = `rgb(${red},0,${blue})`
}

// handleDecrementClick decreases count by 1 and re-renders the count to DOM
function handleDecrementClick() {
  count -= 2;
  current_font_size -= 2;
  red += 40;
  blue -= 40;
  renderCount();
}

// handleIncrementClick increases count by 1 and re-renders the count to DOM
function handleIncrementClick() {
  count += 2;
  current_font_size += 2;
  red -= 40;
  blue += 40;
  renderCount();
}
