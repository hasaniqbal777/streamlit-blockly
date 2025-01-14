<template>
  <div class="blockly-container">
    <div ref="blocklyDiv" class="blocklyDiv" :style="customStyles"></div>
    <button v-if="showButton" @click="submitCode" class="submit-btn">
      Submit Code
    </button>
  </div>
</template>

<script>
import { ref, shallowRef, onMounted } from "vue";
import * as Blockly from "blockly/core";
import * as En from "blockly/msg/en";
import { javascriptGenerator } from "blockly/javascript";
import { pythonGenerator } from "blockly/python";
import { luaGenerator } from "blockly/lua";
import { dartGenerator } from "blockly/dart";
import { phpGenerator } from "blockly/php";
import { Streamlit } from "streamlit-component-lib";
import { useStreamlit } from "../streamlit";
import { toolbox } from "../blocks/toolbox";

// Load Blockly blocks
import "blockly/blocks";
import "../blocks/custom";


export default {
  name: "BlocklyComponent",
  props: ["args"], // Props for arguments passed from Python
  setup(props) {
    useStreamlit(); // For Streamlit lifecycle hooks

    const blocklyDiv = ref(null);
    const workspace = shallowRef(null);

    // Custom styles for the Blockly workspace
    const customStyles = {
      width: props.args.width || "100%", // Default to full width
      height: props.args.height || "500px", // Default to 500px height
      border: props.args.border || "1px solid #ccc", // Default border
      boxSizing: props.args.boxSizing || "border-box", // Default box-sizing
    };

    const showButton = props.args.showButton ?? true; // Default to showing the button

    const submitCode = () => {
      try {
        console.log("submitCode called"); // Debug: Check if function is triggered
        const GeneratorLanguage = props.args.GeneratorLanguage || "javascript";
        let generator;
        switch (GeneratorLanguage) {
          case "javascript":
            generator = javascriptGenerator;
            break;
          case "python":
            generator = pythonGenerator;
            break;
          case "lua":
            generator = luaGenerator;
            break;
          case "dart":
            generator = dartGenerator;
            break;
          case "php":
            generator = phpGenerator;
            break;
          default:
            console.error(`Unsupported generator language: ${GeneratorLanguage}`);
            return;
        }

        const code = generator.workspaceToCode(workspace.value);
        console.log("Generated code:", code); // Debug: Log the generated code
        Streamlit.setComponentValue(code); // Send generated code to Streamlit
      } catch (error) {
        console.error("Error generating code:", error);
      }
    };

    onMounted(() => {
      try {
        Blockly.setLocale(En); // Always use English for messages

        Blockly.Themes.Streamlit = Blockly.Theme.defineTheme('streamlit', {
          'base': Blockly.Themes.Classic,
          'componentStyles': {
            'toolboxBackgroundColour': '#f0f2f6',
            'flyoutBackgroundColour': '#f0f2f6',
            'scrollbarColour': '#b0acb4',
          },
          'startHats': true // Show hat blocks at the beginning of each block category
        });

        const options = {
          theme: Blockly.Themes.Streamlit,
          toolbox: props.args.toolbox || toolbox,
          grid: props.args.grid || {},
          trashcan: props.args.trashcan ?? true,
          zoom: props.args.zoom || {
            controls: true,
            wheel: true,
            startScale: 1,
            maxScale: 3,
            minScale: 0.3,
            scaleSpeed: 1.2,
          },
        };

        // Validate toolbox XML before injecting Blockly
        try {
          const parser = new DOMParser();
          const xmlDoc = parser.parseFromString(options.toolbox, "text/xml");
          const errors = xmlDoc.getElementsByTagName("parsererror");
          if (errors.length > 0) {
            console.error("Invalid toolbox XML:", options.toolbox);
            throw new Error("Toolbox XML is invalid.");
          }
        } catch (xmlError) {
          console.error("Error parsing toolbox XML:", xmlError);
          return;
        }

        // Add comment options to the context menu
        Blockly.ContextMenuItems.registerCommentOptions();

        // Inject Blockly workspace
        workspace.value = Blockly.inject(blocklyDiv.value, options);

        // Automatically emit code on changes if the button is hidden
        if (!showButton) {
          workspace.value.addChangeListener(() => {
            console.log("Workspace changed"); // Debug: Check if change listener is triggered
            submitCode();
          });
        }
      } catch (error) {
        console.error("Error initializing Blockly:", error);
      }
    });

    return {
      blocklyDiv,
      customStyles,
      submitCode,
      showButton,
    };
  },
};
</script>

<style>
.blockly-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.blocklyDiv {
  width: 100%;
  height: 100%;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.blocklyComment .blocklyCommentPreview.blocklyText {
  color: black;
  fill: black
}

.blocklyComment .blocklyText {
  color: black;
}

.blocklyTextInputBubble .blocklyTextarea {
  color: #000 !important;
}


.submit-btn {
  display: inline-flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  font-weight: 400;
  padding-top: 0.25rem;
  padding-right: 0.75rem;
  padding-bottom: 0.25rem;
  padding-left: 0.75rem;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
  min-height: 2.3rem;
  margin-top: 2px;
  margin-right: 0px;
  margin-bottom: 0px;
  margin-left: 0px;
  line-height: 1.6;
  text-transform: none;
  font-size: inherit;
  font-family: inherit;
  color: inherit;
  width: 100%;
  cursor: pointer;
  background-color: rgb(255, 255, 255);
  border-top-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  border-left-width: 1px;
  border-top-style: solid;
  border-right-style: solid;
  border-bottom-style: solid;
  border-left-style: solid;
  border-top-color: rgba(49, 51, 63, 0.2);
  border-right-color: rgba(49, 51, 63, 0.2);
  border-bottom-color: rgba(49, 51, 63, 0.2);
  border-left-color: rgba(49, 51, 63, 0.2);
  border-image-source: none;
  border-image-slice: 100%;
  border-image-width: 1;
  border-image-outset: 0;
  border-image-repeat: stretch;
}

.submit-btn:hover {
  border-top-color: rgb(255, 75, 75);
  border-right-color: rgb(255, 75, 75);
  border-bottom-color: rgb(255, 75, 75);
  border-left-color: rgb(255, 75, 75);
  color: rgb(255, 75, 75);
}

.submit-btn:active {
  background-color: rgb(255, 75, 75);
  border-top-color: rgb(255, 75, 75);
  border-right-color: rgb(255, 75, 75);
  border-bottom-color: rgb(255, 75, 75);
  border-left-color: rgb(255, 75, 75);
  color: rgb(255, 255, 255);
}
</style>