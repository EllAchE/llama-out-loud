import React, { useState } from "react";

function FileUploader() {
  const [file, setFile] = useState(null);
  const [token, setToken] = useState("98c0dfb6-4b72-4e94-8aee-2625b1a3ce91");
  const [uploadStatus, setUploadStatus] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleTokenChange = (event) => {
    setToken(event.target.value);
  };

  const handleUpload = async (event) => {
    event.preventDefault();
    if (!file || !token) {
      setUploadStatus("Please provide both a file and a token.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const options = {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    };

    try {
      const response = await fetch("https://api.vapi.ai/file/upload", options);
      const result = await response.json();
      setUploadStatus(`Upload successful: ${JSON.stringify(result)}`);
    } catch (err) {
      console.error("Upload error:", err);
      setUploadStatus(`Upload failed: ${err.message}`);
    }
  };

  return (
    <div>
      <h3>Upload a File</h3>
      <input type="file" onChange={handleFileChange} />
      <input
        type="text"
        value={token}
        onChange={handleTokenChange}
        placeholder="Enter your authorization token"
      />
      <button onClick={handleUpload}>Upload File</button>
      {uploadStatus && <p>{uploadStatus}</p>}
    </div>
  );
}

export default FileUploader;
