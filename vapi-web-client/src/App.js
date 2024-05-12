import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Vapi from "@vapi-ai/web";
import FileUploader from "./components/FileUploader";

function App() {
  const [message, setMessage] = useState("");
  const vapiRef = useRef(null);

  useEffect(() => {
    const eventSource = new EventSource("http://localhost:3001/events");
    eventSource.onmessage = function (event) {
      const { message } = JSON.parse(event.data);
      console.log("Received message:", message);
      setMessage(message);
      handleClick(message);
    };

    return () => {
      eventSource.close();
    };
  }, []);

  useEffect(() => {
    vapiRef.current = new Vapi("8aa55f4a-50ea-4ceb-b3f7-cef74ef7459e");
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
  }, []);

  const handleClick = (incomingMessage) => {
    const finalMessage = incomingMessage || message;
    console.log("Sending message:", finalMessage);
    if (vapiRef.current) {
      vapiRef.current.send({
        type: "add-message",
        message: {
          role: "system",
          content: finalMessage,
        },
      });
    }
  };

  return (
    <div className="App d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <input
          type="text"
          className="form-control mb-2"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter your message"
        />
        <button className="btn btn-primary" onClick={() => handleClick(null)}>
          Send Message
        </button>
        <FileUploader />
      </div>
    </div>
  );
}

export default App;
