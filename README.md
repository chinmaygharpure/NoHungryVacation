# NoHungryVacation

NoHungryVacation is a Command-Line Interface(CLI) App which generates a meal plan for users on a vacation based on their location, trip dates, budget, and cuisine preferences. In addition, the algorithm ranks the restaurants by rating and suggests the highest rated restaurants that meet the user criteria. In order to develop this CLI, the Yelp Fusion API and other various Python libraries(datetime, file writing, etc) were used.

## Getting Started 


This tutorial assumes that you have Python3 installed on your computer. 

### Installing

This program uses datetime, json, and the requests libraries. If these are not already installed, then use the command:

pip install (libraryName)


#### Running the CLI

In order to run the CLI, export all three Python files from the repository. Make sure to add them to the same directory on your computer. Navigate to the directory with the files using the command line. Use cd (directoryName) and cd - to move back and forth to the right directory. 

Once you have navigated to the right directory, type in python YelpAPIMenuGenerator.py. After this, a prompt should pop up asking the user for their name. Then, multiple prompts will follow. The details about what the user should input are below. 

##### User Input Information

“Which city are you currently located in?” - Enter the name of the city/area that your vacation or business trip will be in. 

“Which state are you located in? “ - Use the abbreviation of the state. For example, California is CA, Washington is WA, and New York is NY. If you need the abbreviation of the state, this link helps: https://abbreviations.yourdictionary.com/articles/state-abbrev.html

“Which cuisines are you interested in” - Enter one cuisine each time this is prompted. When you don’t want to enter anymore cuisines, type STOP. Cuisines include Mexican, Thai, Pizza, Hot Dogs, etc. 

“What is the most you would spend for a single lunch or dinner?” Enter any number for the max amount you would spend(floats, integers, etc all work). Note that this amount should be in US Dollars(USD). 

“What are the year/month/day that you want to start/end the plan on?” - Enter a 4 digit number for the year. For the month, 1 - January, 2 - February …… 12 - December. For the day, Enter 1 for the 1st, 2 for the 2nd ……. 31 for the 31st.

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
