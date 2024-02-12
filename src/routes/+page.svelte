<script lang="ts">

  import { Navbar, NavBrand, NavLi, NavUl } from "flowbite-svelte";
  import { A } from "flowbite-svelte";
  import { Heading } from "flowbite-svelte";
  import { onMount } from "svelte";
  import html2canvas from "html2canvas";

  var text = "";
  var time = 0;

  onMount(() => {
    console.log("onmount");

    const submitButton = document.getElementById("submitButton");
    const urlInput = document.getElementById("urlInput");
    const targetIframe = document.getElementById("targetIframe");
    const iframeContainer = document.getElementById("iframeContainer");
    const body = document.getElementById("body");


    submitButton.addEventListener("click", () => {
      const url = urlInput.value;
      document.getElementById("hidediv").style.display = "none";
      document.getElementById("head").style.display = "none";
      document.getElementById("container").setAttribute('class',"") 
      document.getElementById("subcontainer").setAttribute('class',"") 

      document.getElementById("body").setAttribute('class',"");
      document.getElementById("chatdiv").setAttribute('class',"bottom-right-box");


      body.background = url; 
    });

    const displayImage = document.getElementById("displayImage");
    const imageUpload = document.getElementById("imageUpload");

    displayImage.addEventListener("click", function () {
      console.log("image upload");
      imageUpload.click(); // Trigger the hidden file input
    });

    imageUpload.addEventListener("change", function () {
      const file = this.files[0]; // Get the selected file

      if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
          displayImage.src = event.target.result;
        };

        reader.readAsDataURL(file);
      }
    });

    const toggleButton = document.getElementById("toggleButton");
    const hiddenElement = document.getElementById("hiddenElement");
    let isHidden = false; // Keep track of visibility

    toggleButton.addEventListener("click", function () {
      if (isHidden) {
        hiddenElement.style.display = "block"; // Show
        toggleButton.textContent = "-------------- - --------------"; // Change to minus
        isHidden = false;
      } else {
        hiddenElement.style.display = "none"; // Hide
        toggleButton.textContent = "-------------- + --------------"; // Change back to plus
        isHidden = true;
      }
    });

    const userInput = document.getElementById("userInput");
    const agentElement = document.getElementById("agent");

    let img = document.getElementById("displayimage");
    let paragraph = document.getElementById("paragraph");
    let header = document.getElementById("header");
    let h1 = document.getElementById("h1");
    let chattitle = document.getElementById("chat-title");
    header.addEventListener("input", function () {
      console.log("header" + header?.textContent);
      console.log(h1?.textContent);
      h1.textContent = header?.textContent;
      chattitle?.setAttribute("chat-title", header?.textContent + " Vertex AI Search");
      chattitle?.setAttribute("placeholder-text", "Ask me anything about " + header?.textContent);
    });
    userInput.addEventListener("change", function () {
      const inputValue = userInput.value;
      agentElement?.setAttribute("agent-id", inputValue);
      console.log("changed");
      console.log(agentElement?.getAttribute("agent-id"));

      if (userInput.value === "c749604b-867c-4836-a256-cb81c2ee5754") {
        console.log("Dubai Trav");
        header.textContent = "Dubai Travel";
        h1.textContent = "Welcome to Dubai!";
        paragraph.textContent =
          "Step into a world of dazzling contrasts, where towering skyscrapers stand alongside ancient souks, and the desert beckons just beyond the city limits.  Dubai is a destination that redefines luxury, offering unparalleled experiences from Michelin-starred dining to adrenaline-pumping adventures. Embark on your journey into this magnificent oasis.";
        displayImage.setAttribute("src", "dubai.svg");
        chattitle.setAttribute("placeholder-text", "Ask me anything about Dubai");
      }
      if (userInput.value === "b4d2858e-129a-43b3-ac5e-1e09b74beb9c") {
        header.textContent = "Nova Dynamics";
        h1.textContent = "What is Nova Dynamics?";
        paragraph.textContent =
          "Nova Dynamics gives you the expert insights, stock picks, and cutting-edge analysis to crush the crypto markets. Stop missing out – join the revolution today!";
        displayImage.setAttribute("src", "nova.jpg");
        chattitle.setAttribute("placeholder-text", "Ask me anything about Nova Dynamics");
      }
    });
  });
