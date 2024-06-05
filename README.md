# Identification-of-Fish-Species
The Below image depicts a basic structure of a neural network used for image classification, specifically for identifying different types of fish. Here's a detailed explanation. <br></br>

![Picture1](https://github.com/srinivas21109/Identification-of-Fish-Species/assets/119849011/cc4ef9fb-1dd9-493b-8ed9-332def49ecfe)
<br></br>
<H3><B>Neural Network Structure</B></H3> 

<OL>
<LI><B>Input Layer:</B> <BR>
The image of a fish, in this case, a goldfish, is fed into the neural network. The pixels of the image are used as the input data. Each pixel value is a feature that the network will use to learn and make predictions.</LI> <BR>
<LI><B>Hidden Layers:</B> <BR>
The network contains multiple hidden layers. These layers consist of interconnected neurons.Each neuron in a hidden layer takes input from the neurons in the previous layer, processes it, and passes the output to the neurons in the next layer. The connections between neurons are weighted, and these weights are adjusted during the training process to minimize the error in predictions.</LI>
<BR>
<LI><B>Output Layer:</B> <BR>
The output layer consists of neurons corresponding to the possible classes the network can predict. In this example, there are three classes: Gold Fish, Indian Carp, and Goby.Each neuron in the output layer represents the probability of the input image belonging to a particular class.</LI>
</OL>
  <BR></BR>
  
![Picture2](https://github.com/srinivas21109/Identification-of-Fish-Species/assets/119849011/93d94492-7512-4959-b933-510d19ea6c32)

<br></br>

<H3>User Interface</H3>
The interface is designed to be highly accessible and functional:<BR>
<ol>
<li><b>Sidebar with Fish Species List:</b> The sidebar contains a scrollable list of fish species that the model can recognize, each accompanied by an icon for easy identification.</li><BR>
<li><b>Upload and Capture Options:</b> Users can select to upload an image file or capture a new image using their device's camera.</li><BR>
<li><b>Drag-and-Drop Upload Area:</b> A dedicated area where users can drag and drop image files for classification.</li><BR>
<li><b>Image Upload Limitations:</b> Clearly states the file size limit and supported formats to ensure users provide compatible images.</li><BR>
</ol>
<BR></BR>

![Picture3](https://github.com/srinivas21109/Identification-of-Fish-Species/assets/119849011/50cd8f62-a382-4ea6-9809-2fd0aa67cbc8)

<br></br>
The image depicts a user interface for fish species identification. The uploaded image shows several goldfish swimming. The system has detected the class as "fish" and identified the species as "Gold Fish." On the left side, there's a list of various fish species, each with an icon, providing options for users to explore different types of fish.
<BR></BR>

![Picture4](https://github.com/srinivas21109/Identification-of-Fish-Species/assets/119849011/360efe91-dd21-412a-b397-788c2b53bd93)
The model has identified the fish in the image as a Goby with a confidence level of 100.00%. This indicates that the model is completely certain that the fish belongs to the Goby species. On the other hand, the model has a 0.00% confidence level for other fish species, including Snakehead, Catfish, Janitor Fish, and Mudfish. This means the model is entirely sure that the fish is not any of these species.
<BR></BR>
![Picture5](https://github.com/srinivas21109/Identification-of-Fish-Species/assets/119849011/02975bba-0cc1-4e1e-ab87-83a468afd5d3)
<br>
The model was unable to classify the image as it does not match any of the known classes in the dataset. The message displayed is:<BR></BR>

"Your image doesn't belong to any of our classes 😔"<BR></BR>

This indicates that the image provided, which appears to be a picture of a horse, does not correspond to any of the fish species listed in the model's classification categories. The listed categories include various types of fish such as Bangus, Big Head Carp, Black Spotted Barb, Catfish, Climbing Perch, Fourfinger Threadfin, Freshwater Eel, Glass Perchlet, Goby, Gold Fish, Gourami, Grass Carp, Green Spotted Puffer, and several others. Since a horse is not a fish, the model correctly identifies that the image does not belong to any of its predefined classes.
