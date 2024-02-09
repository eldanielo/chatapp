<script lang="ts">
  import { Navbar, NavBrand, NavLi, NavUl } from "flowbite-svelte";
  import { A } from "flowbite-svelte";
  import { Heading } from "flowbite-svelte";
  import { onMount } from "svelte";

  var text = ""
  var time = 0

  

  onMount(() => {
    console.log("onmount")

    const displayImage = document.getElementById("displayImage");
const imageUpload = document.getElementById("imageUpload");

displayImage.addEventListener("click", function() {
  console.log("image upload")
  imageUpload.click(); // Trigger the hidden file input
});

imageUpload.addEventListener("change", function() {
  const file = this.files[0]; // Get the selected file

  if (file) {
    const reader = new FileReader();

    reader.onload = function(event) {
      displayImage.src = event.target.result;
    };

    reader.readAsDataURL(file);
  }
});

    const toggleButton = document.getElementById("toggleButton");
const hiddenElement = document.getElementById("hiddenElement");
let isHidden = false; // Keep track of visibility

toggleButton.addEventListener("click", function() {
  if (isHidden) {
    hiddenElement.style.display = "block"; // Show
    toggleButton.textContent = "-------------- - --------------"       // Change to minus
    isHidden = false;
  } else {
    hiddenElement.style.display = "none"; // Hide
    toggleButton.textContent = "-------------- + --------------"      // Change back to plus
    isHidden = true;
  }
});

  const userInput = document.getElementById('userInput');
  const agentElement = document.getElementById('agent');

  userInput.addEventListener('change', function() {
    const inputValue = userInput.value;
    agentElement?.setAttribute('agent-id', inputValue);
    console.log("changed")
    console.log(agentElement?.getAttribute('agent-id'))

   

});
const header= document.getElementById('header')
let h1 = document.getElementById('h1')
let chattitle = document.getElementById('chat-title')
  header.addEventListener('input', function() {
    console.log("header" + header?.textContent);
    console.log(h1?.textContent)
    h1.textContent = "What is " + header?.textContent + " ?";
    chattitle?.setAttribute('chat-title', header?.textContent + " Vertex AI Search");
    chattitle?.setAttribute('placeholder-text', "Ask me anything about " + header?.textContent)

    
  });
  });
</script>
<head>
  <style>
    .navbar-brand { 
      display: flex;        
      align-items: center;
    }
    #h1 { /* More specificity to potentially override conflicts */
  font-size: 2.5em;  /* Make it larger */
  font-weight: bold; 
  margin-bottom: 1em; /* Add some spacing for visual separation */
}
  </style>
</head>
<header class="bg-[#B1D6FC]">
  <nav>
    <div class="navbar-brand"> 
      <img id="displayImage" src="nova.jpg" class="mr-3 h-6 sm:h-9" alt="Vertex AI Conversation" />
      <span id='header' contenteditable="true" class="self-center whitespace-nowrap text-xl font-semibold text-black dark:text-white">Nova Dynamics</span>
    </div>
  </nav>
</header>

<div class="container mx-auto bg-[#E2ECF3]" >
  <div class="max-h-full max-w-full bg-[#E2ECF3]">
    <div class="flex max-h-[90vh]">
      <div class="m-6 w-3/5" >
        <h1 id="h1">What is Nova Dyanmics?</h1>
        <input type="file" id="imageUpload" accept="image/*" style="display: none;"> 

        <p class="font-normal text-gray-700 dark:text-gray-400" contenteditable="true">
          Nova Dynamics gives you the expert insights, stock picks, and cutting-edge analysis to crush the crypto markets. Stop missing out – join the revolution today!
        </p>

      
        <p class="mt-6 align-bottom font-normal text-gray-700 dark:text-gray-400">
      
            <button id="toggleButton">-------------- + --------------</button>
        
           
        </p>
        <div id="hiddenElement" >
              
          <label>Agent ID here:</label>
          <input type="text" id="userInput" value="b4d2858e-129a-43b3-ac5e-1e09b74beb9c">
          <br>
          <label>Dubai Travel: </label>
          <input type="text" value="c749604b-867c-4836-a256-cb81c2ee5754" readonly>
          <br>
          <label>Nova Dynamics: </label>
          <input type="text" value="b4d2858e-129a-43b3-ac5e-1e09b74beb9c" readonly>

        </div>

      </div>
      <div class="m-50 w-2/5" style="min-height:500px">
        <script
          src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
        <df-messenger id="agent" 
          project-id="your-project-id"
          agent-id="b4d2858e-129a-43b3-ac5e-1e09b74beb9c"
          language-code="en"
          storage-option="none"
          class="drop-shadow-lg"
          max-query-length=-1>
          <df-messenger-chat id='chat-title'
            chat-title="Vertex AI Conversation"
            bot-writing-text="..."
            placeholder-text="Ask me anything about Nova Dyanmics" />
        </df-messenger>
      </div>
    </div>
  </div>
</div>
