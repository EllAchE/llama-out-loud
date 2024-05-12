const Vapi = require("@vapi-ai/web");

const vapi = Vapi("8aa55f4a-50ea-4ceb-b3f7-cef74ef7459e");

const assistantOverrides = {
  transcriber: {
    provider: "deepgram",
    model: "nova-2",
    language: "en-US",
  },
  recordingEnabled: false,
  variableValues: {
    name: "John",
  },
};

vapi.start("3f4593ce-5141-4c16-9847-21b86463bb92", assistantOverrides);
