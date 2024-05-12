const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = 3001;
const cors = require("cors");
app.use(cors());
app.use(bodyParser.json());
app.use(express.static("public")); // Serve your React app if it's a static app

// List to hold active clients
const clients = [];

// Middleware for setting SSE response headers
function setupSSE(req, res, next) {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");
  res.flushHeaders(); // flush the headers to establish SSE with the client

  // Function to send data to a client
  const sendEvent = (data) => {
    res.write(`data: ${JSON.stringify(data)}\n\n`);
  };

  // Add the client and sendEvent function to the list
  clients.push(sendEvent);

  // Notify all clients about the new connection
  const joinMsg = { message: "A new user has joined the stream." };
  clients.forEach((client) => (client !== sendEvent ? client(joinMsg) : null));

  // When the client closes connection, remove the listener
  req.on("close", () => {
    clients.splice(clients.indexOf(sendEvent), 1);
    res.end();
  });

  next();
}

// SSE endpoint to subscribe to events
app.get("/events", setupSSE, (req, res) => {
  // Send an initial message to just opened connection
  const initialMsg = { message: "Connected to SSE" };
  res.write(`data: ${JSON.stringify(initialMsg)}\n\n`);
});

// Trigger Event Endpoint
app.post("/trigger", (req, res) => {
  const { message } = req.body;
  // Broadcast the message to all connected SSE clients
  clients.forEach((sendEvent) => sendEvent({ message }));
  res.status(200).send("Message broadcast to all clients");
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
