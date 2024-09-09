# End To End Iris Classification Project with Flask

This project is a simple end-to-end machine learning project that uses the Iris dataset to classify the species of an iris flower. The project uses a K-nearest neighbour classifier to make predictions and is deployed using Flask.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the project, follow these steps:
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Run the Flask app using `python app.py`

## Usage


To use the project, follow these steps:
1. Open the browser and navigate to `http://localhost:5000/predict/df`
2. Add the values for the sepal length, sepal width, petal length, and petal width to url parameters. Example: 
```
http://localhost:5000/predict/np?sl=2&sw=1.5&pl=1.0&pw=0.7
```
3. Click the `Enter` button to make a prediction
4. The predicted species will be displayed on the screen. Example Response: 
```json
{
"class": "Versicolor",
"code": 200,
"input": {
    "petal length": 2,
    "petal wwidth": 1.5,
    "sepal length": 1.0,
    "sepal width": 0.7
},
"message": "Prediction Successful",
"model": "DattFrame Model",
"result": 0,
"status": "SUCCESS"
}
```


## Contributing

To contribute to the project, follow these steps:
1. Fork the project
2. Create a new branch (`git checkout -b feature-branch`)
3. Make the appropriate changes in the files
4. Add changes to reflect the changes made
5. Commit your changes (`git commit -am 'Feature added'`)
6. Push to the branch (`git push origin feature-branch`)
7. Create a Pull Request
8. Enjoy your new feature!

## License

This project uses the following license: [MIT](LICENSE)