</script>

<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

  <style>

    .navbar-brand {
      display: flex;
      align-items: center;
    }
    #h1 {
      /* More specificity to potentially override conflicts */
      font-size: 2.5em; /* Make it larger */
      font-weight: bold;
      margin-bottom: 1em; /* Add some spacing for visual separation */
    }
    #iframeContainer {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            visibility: hidden; /* Initially hide the iframe */
        }
        .bottom-right-box {
          position: fixed; /* Or 'absolute' if you want it positioned within the container */
  bottom: 20px;    /* Distance from the bottom */
  right: 20px;     /* Distance from the right */
  width: 300px;    /* Adjust the width */
  height: 400px;   /* Adjust the height */
  background-color: #fff;  /* White background */
  border-radius: 8px;      /* Rounded corners */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); /* Subtle shadow */
  padding: 15px;   /* Internal padding for chat content */
  overflow-y: auto; /* Add a scrollbar if content exceeds height */
}

  </style>
</head>
<header class="bg-[#B1D6FC]" id="head">
  <nav>
    <div class="navbar-brand">
      <img id="displayImage" src="nova.jpg" class="mr-3 h-6 sm:h-9" alt="Vertex AI Conversation" />
      <span
        id="header"
        contenteditable="true"
        class="self-center whitespace-nowrap text-xl font-semibold text-black dark:text-white"
        >Nova Dynamics</span>
    </div>
  </nav>
</header>

<div class="container mx-auto bg-[#E2ECF3]" id="container">
  <div class="max-h-full max-w-full bg-[#E2ECF3]" id="subcontainer">
    <div class="flex max-h-[90vh]">
      <div class="m-6 w-3/5" id="hidediv">
        <h1 id="h1">What is Nova Dyanmics?</h1>
        <input type="file" id="imageUpload" accept="image/*" style="display: none;" />

        <p
          id="paragraph"
          class="font-normal text-gray-700 dark:text-gray-400"
          contenteditable="true">
          Nova Dynamics gives you the expert insights, stock picks, and cutting-edge analysis to
          crush the crypto markets. Stop missing out – join the revolution today!
        </p>

        <p class="mt-6 align-bottom font-normal text-gray-700 dark:text-gray-400">
          <button id="toggleButton">-------------- + --------------</button>
        </p>
        <div id="hiddenElement">
          <label>Agent ID: </label>
          <input type="text" id="userInput" list="itemDatalist" />
          <datalist id="itemDatalist">
            <option value="b4d2858e-129a-43b3-ac5e-1e09b74beb9c" label="Nova Dynamics" /><option
            <option value="4b1546ef-fb28-4dca-972a-190c7c6dbc8b" label="DubaiEvent" /><option
              value="c749604b-867c-4836-a256-cb81c2ee5754"
              label="Dubai Travel" /></datalist>
              <br>
              <label>Background:</label>

              <input type="text" id="urlInput" list="urllist" />
          <datalist id="urllist">
                <option value="https://screenshot.googleplex.com/7gNWrAHAFBeWqtq.png" label="Dubai" /><option/>
              </datalist>

          <button class="btn btn-primary" id="submitButton">Use background from Screenshot (URL) instead</button>
          <div id="iframeContainer">
          <iframe id="targetIframe" src="https://html2canvas.hertzen.com/" />
        </div>
        </div>
      </div>
      <div class="m-50 w-2/5" style="min-height:500px" id="chatdiv">
        <script
          src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
        <df-messenger
          id="agent"
          project-id="your-project-id"
          agent-id="b4d2858e-129a-43b3-ac5e-1e09b74beb9c"
          language-code="en"
          storage-option="none"
          class="drop-shadow-lg"
          max-query-length="-1">
          <df-messenger-chat
            id="chat-title"
            chat-title="Vertex AI Conversation"
            bot-writing-text="..."
            placeholder-text="Ask me anything about Nova Dyanmics" />
        </df-messenger>
      </div>
    </div>
  </div>
</div>
