import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import Vapi from "@vapi-ai/web";

function App() {
  const [message, setMessage] = useState("");

  // Create a ref for the Vapi instance
  const vapiRef = React.useRef(null);

  useEffect(() => {
    // Initialize the Vapi instance only once when the component mounts
    vapiRef.current = new Vapi("8aa55f4a-50ea-4ceb-b3f7-cef74ef7459e");

    // vapi.on("speech-start", () => {
    //   console.log("Assistant speech has started.");
    // });

    // vapi.on("speech-end", () => {
    //   console.log("Assistant speech has ended.");
    // });

    // vapi.on("call-start", () => {
    //   console.log("Call has started.");
    // });

    // vapi.on("call-end", () => {
    //   console.log("Call has ended.");
    // });

    const assistantOverrides = {
      transcriber: {
        provider: "deepgram",
        model: "nova-2",
        language: "en-US",
      },
      recordingEnabled: false,
      variableValues: {
        name: "Steve Jobs",
      },
    };

    vapiRef.current.start(
      "3f4593ce-5141-4c16-9847-21b86463bb92",
      assistantOverrides
    );

    // Cleanup function to possibly disconnect or clean up the Vapi instance when the component unmounts
    return () => {
      if (vapiRef.current) {
        // Perform cleanup if needed, such as disconnecting the Vapi session
      }
    };
  }, []); // The empty dependency array ensures this effect runs only once

  const handleClick = () => {
    console.log("Sending message:");
    console.log(message);

    if (vapiRef.current) {
      vapiRef.current.send({
        type: "add-message",
        message: {
          role: "system",
          content: message,
        },
      });
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter your message"
        />
        <button onClick={handleClick}>Send Message</button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
