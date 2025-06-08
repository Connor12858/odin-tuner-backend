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
  const inputPath = `/tmp/${req.file.filename}`;
  const outputPath = `/tmp/${req.file.filename}_out.txt`;

  exec(`python3 processor.py ${inputPath} ${outputPath}`, (err) => {
    if (err) return res.status(500).send("Python processing failed");

    const result = fs.readFileSync(outputPath, "utf-8");
    res.json({ content: result });

    fs.unlinkSync(inputPath);
    fs.unlinkSync(outputPath);
  });
});

const port = process.env.PORT || 10000;
app.listen(port, () => console.log(`Backend running on ${port}`));
