const express = require("express");
const multer = require("multer");
const cors = require("cors");
const { exec } = require("child_process");
const fs = require("fs");

const app = express();
const upload = multer({ dest: "uploads/" });

app.use(cors());
app.use(express.json());

app.post("/api/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: "No file uploaded" });
  }

  const inputPath = req.file.path; // FIXED LINE
  const outputPath = `${inputPath}_out.txt`;

  // console.log("Input path:", inputPath);
  // console.log("Output path:", outputPath);


  exec(`python3 processor.py ${inputPath} ${outputPath}`, (err) => {
    if (err) {
      console.error("Python script failed:", err);
      return res.status(500).send("Python script failed");
    }

    const result = fs.readFileSync(outputPath, "utf-8");
    res.json({ content: result, originalFilePath: inputPath });

    fs.unlinkSync(inputPath);
    fs.unlinkSync(outputPath);
  });
});

app.post("/api/download", express.json(), (req, res) => {
  const { originalFilePath, newData } = req.body;

  if (!originalFilePath || !newData) {
    return res.status(400).json({ error: "Missing original file or new data" });
  }

  const outputPath = `${originalFilePath}_modified.csv`;

  // Write the dictionary to a temp JSON file
  const jsonPath = `${originalFilePath}_map.json`;
  fs.writeFileSync(jsonPath, JSON.stringify(newData));

  console.log("Running modifier.py with:");
  console.log("Original File:", originalFilePath);
  console.log("Value Map JSON:", jsonPath);

  exec(`python3 modifier.py ${originalFilePath} ${jsonPath} ${outputPath}`, (err) => {
    if (err) {
      console.error("Python script failed:", err);
      return res.status(500).send("Python script failed");
    }

    const result = fs.readFileSync(outputPath, "utf-8");
    res.json({ content: result });

    fs.unlinkSync(outputPath);
    fs.unlinkSync(jsonPath);
  });
});

const port = process.env.PORT || 10000;
app.listen(port, () => console.log(`Backend running on ${port}`));
