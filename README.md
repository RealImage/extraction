# extraction
Serverless email attachement extractor

To create a deployment package

Create a folder (examplefolder), and then create a subfolder (node_modules).

Install the Node.js platform. For more information, see the Node.js website.

Install dependencies. The code examples use the following libraries:

AWS SDK for JavaScript in Node.js

gm, GraphicsMagick for node.js

Async utility module

The AWS Lambda runtime already has the AWS SDK for JavaScript in Node.js, so you only need to install the other libraries. Open a command prompt, navigate to the examplefolder, and install the libraries using the npm command, which is part of Node.js.

```
npm install async gm mailparser
```

copy paste the json from sampletest.json to the lambda function.
